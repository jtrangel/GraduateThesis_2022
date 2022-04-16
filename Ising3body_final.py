#!/usr/bin/env python
# coding: utf-8

# In[1]:


import qiskit


# In[2]:


qiskit.__qiskit_version__


# In[3]:


#Importing necessary packages from qiskit, numpy, math and matplotlib
from qiskit import ClassicalRegister, QuantumRegister, QuantumCircuit, Aer, execute
import numpy as np 
import math as m
import matplotlib
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from qiskit.tools.visualization import plot_histogram

#Statevector simulator which is the main backend used
S_simulator = Aer.backends(name='statevector_simulator')[0] 


# In[4]:


#***************************************************************************************
#  -The functions used in this code were mainly developed by Koch, et al. with minor 
#   adjustments and changes to fit the model and matrix derivations done in Chapter 3 - 
#
#    Title: Fundamentals In Quantum Algorithms: A Tutorial Series Using Qiskit Continued
#    Author: Koch, Daniel and Patel, Saahil and Wessing, Laura and Alsing, Paul M.
#    Date: 2020
#    Availability: 10.48550/ARXIV.2008.10647
#
#***************************************************************************************


# In[5]:


def Ub_Mixer(qc, q, beta, Vert):
    #Input: qc (QuantumCircuit) q (QuantumRegister) beta (hyperparameter) Vert (counting array
    #       with external magnetic field values)
    #Applies the quantum logic gates for a U(B,beta) operation using Rx, Ry, and CNOT gates
    qc.barrier()
    for v in np.arange( len(Vert) ):
        qc.rx( -2*beta, q[int(Vert[v][0])] ) #Rx gates
    #CNOT gates for entanglement
    qc.cx( q[0], q[1] )    
    qc.cx( q[2], q[0] )
    for v2 in np.arange( len(Vert) ):
        qc.ry( -2*beta, q[int(Vert[v2][0])] ) #Ry gates


# In[13]:


def Uc_Ising(qc, q, gamma, Vert, Edge):
    #Input: qc (QuantumCircuit) q (QuantumRegister) gamma (hyperparameter) Vert (counting array 
    #       with h-values) Edge (array describing qubit/spin relations)
    #Applies the quantum logic gates for a U(C,gamma) operation using Rz and CNOT gates
    J = [1.5,-3,1.5] #Values for J 
    for e in np.arange( len(Edge) ): # Z_i Z_j
        qc.cx( q[int(Edge[e][0])], q[int(Edge[e][1])] ) #Ancilla CNOT gates with Rz gate
        qc.rz(-2*gamma*J[e], q[int(Edge[e][1])] ) #Rz gate encoding coupling coefficient (J) values
        qc.cx( q[int(Edge[e][0])], q[int(Edge[e][1])] )
    qc.barrier()
    for v in np.arange( len(Vert) ): # Z_gamma
        qc.rz(-2*gamma*(Vert[v][1]), q[int(Vert[v][0])] ) #Rz gate encoding external magnetic field (h) effects


# In[7]:


def Ising_Circuit(qc, q, V, E, beta, gamma, **kwargs):
    #Input: qc (QuantumCircuit) q (QuantumRegister) V (Vert array) E (Edge array) beta (hyperparameter)
    #       gamma (hyperparameter)
    #Forms Quantum Circuit for given geometry parameters in V, E and phase parameters in beta, gamma
    Uc_Ising(qc,q,gamma,V,E) 
    Ub_Mixer(qc,q,beta,V)


# In[8]:


def Binary(N, total, LSB):
    #Input: N (integer) total (integer) LSB (string -least significant bit)
    #Gives base-2 binary equivalent of N with LSB notation. 
    #Used for listing down possible states for N qubits
    qubits = int(m.log(total,2))
    b_num = np.zeros(qubits)
    for i in np.arange(qubits):
        if( N/((2)**(qubits-i-1)) >= 1 ):
            if(LSB=='R'):
                b_num[i] = 1
            if(LSB=='L'):
                b_num[int(qubits-(i+1))] = 1
            N = N - 2**(qubits-i-1)
    B = []
    for j in np.arange(len(b_num)):
        B.append(int(b_num[j]))
    return B


