from cProfile import label
from ctypes import alignment
from doctest import run_docstring_examples
from telnetlib import DO
from tkinter import Image
from turtle import done, down, width
from typing_extensions import runtime
from cv2 import circle, line
from manim import *
from regex import D
from sklearn.covariance import LedoitWolf
from sklearn.preprocessing import scale
from manimlib import *
from manim.mobject.geometry.tips import ArrowTriangleFilledTip

class vid5(Scene):
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

        obj1 = Circle(radius = 0.2*2.5, color= GRAY_A, fill_opacity = 1) 
        obj1.shift(UP)
        obj2 = Circle(radius = 0.25*2.5, color= YELLOW_A, fill_opacity = 1)
        obj2.next_to(obj1, DOWN+ LEFT)
        obj3 = Circle(radius = 0.25*2.5, color= YELLOW_A, fill_opacity = 1) 
        obj3.next_to(obj1, DOWN+ RIGHT)   
        obj2.shift(DOWN)
        obj3.shift(DOWN)

        line1 = Line(obj1.get_center(),obj2.get_center(), stroke_width = 1.8)
        line2 = Line(obj2.get_center(),obj3.get_center(), stroke_width = 1.8)
        line3 = Line(obj3.get_center(),obj1.get_center(), stroke_width = 1.8)

        background.z_index = -3

        line1.z_index = obj1.z_index -1
        line2.z_index = obj1.z_index -1
        line3.z_index = obj1.z_index -1

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
        figgroup = Group(labelgroup,objgroup,linegroup)
        figgroup.move_to(Dot(np.array([0,0,0])))

        self.add(figgroup)
        self.wait()

        hval1 = Tex("$h = 0.01$")
        hval2 = Tex("$h = 0.01$")
        hval3 = Tex("$h = 0.01$")
        hval1.move_to(obj1_h.get_center())
        hval2.move_to(obj2_h.get_center())
        hval3.move_to(obj3_h.get_center())
        dot1 = Tex("$\\cdot$").scale(2)
        dot2 = Tex("$\\cdot$").scale(2)
        dot1.move_to(np.array([-6,2,0]))
        dot2.next_to(dot1, 3*DOWN)

        self.play(obj1_h.animate.become(hval1), obj2_h.animate.become(hval2), obj3_h.animate.become(hval3), run_time = 0.5)
        self.play(Create(dot1),obj1_h.animate.next_to(dot1,RIGHT),obj2_h.animate.next_to(dot1,RIGHT),
                    obj3_h.animate.next_to(dot1,RIGHT))

        j1copy = obj12_j.copy()
        j3copy = obj31_j.copy()
        self.add(j1copy,j3copy)

        J_1 = Tex("$J_1$")
        J_2 = Tex("$J_2$")
        J_3 = Tex("$J_3$")
        J_1.move_to(obj12_j.get_center())
        J_2.move_to(obj23_j.get_center())
        J_3.move_to(obj31_j.get_center())
        J_1copy = J_1.copy()
        J_3copy = J_3.copy()

        equals = Tex("$=$")
        equals.next_to(dot2,5*RIGHT)

        self.play(Create(dot2),Write(equals), run_time = 0.3)
        self.play(j1copy.animate.next_to(equals,LEFT), j3copy.animate.next_to(equals,RIGHT))
        self.wait(0.7)

        J_1copy.move_to(j1copy.get_center())
        J_3copy.move_to(j3copy.get_center())

        self.play(j1copy.animate.become(J_1copy), obj12_j.animate.become(J_1), j3copy.animate.become(J_3copy), 
                obj31_j.animate.become(J_3), obj23_j.animate.become(J_2))

        self.wait(1)

        obj1.z_index = line1.z_index +1
        obj2.z_index = line1.z_index +1
        obj3.z_index = line1.z_index +1

        stable = Text("Configurations:", font_size = headerfont)
        stable.next_to(dot1, RIGHT)
        stable.shift(8*RIGHT+ UP)
        label1 = Text("State", font_size = labelfont)
        #label2 = Text("Energy", font_size = labelfont)
        label1.next_to(stable,DOWN)
        #label1.shift(0.5*LEFT)
        #label2.next_to(label1,RIGHT)

        states = VGroup()
        list = ['000', '100', '010', '110', '001', '101', '011', '111']
        for n in range(8):
            state = MathTex("\\vert" + list[n] +"\\rangle")
            states.add(state)

        states.arrange(DOWN, center = False, aligned_edge = LEFT, buff=0.1)
        states.next_to(label1,DOWN)
        self.play(Write(stable),Write(label1),Write(states), run_time = 1)
        
