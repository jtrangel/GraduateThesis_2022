from doctest import run_docstring_examples
from telnetlib import DO
from turtle import done, down, width
from typing_extensions import runtime
from cv2 import circle, line
from manim import *
from regex import D
from sklearn.preprocessing import scale
from manimlib import *


class vid1(Scene):
    def construct(self):
        background = ImageMobject("slide.jpg")
        self.add(background)
        self.bring_to_back(background)

        nip = ImageMobject("niplogo2.png")
        nip.to_edge(DOWN + RIGHT)
        nip.shift(DOWN + 0.9*RIGHT)
        nip.scale(0.45)

        sand = ImageMobject("sandlogo.png")
        sand.next_to(nip,LEFT)
        sand.scale(1.65)
        
        self.add(nip,sand)

        titlefont = 52
        title1 = Text("Qiskit Implementation of", font_size= titlefont)
        title2 = Text("the 3-body Ising Model", font_size= titlefont)
        title3 = Text("for alternating coupling", font_size= titlefont)
        title4 = Text("constant chains", font_size= titlefont)
        
        titles = VGroup()
        titles.add(title1,title2,title3,title4)
        titles.arrange(DOWN, center = True, buff = 0.2)
        titles.shift(0.5*UP)

        pic = ImageMobject("grad3.jpg").scale(0.6)
        #pic = ImageMobject("gradpic.jpg").scale(0.24)

        infofont = 15
        info1 = Text("Jerico Rangel, IV - BS Applied Physics", font_size = infofont)
        info1.shift(2.5*DOWN + 2*LEFT)
        info2 = Text("Structure and Dynamics Laboratory", font_size = infofont)
        info3 = Text("Advised by: Dr. Cristine DLR Villagonzalo", font_size = infofont)
        info4 = Text("jrangel@nip.upd.edu.ph", font_size = infofont)

        infos = VGroup()
        infos.add(info1,info2,info3,info4)
        infos.arrange(DOWN, center = False, aligned_edge = LEFT, buff=0.1)
        pic.next_to(infos, LEFT)
        pic.shift(0.1*UP)
            
        self.add(infos, pic)
        self.play(DrawBorderThenFill(titles), run_time = 2)
        self.wait(1)
        self.play(FadeOut(titles), FadeOut(infos), FadeOut(pic))
        self.wait(0.5)