# In[14]:


def Ising_Energy(V, E, **kwargs):
    #Input: V (Vert array) E (Edge array) 
    #Manually solves for the energy of each configuration based on the set Hamiltonian
    #This is solved for comparative purposes
    Energies = []
    States = []
    J = [1.5,-3,1.5] #coupling coefficient values
    for s in np.arange( 2**len(V) ):
        B = Binary(int(s),2**len(V),'L') 
        B2 = []
        for i in np.arange(len(B)):
            if( B[i] == 0 ):
                B2.append(1)  #when binary state is 0, Ising value=1
            else:
                B2.append(-1) #Ising value = -1 otherwise
        state = ''
        energy = 0
        for s2 in np.arange(len(B)):
            state = state+str(B[s2])
            energy = energy - V[s2][1]*B2[s2] #2nd term of cost function
        States.append(state) #Lists down states 
        for j in np.arange( len(E) ):
            energy = energy - J[j] * B2[int(E[j][0])] * B2[int(E[j][1])]
        Energies.append(energy) #Lists down corresponding energy per state
    return Energies,States 


# In[10]:


def Ising_Gradient_Descent(qc, q, Circ, V, E, beta, gamma, epsilon, En, step):
    #Input: qc (QuantumCircuit) q (QuantumRegister) Circ (Ising_Circuit function) V (Vert array)
    # E (Edgearray) beta (hyperparameter) gamma (hyperparameter) epsilon (optimization parameter)
    # En (Energies) step (step size)
    # Uses Gradient Descent optimization to determine the next values for gamma and beta 
    params = [ [beta+epsilon,gamma],[beta-epsilon,gamma],[beta,gamma+epsilon],[beta,gamma-epsilon] ]
    ev = []
    for i in np.arange( 4 ):
        q = QuantumRegister(len(V))
        qc= QuantumCircuit(q)
        for hh in np.arange(len(V)):
            qc.h( q[int(hh)] )
        Circ( qc, q, V, E, params[i][0], params[i][1])
        ev.append( E_Expectation_Value( qc, En ) )
    beta_next = beta - ( ev[0] - ev[1] )/( 2.0*epsilon ) * step
    gamma_next = gamma - ( ev[2] - ev[3] )/( 2.0*epsilon ) * step
    return beta_next, gamma_next


# In[11]:


def E_Expectation_Value( qc, Energies ):
    #Input: qc (QuantumCircuit) Energies (array)
    #Gets the current statevector and solves its expectation value 
    SV = execute( qc, S_simulator, shots=1 ).result().get_statevector()
    EV = 0
    for i in np.arange( len(SV) ):
        EV = EV + Energies[i] *abs( SV[i] * np.conj(SV[i]) )
    EV = round(EV,4)
    return EV


# In[12]:


def Top_States(States, Energies, SV, top):
    #Input: States (array) Energies (array) SV (Qiskit statevector) top (integer)
    #Displays the top most probable states in the system, and their associated energy
    #Used by Koch et al. for better visualization of the Qiskit output statevector
    P = []
    S = []
    E = []
    for a in np.arange( top ):
        P.append(-1)
        S.append('no state')
        E.append('no energy')
    for i in np.arange(len(States)):
        new_top = False
        probs = abs(SV[i]*np.conj(SV[i]))*100
        state = States[i]
        energ = Energies[i]
        j = 0
        while( (new_top == False) and (j < top) ):
            if( probs > P[j] ):
                for k in np.arange( int( len(P) - (j+1) ) ):
                    P[int( -1-k )] = P[int( -1-(k+1) )]
                    S[int( -1-k )] = S[int( -1-(k+1) )]
                    E[int( -1-k )] = E[int( -1-(k+1) )]
                P[j] = probs
                S[j] = state
                E[j] = energ
                new_top = True
            j = int(j+1)
    for s in np.arange( top ):
        print('State ',S[s],' Probability: ',round(P[s],2),'%',' Energy: ',round(E[s],2))