class vid6(Scene):
    def construct(self):
        background = ImageMobject("slide.jpg")
        self.add(background)
        self.bring_to_back(background)
        background.z_index = -4

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

        obj1 = Circle(radius = 0.2*2.5, color= GRAY_A, fill_opacity = 1) 
        obj1.shift(UP)
        obj2 = Circle(radius = 0.25*2.5, color= YELLOW_A, fill_opacity = 1)
        obj2.next_to(obj1, DOWN+ LEFT)
        obj3 = Circle(radius = 0.25*2.5, color= YELLOW_A, fill_opacity = 1) 
        obj3.next_to(obj1, DOWN+ RIGHT)   
        obj2.shift(DOWN)
        obj3.shift(DOWN)

        line1 = Line(obj1.get_center(),obj2.get_center(), stroke_width = 1.8)
        line2 = Line(obj2.get_center(),obj3.get_center(), stroke_width = 1.8)
        line3 = Line(obj3.get_center(),obj1.get_center(), stroke_width = 1.8)
        line1.z_index = obj1.z_index -1
        line2.z_index = obj1.z_index -1
        line3.z_index = obj1.z_index -1

        J_1 = Tex("$J_1$")
        J_2 = Tex("$J_2$")
        J_3 = Tex("$J_3$")
        J_1.next_to(line1.get_center(), LEFT)
        J_2.next_to(line2.get_center(), DOWN)
        J_3.next_to(line3.get_center(), RIGHT)
        hval1 = Tex("$h = 0.01$")
        J_1copy = J_1.copy()
        J_3copy = J_3.copy()
        equals = Tex("=")

        dot1 = Tex("$\\cdot$").scale(2)
        dot2 = Tex("$\\cdot$").scale(2)
        dot1.move_to(np.array([-6,2,0]))
        dot2.next_to(dot1, 3*DOWN)

        hval1.next_to(dot1, RIGHT)
        equals.next_to(dot2,5*RIGHT)
        J_1copy.next_to(equals,LEFT)
        J_1copy.shift(0.2*LEFT)
        equals.next_to(J_1copy,RIGHT)
        J_3copy.next_to(equals,RIGHT)
    
        figgroup = Group(obj1,obj2,obj3,J_1,J_2,J_3,line1,line2,line3)

        stable = Text("Configurations:", font_size = headerfont)
        stable.next_to(dot1, RIGHT)
        stable.shift(8*RIGHT+ UP)
        label1 = Text("State", font_size = labelfont)
        #label2 = Text("Energy", font_size = labelfont)
        label1.next_to(stable,DOWN)
        #label1.shift(0.5*LEFT)
        #label2.next_to(label1,RIGHT)

        states = VGroup()
        list = ['000', '100', '010', '110', '001', '101', '011', '111']
        for n in range(8):
            state = MathTex("\\vert" + list[n] +"\\rangle")
            states.add(state)

        states.arrange(DOWN, center = False, aligned_edge = LEFT, buff=0.1)
        states.next_to(label1,DOWN)

        self.add(stable,label1,states,figgroup,dot1,dot2,hval1,J_1copy,equals,J_3copy)

        spin1 = Line(obj1.get_bottom(), obj1.get_top(), color = RED_E, stroke_width= 3.2).add_tip(tip_shape = ArrowTriangleFilledTip)
        spin2 = Line(obj2.get_bottom(), obj2.get_top(), color = RED_E, stroke_width= 3.2).add_tip(tip_shape = ArrowTriangleFilledTip)
        spin3 = Line(obj3.get_bottom(), obj3.get_top(), color = RED_E, stroke_width= 3.2).add_tip(tip_shape = ArrowTriangleFilledTip)
        spin1down = Line(obj1.get_top(), obj1.get_bottom(), color = RED_E, stroke_width= 3.2).add_tip(tip_shape = ArrowTriangleFilledTip)
        spin2down = Line(obj2.get_top(), obj2.get_bottom(), color = RED_E, stroke_width= 3.2).add_tip(tip_shape = ArrowTriangleFilledTip)
        spin3down = Line(obj3.get_top(), obj3.get_bottom(), color = RED_E, stroke_width= 3.2).add_tip(tip_shape = ArrowTriangleFilledTip)

        upspins = VGroup(spin1,spin2,spin3)
        downspins = VGroup(spin1down,spin2down,spin3down)

        alpha1 = MathTex("\\alpha_1 = \\frac{J_2}{J_1}")
        alpha3 = MathTex("\\alpha_3 = \\frac{J_1}{J_3} = 1")
        alpha1.next_to(J_1copy,DOWN)
        alpha1.shift(DOWN)
        alpha3.next_to(alpha1,DOWN)
        alpha3.shift(0.5*RIGHT)
        J_1copy2 = J_1.copy()
        J_1copy3 = J_1.copy()
        J_2copy2 = J_2.copy()
        J_3copy2 = J_3.copy()

        alpha1pair = Group(J_1copy2,J_2copy2)
        alpha3pair = Group(J_1copy3,J_3copy2)

        index = []
        for n in range(8):
            listx = ['000', '001', '010', '011', '100', '101', '110', '111']
            s = []
            currentstate = listx[n]
            upcopy = upspins.copy()
            downcopy = downspins.copy()
            for spincount in range(3):
                if currentstate[spincount] == '0':
                    s.append(upcopy[spincount])
                else:
                    s.append(downcopy[spincount])
            self.play(FadeIn(s[0],s[1],s[2]), run_time = 0.4)
            self.wait(0.2)
            self.play(s[0].animate.next_to(states[n],2.5*RIGHT).scale(0.55), s[1].animate.next_to(states[n],1.75*RIGHT).scale(0.45), 
                    s[2].animate.next_to(states[n],RIGHT).scale(0.45), run_time = 0.4)
            index.append(s)
            if n == 2:
                self.play(Transform(alpha1pair,alpha1), run_time = 0.4)
            if n == 4:
                self.play(Transform(alpha3pair,alpha3), run_time = 0.4)

        indexs = VGroup()
        for n1 in range(len(index)):
            for n2 in range(3):
                indexs.add(index[n1][n2])

        dot1new = Dot(np.array([-6,2,0]))
        dot2new = Dot().next_to(dot1new,RIGHT)

        self.wait(0.5)
        self.play(FadeOut(stable,states,dot1,dot2,J_1copy,equals,J_3copy,hval1,alpha3pair,label1),
        FadeOut(indexs), alpha1pair.animate.next_to(dot2new,RIGHT), figgroup.animate.shift(4.5*RIGHT+0.5*UP).scale(0.8)
        )