class vid2(Scene):
    def construct(self):
        background = ImageMobject("slide.jpg")
        self.add(background)
        self.bring_to_back(background)

        nip = ImageMobject("niplogo2.png")
        nip.to_edge(DOWN + RIGHT)
        nip.shift(DOWN + 0.9*RIGHT)
        nip.scale(0.45)

        sand = ImageMobject("sandlogo.png")
        sand.next_to(nip,LEFT)
        sand.scale(1.65)
        
        self.add(nip,sand)

        headerfont = 33
        labelfont = 22

        qcomp = Text("Quantum Computing", font_size = headerfont)
        qcomp.shift(2.3*UP+3.2*LEFT)

        qubits = Text("2 Qubits", font_size=labelfont)
        qubits.next_to(qcomp, DOWN)
        qubits.shift(0.5*RIGHT + 0.5*DOWN)
        qubits2 = Text("Qubits", font_size=25)
        qubits2.next_to(qubits, RIGHT)
        qubits2.shift(RIGHT)
        blist1 = BulletedList("Quantum Parallelism", "Entanglement", "Interference")
        blist1.next_to(qcomp,DOWN)
        blist1.shift(0.8*DOWN)
        speedup = Text(" - 'Significant' speedups", font_size = 29)
        speedup.next_to(qcomp, RIGHT)

        psi_1 = MathTex("\\vert \\Psi \\rangle &= c_0 \\vert 00 \\rangle \\\ &+ c_1 \\vert 01 \\rangle")
        psi_2 = MathTex("&+ c_2 \\vert 10 \\rangle \\\ &+ c_3 \\vert 11 \\rangle")
        psi_1.next_to(qubits, DOWN)
        psi_2.next_to(psi_1, DOWN)
        psi_2.shift(0.35*RIGHT)

        bitlabel = Text("2 Bits", font_size=labelfont)
        bitlabel.next_to(qubits, RIGHT)
        bitlabel.shift(3*RIGHT)
        bits = MathTex("&00 \\\ &01 \\\ &10 \\\ &11")
        bits.next_to(bitlabel,DOWN)
        bits.shift(0.1*DOWN)

        #qubits in ket
        ket_0 = MathTex("\\vert 0 \\rangle = \\begin{bmatrix} 1 \\\ 0 \\end{bmatrix}")
        ket_1 = MathTex("\\vert 1 \\rangle = \\begin{bmatrix} 0 \\\ 1 \\end{bmatrix}")
        ket_0.shift(2*LEFT)
        ket_1.next_to(ket_0, RIGHT)
        ket_1.shift(1.5*RIGHT)

        #superposition
        superpostext  = Text("Superposition of states", font_size= 28)
        superposition = MathTex("\\vert \\Psi \\rangle &= c_1 \\vert 0 \\rangle + c_2 \\vert 1 \\rangle \\\ \
                        &= c_1 \\begin{bmatrix} 1\\\ 0 \\end{bmatrix} + c_2 \\begin{bmatrix} 0 \\\  1\\end{bmatrix} \\\ \
                        &= \\begin{bmatrix} c_1 \\\ c_2 \\end{bmatrix}")
        superpostext.next_to(qubits2, DOWN)
        superpostext.shift(0.8*UP)
        superposition.next_to(superpostext, DOWN)
        superposition.shift(0.25*DOWN)

        self.play(Write(qcomp), run_time= 1)
        self.wait(1)
        self.play(Write(qubits), Write(bitlabel), run_time = 1)
        self.play(FadeIn(psi_1), FadeIn(psi_2), FadeIn(bits))
        self.wait(3.75)
        
        self.play(qubits.animate.shift(5*RIGHT),psi_1.animate.shift(5*RIGHT), psi_2.animate.shift(5*RIGHT), FadeOut(bits), FadeOut(bitlabel), run_time = 2.5)

        self.play(FadeIn(blist1[0]))
        self.play(FadeIn(blist1[1]))
        self.play(FadeIn(blist1[2]))
        self.wait()
        self.play(Transform(blist1, speedup))
        self.wait()
        self.play(Transform(qubits,qubits2), Transform(psi_1, ket_0), Transform(psi_2, ket_1))
        self.wait(1.5)
        ket_0.shift(2.5*LEFT)
        self.play(psi_1.animate.shift(2.5*LEFT),psi_2.animate.next_to(ket_0, DOWN), FadeOut(qubits))
        self.play(FadeIn(superpostext), Write(superposition))
        self.wait(0.75)
        self.play(FadeOut(qcomp), FadeOut(blist1), FadeOut(superpostext), FadeOut(superposition),FadeOut(psi_1), FadeOut(psi_2), run_time = 0.75)
        self.wait(0.25) 