# In[15]:


#Parameters for Gradient Descent
epsilon = 0.001 
#step_size=0.01
step_size = 0.001
delta = 0.002
#-------------------------------------------------------
#Geometry parameters and external magnetic field
Vert = [ [0,0.01] , [1,0.01] , [2,0.01] ] #h
Edge = [ [0,1],[1,2],[0,2] ] #relationship between spins/qubits
#-------------------------------------------------------
#Initial values for optimization 
Energies,States = Ising_Energy(Vert,Edge)
EV = 100
EV_old = 1000
EV_min = 1000
#-------------------------------------------------------
#Phase parameters/optimization hyperparameters
gamma = -5
beta = -4
s = 0
#-------------------------------------------------------
#Main part of the algorithm which attempts to find absolute minimum energy of quantum system
while( (abs( EV - EV_old ) > delta) and ( EV < EV_old ) ):
    q = QuantumRegister(len(Vert))
    c = ClassicalRegister(len(Vert))
    qc= QuantumCircuit(q,c)
    for hh in np.arange(len(Vert)):
        qc.h( q[int(hh)] )
    if( s != 0 ):
        beta,gamma = Ising_Gradient_Descent(qc,q,Ising_Circuit,Vert,Edge,beta,gamma,epsilon,Energies,step_size)
    Ising_Circuit( qc, q, Vert, Edge, beta, gamma)
    EV_old = EV
    EV = E_Expectation_Value( qc, Energies )
    if( EV < EV_min ):
        Params = [beta,gamma]
        EV_min = EV
    s = int(s+1)
    print('E(\u03B3,\u03B2): ',np.around(EV,3),' \u03B3 = ',round(gamma,6),' \u03B2 = ',round(beta,6),'step =',s)


# In[17]:


#Checking how well the algorithm found the lowest energy
print(Energies,States)


# In[18]:


#Quantum circuit visualization using matplotlib
qc.draw(output='mpl')


# In[35]:


#Running the circuit via the statevector simulator for histogram visualization
def run_circuit(circuit,shots):
    exec = execute(circuit, backend = S_simulator, shots = shots)
    result = exec.result()
    return result,result.get_counts(circuit)


# In[36]:


#Histogram visualization
from matplotlib import style
style.use("dark_background")

shots = 1000
run,counts = run_circuit(qc,shots)
plot_histogram(counts)


# In[39]:


#States,corresponding probabilities and energies
SV = run.get_statevector()
Top_States(States,Energies,SV,8)
#Verifying statevector as a complex value
print(SV)


# In[19]:


#Adding measurement so that quantum circuit can be run on qasm simulator or actual quantum computers
qc.measure([0,1,2],[0,1,2])
simulator = Aer.get_backend('qasm_simulator')


# In[20]:


#Visualization of quantum circuit with measurements
qc.draw(output='mpl')


# In[43]:


#Connecting to the IBM cloud backend
from qiskit import IBMQ

IBMQ.save_account('******************************************************************...')
IBMQ.load_account()


# In[44]:


#Checking of quantum computer queues

provider = IBMQ.get_provider("ibm-q")
for backend in provider.backends():
    try:
        qubit_count = len(backend.properties().qubits)
    except:
        qubit_count = "simulated"
    print(f"{backend.name()} has {backend.status().pending_jobs} queued and {qubit_count} qubits")    


# In[76]:


#Code for monitoring quantum computer run
from qiskit.tools.monitor import job_monitor

backend = provider.get_backend("ibmq_lima")
job = execute(qc, backend = backend, shots = 1000)
job_monitor(job)


# In[87]:


#Get number of occurences per configuration
result = job.result()
counts = result.get_counts(qc)

#Visualization of results
plot_histogram(counts)


# In[79]:


#View specific run parameters and results 
print(result)