class vid7(Scene):
    def construct(self):
        background = ImageMobject("slide.jpg")
        self.add(background)
        self.bring_to_back(background)
        background.z_index = -4

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

        obj1 = Circle(radius = 0.2*2.5, color= GRAY_A, fill_opacity = 1) 
        obj1.shift(UP)
        obj2 = Circle(radius = 0.25*2.5, color= YELLOW_A, fill_opacity = 1)
        obj2.next_to(obj1, DOWN+ LEFT)
        obj3 = Circle(radius = 0.25*2.5, color= YELLOW_A, fill_opacity = 1) 
        obj3.next_to(obj1, DOWN+ RIGHT)   
        obj2.shift(DOWN)
        obj3.shift(DOWN)

        line1 = Line(obj1.get_center(),obj2.get_center(), stroke_width = 1.8)
        line2 = Line(obj2.get_center(),obj3.get_center(), stroke_width = 1.8)
        line3 = Line(obj3.get_center(),obj1.get_center(), stroke_width = 1.8)
        line1.z_index = obj1.z_index -1
        line2.z_index = obj1.z_index -1
        line3.z_index = obj1.z_index -1

        J_1 = Tex("$J_1$")
        J_2 = Tex("$J_2$")
        J_3 = Tex("$J_3$")
        J_1.next_to(line1.get_center(), LEFT)
        J_2.next_to(line2.get_center(), DOWN)
        J_3.next_to(line3.get_center(), RIGHT)

        figgroup = Group(J_1,J_2,J_3,obj1,obj2,obj3,line1,line2,line3)

        alpha1 = MathTex("\\alpha_1 = \\frac{J_2}{J_1} =")
        dot1 = Dot(np.array([-6,2,0]))
        dot2 = Dot().next_to(dot1,RIGHT)
        alpha1.next_to(dot2, RIGHT)

        track = ValueTracker(-1.5)

        alpha1val = DecimalNumber(track.get_value(), num_decimal_places=1)
        alpha1val.next_to(alpha1,RIGHT)
        figgroup.shift(4.5*RIGHT+0.5*UP).scale(0.8)

        qub1 = Text("Qubit 1", font_size = 17)
        qub2 = Text("Qubit 2", font_size = 17) 
        qub3 = Text("Qubit 3", font_size = 17)
        qub1.next_to(obj1, UP)
        qub2.next_to(obj2, DOWN + LEFT)
        qub3.next_to(obj3, DOWN + RIGHT)
        qub2.shift(0.1*UP+1.22*RIGHT)
        qub3.shift(0.1*UP+1.22*LEFT)

        self.add(alpha1,figgroup)

        l1 = NumberLine(
            x_range=[-1.5, 1.5, 0.5],
            unit_size=2.5,
            #numbers_with_elongated_ticks=[-2, 4],
            include_numbers=True,
            font_size=23,
        )
        l1.next_to(alpha1, DOWN)
        l1.shift(2*RIGHT)
        self.play(Create(l1), run_time = 0.75)

        blist = BulletedList("Magnetic Frustration: ","Relative minima: ","Absolute minimum: ", font_size = 35)
        blist.shift(4.75*LEFT + 1.5*DOWN)
        J_1val = Tex("$1.0$", font_size = 30)
        J_3val = Tex("$1.0$", font_size = 30)
        J_1val.move_to(J_1.get_center())
        J_3val.move_to(J_3.get_center())
        
        t_marker = Dot(color=YELLOW).add_updater(
            lambda mob: mob.move_to(l1.number_to_point(track.get_value())),
        ).update()

        alpha1val.add_updater(
            lambda mob: mob.set_value(track.get_value())
        )
        self.play(Write(alpha1val), Create(t_marker), DrawBorderThenFill(blist), J_1.animate.become(J_1val), 
                J_3.animate.become(J_3val),FadeIn(qub1,qub2,qub3),  run_time = 0.5)
        """
        def vibrate(obj1,obj2,obj3,iters):
            for n in range(iters):
                shake = (iters/20)
                if n %2 == 0:
                    self.play(
                    obj1.animate.shift(0.1*shake*RIGHT),
                    obj2.animate.shift(0.1*shake*RIGHT),
                    obj3.animate.shift(0.1*shake*RIGHT), run_time = 1/(4*iters)
                    )
                    self.play(
                    obj1.animate.shift(0.1*shake*LEFT),
                    obj2.animate.shift(0.1*shake*LEFT),
                    obj3.animate.shift(0.1*shake*LEFT), run_time = 1/(4*iters)
                    )
                if n %2 == 1:
                    self.play(
                    obj1.animate.shift(0.1*shake*LEFT),
                    obj2.animate.shift(0.1*shake*LEFT),
                    obj3.animate.shift(0.1*shake*LEFT), run_time = 1/(4*iters)
                    )
                    self.play(
                    obj1.animate.shift(0.1*shake*RIGHT),
                    obj2.animate.shift(0.1*shake*RIGHT),
                    obj3.animate.shift(0.1*shake*RIGHT), run_time = 1/(4*iters)
                    )
        """
        alphavals = [-1.5,-1.3,-1.1,-1,-0.9,-0.7,-0.5,-0.3,0.3,0.5,0.7,0.9,1,1.1,1.3,1.5]

        dotf = Dot().next_to(blist[0],RIGHT)
        dotr = Dot().next_to(blist[1],RIGHT)
        dota = Dot().next_to(blist[2],RIGHT)
        comma1 = Text(",").scale(0.3)
        comma1.next_to(dotf,RIGHT)
        comma1.shift(0.1*DOWN)
        comma2 = Text(",").scale(0.3)
        comma2.next_to(dotr,RIGHT)
        comma2.shift(0.1*DOWN)
        comma3 = Text(",").scale(0.3)
        comma3.next_to(dota,RIGHT)
        comma3.shift(0.1*DOWN)
        index = []
        commaindex = []

        symmetry = Tex("Symmetry: $J_2 = \\frac{n}{2}J_1$ or $\\alpha_1 = \\frac{n}{2}\\alpha_3$ \\quad(n = 1,2,3...)", font_size = 35)
        symmetry.next_to(blist[2],DOWN)
        symmetry.shift(0.3*DOWN + 3.5*RIGHT)

        for n in range(len(alphavals)):
            self.play(track.animate.set_value(alphavals[n]), run_time = 0.75)
            alphacopy = DecimalNumber(track.get_value(), num_decimal_places=1).scale(0.6)
            J2copy = DecimalNumber(track.get_value(), num_decimal_places=1).scale(0.8)
            J2copy.move_to(J_2.get_center())
            alphacopy.move_to(alpha1val.get_center())
            a = alphavals[n]
            #Frustration
            if a == -1.5 or a ==-1.3 or a ==-1.1 or a ==-0.3 or a ==0.3 or a ==0.7 or a ==0.9 or a ==1.1 or a ==1.3:
                #vibrate(obj1,obj2,obj3,10)
                if a == -1.5:
                    self.play(alphacopy.animate.move_to(dotf.get_center()), J_2.animate.become(J2copy),run_time= 0.25)
                else:        
                    comma1copy = comma1.copy()
                    self.play(alphacopy.animate.move_to(dotf.get_center()),Create(comma1copy), J_2.animate.become(J2copy),run_time= 0.25)
                    commaindex.append(comma1copy)
                comma1.next_to(dotf,RIGHT)
                comma1.shift(0.1*DOWN)
                dotf.next_to(alphacopy,RIGHT)
                dotf.shift(0.1*RIGHT)
                if a == -0.3:
                    dotf.shift(0.1*LEFT)
                if a == 0.3 or a ==0.7 or a ==0.9 or a ==1.1 or a ==1.3:
                    dotf.shift(0.1*LEFT)
                    comma1.shift(0.1*LEFT)
            #Relmin
            if a == -0.9 or a == -0.7:
                #vibrate(obj1,obj2,obj3,5)
                if a == -0.9:
                    self.play(alphacopy.animate.move_to(dotr.get_center()), J_2.animate.become(J2copy),run_time= 0.25)
                else:        
                    comma2copy = comma2.copy()
                    self.play(alphacopy.animate.move_to(dotr.get_center()),Create(comma2copy), J_2.animate.become(J2copy),run_time= 0.25)
                    commaindex.append(comma2copy)
                comma2.next_to(dotr,RIGHT)
                comma2.shift(0.1*DOWN)
                dotr.next_to(alphacopy,RIGHT)
                dotr.shift(0.1*RIGHT)
            #Absmin
            if a == -1 or a == -0.5 or a == 0.5 or a == 1.5:
                if a == -1:
                    self.play(alphacopy.animate.move_to(dota.get_center()), J_2.animate.become(J2copy),run_time= 0.25)
                else:        
                    comma3copy = comma3.copy()
                    self.play(alphacopy.animate.move_to(dota.get_center()),Create(comma3copy), J_2.animate.become(J2copy),run_time= 0.25)
                    commaindex.append(comma3copy)
                comma3.next_to(dota,RIGHT)
                comma3.shift(0.1*DOWN)
                dota.next_to(alphacopy,RIGHT)
                dota.shift(0.1*RIGHT)
                if a == -0.5:
                    dota.shift(0.1*LEFT)
                if a == 0.5:
                    self.play(DrawBorderThenFill(symmetry), run_time = 0.5)
                    dota.shift(0.1*LEFT)
                    comma3.shift(0.1*LEFT)
                if a == 1.5:
                    dota.shift(0.1*LEFT)
                    comma3.shift(0.1*LEFT)
            index.append(alphacopy)
        
        indexs = VGroup()
        commaindexs = VGroup()
        for n1 in range(len(index)):
            indexs.add(index[n1])
        for n1 in range(len(commaindex)):
            commaindexs.add(commaindex[n1])

        self.wait(0.5)
        self.play(FadeOut(blist,qub1,qub2,qub3,figgroup,alpha1val,alpha1,l1,J_1val,J_3val,J2copy,t_marker,indexs,commaindexs,symmetry), run_time = 0.75)
        self.wait(0.25)