class vid3(MovingCameraScene):
    def construct(self):
        background = ImageMobject("slide.jpg")
        self.add(background)
        self.bring_to_back(background)

        nip = ImageMobject("niplogo2.png")
        nip.to_edge(DOWN + RIGHT)
        nip.shift(DOWN + 0.9*RIGHT)
        nip.scale(0.45)

        sand = ImageMobject("sandlogo.png")
        sand.next_to(nip,LEFT)
        sand.scale(1.65)
        
        self.add(nip,sand)

        headerfont = 33
        labelfont = 22

        self.wait(1)

        iterx = -0.5
        itery = -2
        modcheck = 0

        index= []

        for n1 in range(-1,2):
            circles1 = []
            circles2 = []
            for n2 in range(-5,3):
                modcheck = n2 + 5
                if modcheck%2 == 1:
                    circles1.append(Circle(radius=0.2, color=GRAY_A, fill_opacity = 1, arc_center=np.array([n2+ 1 + iterx,n1 + itery,0])))
                    circles2.append(Circle(radius=0.25, color=YELLOW_A, fill_opacity = 1, arc_center=np.array([n2+ 1.5 + iterx,n1+1 +itery,0])))
                else: 
                    circles1.append(Circle(radius=0.25, color=YELLOW_A, fill_opacity = 1, arc_center=np.array([n2+ 1 + iterx,n1 + itery,0])))
                    circles2.append(Circle(radius=0.2, color=GRAY_A, fill_opacity = 1, arc_center=np.array([n2+ 1.5 + iterx,n1+1 +itery,0])))
            circle_group1 = VGroup(*circles1)
            circle_group2 = VGroup(*circles2)
            if n1==0:
                cirqleft = circle_group2[5]
                cirqright = circle_group2[6]
            index.append(circle_group1)
            index.append(circle_group2)
            self.play(DrawBorderThenFill(circle_group1, run_time=0.4), DrawBorderThenFill(circle_group2, run_time=0.4))
            iterx += 1
            itery += 1
        
        self.wait(2.5)

        ogwidth = self.camera.frame_width
        ogheight = self.camera.frame_height

        self.play(
            self.camera.frame.animate.set(width = 5).move_to(circle_group1[5])
        )
        
        line1 = Line(circle_group1[5].get_edge_center(LEFT),circle_group1[4].get_edge_center(RIGHT), stroke_width = 1.2)
        line2 = Line(circle_group1[5].get_edge_center(RIGHT),circle_group1[6].get_edge_center(LEFT), stroke_width = 1.2)
        line3 = Line(circle_group1[5].get_center(),circle_group2[4].get_center(), stroke_width = 1.2)
        line4 = Line(circle_group1[5].get_center(),circle_group2[5].get_center(), stroke_width = 1.2)
        line5 = Line(circle_group1[5].get_center(),cirqleft.get_center(), stroke_width = 1.2)
        line6 = Line(circle_group1[5].get_center(),cirqright.get_center(), stroke_width = 1.2)

        line1.z_index = circle_group1.z_index -1
        line2.z_index = circle_group1.z_index -1
        line3.z_index = circle_group1.z_index -1
        line4.z_index = circle_group1.z_index -1
        line5.z_index = circle_group1.z_index -1
        line6.z_index = circle_group1.z_index -1
        
        background.z_index = line4.z_index - 2

        self.play(Create(line1),Create(line2),Create(line3),Create(line4), Create(line5), Create(line6), run_time = 1)

        func = lambda x : -x[1]*RIGHT - x[0]*UP
        field = ArrowVectorField(func, x_range = [-5,5,0.5], y_range = [-2.5,2.5,0.5])
        self.play(Create(field), run_time=1.5)

        field.z_index = -2

        self.wait(1)

        obj1 = Circle(radius = 0.2*2.5, color= GRAY_A, fill_opacity = 1) 
        obj1.shift(UP)
        obj2 = Circle(radius = 0.25*2.5, color= YELLOW_A, fill_opacity = 1)
        obj2.next_to(obj1, DOWN+ LEFT)
        obj3 = Circle(radius = 0.25*2.5, color= YELLOW_A, fill_opacity = 1) 
        obj3.next_to(obj1, DOWN+ RIGHT)
        obj2.shift(DOWN)
        obj3.shift(DOWN)    

        extras= []
        extras.append(circle_group2[0:5])
        extras.append(circle_group2[6:8])
        extras.append(circle_group1[0:5])
        extras.append(circle_group1[7])

        #print(obj1.z_index)
        #print(field.z_index)

        self.remove(line1,line2,line3,line4,line5,line6)

        self.play(
            self.camera.frame.animate.set(width=ogwidth, height = ogheight).move_to(Dot(np.array([0,0,0]))), Transform(circle_group1[5],obj1), Transform(circle_group1[6],obj2)
            , Transform(circle_group2[5], obj3), FadeOut(index[0],index[1],index[2], index[3]), FadeOut(extras[0],extras[1],extras[2],extras[3]),
        )
        self.wait()

        question = Text("What makes this configuration stable (low energy)?", font_size = headerfont)
        question.shift(3*UP)
        bg = SurroundingRectangle(question, corner_radius=0.2,fill_opacity = 1, fill_color = BLACK)
        group = Group(field,circle_group2[5],circle_group1[5],circle_group1[6])
        self.play(Create(bg),DrawBorderThenFill(question), run_time = 1)
        self.wait(0.5)

        func2 = lambda x : abs(x[1]*UP +5*UP) 
        field2 = ArrowVectorField(func2, x_range = [-5,5,0.5], y_range = [-2.5,1.75,0.5])
        
        self.play(FadeIn(field2), FadeOut(group), FadeOut(question, bg), run_time=0.75)
        self.wait(0.5)   