class vid8(Scene):
    def construct(self):
        background = ImageMobject("slide.jpg")
        self.add(background)
        self.bring_to_back(background)
        background.z_index = -4

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

        qcomp_trials = Text("Quantum computer trials: 'ibmq_lima'", font_size = headerfont)
        qcomp_trials.shift(2.3*UP+1.5*LEFT)

        trial1 = ImageMobject("grey-1.1.png")
        trial2 = ImageMobject("grey1.5.png")
        trial1.shift(3.1*LEFT + 0.5*DOWN)
        trial2.shift(3.1*RIGHT+ 0.5*DOWN)
        label1 = Tex("$\\alpha_1 = -1.1$")
        label2 = Tex("$\\alpha_1 = 1.5$")
        label1.next_to(trial1,DOWN)
        label2.next_to(trial2,DOWN)
        self.play(DrawBorderThenFill(qcomp_trials), run_time = 1)
        self.play(AnimationGroup(FadeIn(trial1,trial2,label1,label2), lag_ratio = 0.1), run_time  = 1)
        self.wait(2.5)
        self.play(FadeOut(qcomp_trials,label1,label2,trial1,trial2))

        title = Text("Other material lattice coupling coefficient studies:", font_size= 29)
        title.move_to(qcomp_trials.get_center())
        title.shift(RIGHT)
        boro = ImageMobject("boro.JPG").scale(0.9)
        livo = ImageMobject("livopo4.JPG").scale(0.79)
        boro.move_to(trial1.get_center())
        livo.move_to(trial2.get_center())
        boro.shift(0.2*LEFT)
        livo.shift(0.35*RIGHT)

        citeboro = VGroup()
        cite1 = Text("K. Shi, W. Jiang, A. Guo, K. Wang, and C. Wu, “Magnetic and thermodynamic properties of ising model with borophene structure", font_size = 9)
        cite1_1 = Text("in a longitudinal magnetic field,” Physica A: Statistical Mechanics and its Applications, vol. 500, pp. 11-22, 2018.", font_size = 9)
        cite2 = Text("P. K. Mukharjee, K. M. Ranjith, M. Baenitz, Y. Skourski, A. A. Tsirlin, and R. Nath, “Two types of alternating spin- 1",font_size = 9)
        cite2_2 = Text("2 chains and their field-induced transitions in ε-LiVOPO4,” Phys.Rev. B, vol. 101, p. 224403, Jun 2020.", font_size = 9)
        
        citeboro.add(cite1)
        citeboro.add(cite1_1)
        citeboro.add(cite2)
        citeboro.add(cite2_2)
        citeboro.arrange(DOWN, center = False, aligned_edge = LEFT, buff = 0.05)

        citeboro.next_to(boro,DOWN)
        citeboro.shift(0.25*DOWN+2*RIGHT)

        self.play(DrawBorderThenFill(title), run_time = 0.5)
        self.play(FadeIn(boro,livo), FadeIn(citeboro))
        self.wait(2.75)
        self.play(FadeOut(title,boro,livo,citeboro))