class vid4(Scene):
    def construct(self):
        background = ImageMobject("slide.jpg")
        self.add(background)
        self.bring_to_back(background)

        nip = ImageMobject("niplogo2.png")
        nip.to_edge(DOWN + RIGHT)
        nip.shift(DOWN + 0.9*RIGHT)
        nip.scale(0.45)

        sand = ImageMobject("sandlogo.png")
        sand.next_to(nip,LEFT)
        sand.scale(1.65)
        
        self.add(nip,sand)

        headerfont = 33
        labelfont = 22

        func2 = lambda x : abs(x[1]*UP +5*UP) 
        field2 = ArrowVectorField(func2, x_range = [-5,5,0.5], y_range = [-2.5,1.75,0.5])
        self.add(field2)

        #field.z_index = obj1.z_index - 2

        obj1 = Circle(radius = 0.2*2.5, color= GRAY_A, fill_opacity = 1) 
        obj1.shift(UP)
        obj2 = Circle(radius = 0.25*2.5, color= YELLOW_A, fill_opacity = 1)
        obj2.next_to(obj1, DOWN+ LEFT)
        obj3 = Circle(radius = 0.25*2.5, color= YELLOW_A, fill_opacity = 1) 
        obj3.next_to(obj1, DOWN+ RIGHT)   
        obj2.shift(DOWN)
        obj3.shift(DOWN)
        
        #self.play(Create(obj1),Create(obj2),Create(obj3))
        self.play(DrawBorderThenFill(obj1),DrawBorderThenFill(obj2),DrawBorderThenFill(obj3), run_time = 0.75)

        line1 = Line(obj1.get_center(),obj2.get_center(), stroke_width = 1.8)
        line2 = Line(obj2.get_center(),obj3.get_center(), stroke_width = 1.8)
        line3 = Line(obj3.get_center(),obj1.get_center(), stroke_width = 1.8)

        background.z_index = -3

        line1.z_index = obj1.z_index -1
        line2.z_index = obj1.z_index -1
        line3.z_index = obj1.z_index -1

        self.play(Create(line1), Create(line2), Create(line3), run_time = 0.75)

        obj1_h = Tex("$h$")
        obj12_j = Tex("$J_{1,2}$")
        obj2_h = Tex("$h$")
        obj23_j = Tex("$J_{2,3}$")
        obj3_h = Tex("$h$")
        obj31_j = Tex("$J_{1,3}$")

        obj1_h.next_to(obj1, UP)
        obj2_h.next_to(obj2, DOWN + LEFT)
        obj3_h.next_to(obj3, DOWN + RIGHT)
        obj2_h.shift(0.25*UP+0.25*RIGHT)
        obj3_h.shift(0.25*UP+0.25*LEFT)

        obj12_j.next_to(line1.get_center(), LEFT)
        obj23_j.next_to(line2.get_center(), DOWN)
        obj31_j.next_to(line3.get_center(), RIGHT)

        labelgroup = Group(obj1_h,obj12_j,obj2_h,obj23_j,obj3_h,obj31_j)
        objgroup = Group(obj1,obj2,obj3)
        linegroup = Group(line1,line2,line3)
        
        self.play(FadeIn(labelgroup), FadeOut(field2))        
        self.wait(2)

        spin1 = Arrow(obj1.get_top(), obj1.get_bottom(), color = RED_E, stroke_width= 6.2, max_stroke_width_to_length_ratio = 9,  max_tip_length_to_length_ratio=0.4)
        spin1copy = Arrow(obj1.get_top(), obj1.get_bottom(), color = RED_E, stroke_width= 6.2, max_stroke_width_to_length_ratio = 9,  max_tip_length_to_length_ratio=0.4)
        spin2 = Arrow(obj2.get_bottom(), obj2.get_top(), color = RED_E, stroke_width= 6.2, max_stroke_width_to_length_ratio = 9,  max_tip_length_to_length_ratio=0.4)
        spin3 = Arrow(obj3.get_bottom(), obj3.get_top(), color = RED_E, stroke_width= 6.2, max_stroke_width_to_length_ratio = 9,  max_tip_length_to_length_ratio=0.4)
        spin3copy = Arrow(obj3.get_bottom(), obj3.get_top(), color = RED_E, stroke_width= 6.2, max_stroke_width_to_length_ratio = 9,  max_tip_length_to_length_ratio=0.4)
        spin4 = Arrow(obj1.get_bottom(), obj1.get_top(), color = RED_E, stroke_width= 6.2, max_stroke_width_to_length_ratio = 9,  max_tip_length_to_length_ratio=0.4)
        spin5 = Arrow(obj3.get_top(), obj3.get_bottom(), color = RED_E, stroke_width= 6.2, max_stroke_width_to_length_ratio = 9,  max_tip_length_to_length_ratio=0.4)

        self.play(FadeIn(spin1,spin2,spin3))
        self.wait()
        self.play(spin1.animate.become(spin4), spin3.animate.become(spin5))
        self.play(spin1.animate.become(spin1copy), spin3.animate.become(spin3copy))
        self.wait()

        spingroup = Group(spin2,spin1copy,spin3copy)

        Hamiltonian = MathTex("H_{Ising} = -\\sum_{\\langle ij \\rangle} J_{ij}\\sigma^{z}_{i}\\sigma^{z}_{j} - \\sum_{i} h_{i}\\sigma^{x}_{i}")
        ising = Text("Ising Model", font_size = headerfont)
        ising.shift(2.3*UP+2.2*LEFT)
        Hamiltonian.next_to(ising, DOWN)
        Hamiltonian.shift(0.8*DOWN)
        text1 = Tex("$h$ = external magnetic field", font_size = 29)
        text2 = Tex("$J$ = coupling constant/coefficient", font_size = 29)
        text3 = MathTex("\\sigma &= -1 \\text{ if spin up } \\vert 0\\rangle \\\ &= 1 \\text{ if spin down } \\vert 1\\rangle", font_size = 29)
        
        dot1 = Tex("$\\cdot$").scale(2)
        dot2 = Tex("$\\cdot$").scale(2)
        dot3 = Tex("$\\cdot$").scale(2)

        vg = VGroup(text1,text2,text3)
        vgdots = VGroup(dot1,dot2,dot3)

        vg.arrange(DOWN, center=False, aligned_edge=LEFT) 
        vgdots.arrange(DOWN, center=False, aligned_edge=LEFT) 
        
        vg.next_to(Hamiltonian,DOWN)
        vg.shift(0.5*DOWN + LEFT)
        
        for n in range(3):
            vgdots[n].next_to(vg[n],LEFT)
        vgdots[2].shift(0.2*UP)

        self.remove(spin1, spin3)

        self.play(labelgroup.animate.shift(4*RIGHT).scale(0.7), objgroup.animate.shift(4*RIGHT).scale(0.7),
                spingroup.animate.shift(4*RIGHT).scale(0.7), linegroup.animate.shift(4*RIGHT).scale(0.7),
                Write(ising), Write(Hamiltonian), Write(vg), Write(vgdots), run_rime= 2
        )
        self.wait(3)

        ising2 = Text("Ising Model as a quantum circuit", font_size=headerfont)
        ising2.shift(2.3*UP)
        qiskit = ImageMobject("qiskitlogo.png")
        qiskit.next_to(Hamiltonian, DOWN)
        qiskit.shift(2.2*RIGHT+0.3*DOWN)
        qiskitcite = Text("M. S. Anis, Abby-Mitchell, and H. A. et al., “Qiskit: An open-source framework for quantum computing,” 2021.", font_size = 10)
        qiskitcite.next_to(vg[2],DOWN)
        qiskitcite.shift(0.7*DOWN+1.5*RIGHT)

        figgroup = Group(labelgroup,objgroup,spingroup,linegroup)

        self.play(ising.animate.become(ising2), Hamiltonian.animate.shift(2.2*RIGHT +0.5*UP), 
                figgroup.animate.shift(1.2*RIGHT).scale(0.7), FadeOut(vg,vgdots), run_time = 0.9)
        self.wait()

        arrow1 = Arrow(Hamiltonian.get_bottom(), qiskit.get_top())
        self.play(Create(arrow1) , FadeIn(qiskit), FadeIn(qiskitcite), run_time = 0.75)

        subfont = 19

        qcirc = Text("Quantum circuit creation", font_size=subfont)
        sim = Text("Simulation", font_size=subfont)
        ibmquantum = Text("IBM Quantum computers", font_size=subfont)

        qcirc.next_to(qiskit,LEFT)
        qcirc.shift(1.5*LEFT + 0.8*DOWN)
        sim.next_to(qiskit,DOWN)
        sim.shift(1.2*DOWN)
        ibmquantum.next_to(qiskit,RIGHT)
        ibmquantum.shift(1.5*RIGHT + 0.8*DOWN)

        arrow2 = Arrow(qiskit.get_bottom(), qcirc.get_right(), stroke_width= 2.8)
        arrow3 = Arrow(qiskit.get_bottom(), sim.get_top(), stroke_width= 2.8)
        arrow4 = Arrow(qiskit.get_bottom(), ibmquantum.get_left(), stroke_width= 2.8)

        self.play(AnimationGroup(Create(arrow2), Write(qcirc), Create(arrow3), Write(sim), Create(arrow4), Write(ibmquantum),  
                 lag_ratio= 0.1))

        self.wait(1.5)
        
        via = Text("via", font_size=headerfont)
        via.next_to(ising,RIGHT)
        via.shift(2*LEFT +0.05*UP)

        self.play(ising.animate.shift(2*LEFT), Write(via), qiskit.animate.next_to(via, RIGHT), 
                FadeOut(arrow2,arrow3,arrow4,qcirc,sim,ibmquantum)
        )
        uc= ImageMobject("samplecirc.png").scale(1.15)
        uc.shift(1.5*DOWN) 

        dot = Dot()
        dot.next_to(uc.get_center(), DOWN)
        dot.shift(UP)

        Hamiltoniancopy = MathTex("H_{Ising} = -\\sum_{\\langle ij \\rangle} J_{ij}\\sigma^{z}_{i}\\sigma^{z}_{j} - \\sum_{i} h_{i}\\sigma^{x}_{i}")
        Hamiltoniancopy.move_to(Hamiltonian.get_center())

        self.play(Hamiltonian.animate.become(Hamiltoniancopy), run_time = 0.1)
        self.play(Transform(Hamiltoniancopy,dot),FadeIn(uc), run_time = 0.5)
        self.wait(1.5)
        self.play(FadeOut(ising,via,qiskit, Hamiltonian, Hamiltoniancopy,dot,arrow1,qiskitcite,figgroup), 
        uc.animate.shift(3.5*LEFT + 2*UP).scale(0.75),
        run_time = 0.75)
        self.wait(0.25)

class vid4_2(Scene):
    def construct(self):
        background = ImageMobject("slide.jpg")
        self.add(background)
        self.bring_to_back(background)

        nip = ImageMobject("niplogo2.png")
        nip.to_edge(DOWN + RIGHT)
        nip.shift(DOWN + 0.9*RIGHT)
        nip.scale(0.45)

        sand = ImageMobject("sandlogo.png")
        sand.next_to(nip,LEFT)
        sand.scale(1.65)
        
        self.add(nip,sand)

        uc= ImageMobject("samplecirc.png").scale(1.15)
        uc.shift(1.5*DOWN)
        uc.shift(3.5*LEFT + 2*UP).scale(0.75)

        self.add(uc)

        schem = ImageMobject("schem.jpg")
        schem.shift(3*RIGHT)

        self.play(FadeIn(schem), run_time = 0.5)
        self.wait(3.5)
        self.play(FadeOut(uc,schem), run_time = 0.5)
        self.wait(0.25)