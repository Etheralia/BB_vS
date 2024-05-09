from manim import *



black_color = "#212123"
x_color = BLUE
y_color = "#33cc33"
z_color = GREEN
u_color = YELLOW
t_color = "#ccccc33"
f_color = "#33cccc"
arrow_color = "#666FFF"
s_color = PINK
v_color = PINK
P_color = BLUE
n_color = GREEN
R_color = YELLOW
x1_color = BLUE
x2_color = RED
x3_color = GREEN
class Intro(Scene):
    def construct(self):
        self.camera.background_color = black_color
        formulaz_x_y = MathTex(r"z=f(x,y)").scale(2)
        formulaz_x_y[0][0].set_color(z_color)
        formulaz_x_y[0][2].set_color(f_color)
        formulaz_x_y[0][4].set_color(x_color)
        formulaz_x_y[0][6].set_color(y_color)
        self.play(Write(formulaz_x_y))
        self.wait()
        formulaz = MathTex(r"z").scale(2).to_edge(UP+LEFT,buff = 1).set_color(z_color)
        formulax = MathTex(r"x").scale(2).next_to(formulaz,UP+5*RIGHT).set_color(x_color)
        formulay = MathTex(r"y").scale(2).next_to(formulaz,DOWN+5*RIGHT).set_color(y_color)
        formulat = MathTex(r"t").scale(2).next_to(formulaz,12*RIGHT).set_color(t_color)
        formulas = MathTex(r"s").scale(2).move_to([formulat.get_center()[0],formulax.get_center()[1],0]).set_color(t_color)
        
        formulaz_p_x = MathTex(r"\frac{\partial z}{\partial x}").scale(2).shift(2*LEFT)
        formulaz_p_y = MathTex(r"\frac{\partial z}{\partial y}").scale(2).shift(2*RIGHT)
        formulaz_p_x[0][1].set_color(z_color)
        formulaz_p_x[0][4].set_color(x_color)
        formulaz_p_y[0][1].set_color(z_color)
        formulaz_p_y[0][4].set_color(y_color)
        
        formulaz_d_t_xy = MathTex(
            r"\frac{d z}{d t}", "=",  
            r"\frac{\partial z}{\partial x}",  
            r"\frac{d x}{d t}",  
            "+",  
            r"\frac{\partial z}{\partial y}",  
            r"\frac{d y}{d t}").scale(2)
        formulaz_d_t_xy[0][1].set_color(z_color)
        formulaz_d_t_xy[2][1].set_color(z_color)
        formulaz_d_t_xy[5][1].set_color(z_color)
        formulaz_d_t_xy[0][4].set_color(t_color)
        formulaz_d_t_xy[3][4].set_color(t_color)
        formulaz_d_t_xy[6][4].set_color(t_color)
        formulaz_d_t_xy[2][4].set_color(x_color)
        formulaz_d_t_xy[3][1].set_color(x_color)
        formulaz_d_t_xy[5][4].set_color(y_color)
        formulaz_d_t_xy[6][1].set_color(y_color)
        
        
        formulau_d_t_xy = MathTex(r"\frac{d u}{d t}","=",r"\frac{\partial u}{\partial t}","+",r"\frac{\partial u}{\partial x} ",r"\frac{d x}{d t}","+",r"\frac{\partial u}{\partial y}" ,r"\frac{d y}{d t}").scale(2)
        formulau_d_t_xy[0][1].set_color(u_color)
        formulau_d_t_xy[2][1].set_color(u_color)
        formulau_d_t_xy[4][1].set_color(u_color)
        formulau_d_t_xy[7][1].set_color(u_color)
        formulau_d_t_xy[0][4].set_color(t_color)
        formulau_d_t_xy[2][4].set_color(t_color)
        formulau_d_t_xy[5][4].set_color(t_color)
        formulau_d_t_xy[8][4].set_color(t_color)
        formulau_d_t_xy[4][4].set_color(x_color)
        formulau_d_t_xy[5][1].set_color(x_color)
        formulau_d_t_xy[7][4].set_color(y_color)
        formulau_d_t_xy[8][1].set_color(y_color)
        
        formulaz_d_t_xy_alld = MathTex(
            r"\frac{\partial z}{\partial t}", "=",  
            r"\frac{\partial z}{\partial x}",  
            r"\frac{\partial x}{\partial t}",  
            "+",  
            r"\frac{\partial z}{\partial y}",  
            r"\frac{\partial y}{\partial t}").scale(2)
        formulaz_d_t_xy_alld[0][1].set_color(z_color)
        formulaz_d_t_xy_alld[2][1].set_color(z_color)
        formulaz_d_t_xy_alld[5][1].set_color(z_color)
        formulaz_d_t_xy_alld[0][4].set_color(t_color)
        formulaz_d_t_xy_alld[3][4].set_color(t_color)
        formulaz_d_t_xy_alld[6][4].set_color(t_color)
        formulaz_d_t_xy_alld[2][4].set_color(x_color)
        formulaz_d_t_xy_alld[3][1].set_color(x_color)
        formulaz_d_t_xy_alld[5][4].set_color(y_color)
        formulaz_d_t_xy_alld[6][1].set_color(y_color)
        
                                    
        VG_z_x_y = VGroup(formulaz,formulax,formulay)
        a_z_x = Arrow(formulaz.get_right(),formulax.get_left(),buff=0.1).set_color(arrow_color)
        a_z_y = Arrow(formulaz.get_right(),formulay.get_left(),buff=0.1).set_color(arrow_color)
        a_x_t = always_redraw(lambda:Arrow(formulax.get_right(),formulat.get_left(),buff=0.1).set_color(arrow_color))
        a_y_t = always_redraw(lambda:Arrow(formulay.get_right(),formulat.get_left(),buff=0.1).set_color(arrow_color))
        a_x_s = always_redraw(lambda:Arrow(formulax.get_right(),formulas.get_left(),buff=0.1).set_color(arrow_color))
        a_y_s = always_redraw(lambda:Arrow(formulay.get_right(),formulas.get_left(),buff=0.1).set_color(arrow_color))
        
        
        
        self.play(Transform(formulaz_x_y,VG_z_x_y))
        self.play(Create(a_z_x),Create(a_z_y))
        self.wait()
        self.play(Write(formulaz_p_x),Write(formulaz_p_y))
        self.wait()
        self.play(Create(a_x_t),Create(a_y_t),Write(formulat))
        self.wait()
        self.play(AnimationGroup(formulaz_p_x.animate.move_to(formulaz_d_t_xy[2].get_center()),
                                 FadeIn(formulaz_d_t_xy),
                                 lag_ratio=0.5
                                 ),
                  formulaz_p_y.animate.move_to(formulaz_d_t_xy[5].get_center()))
        self.remove(formulaz_p_y,formulaz_p_x)
        self.wait()
        self.play(Wiggle(a_x_t),Wiggle(a_y_t))
        self.wait()
        for _ in range(2):
            self.play(Wiggle(a_x_t),Wiggle(a_y_t),Wiggle(a_z_x),Wiggle(a_z_y))
        self.wait()
        self.play(formulat.animate.move_to([formulat.get_center()[0],formulay.get_center()[1],0]),
                  Create(a_y_s),
                  Create(a_x_s),
                  Write(formulas)
                  )
        self.wait()
        self.play(TransformMatchingShapes(formulaz_d_t_xy[0],formulaz_d_t_xy_alld[0]),
                    TransformMatchingShapes(formulaz_d_t_xy[3],formulaz_d_t_xy_alld[3]),
                  TransformMatchingShapes(formulaz_d_t_xy[6],formulaz_d_t_xy_alld[6]))
        self.wait()
        
        group_a_zxyt = VGroup(a_z_x,a_z_y,a_x_t,a_y_t).copy().set_color(RED)
        group_a_zxyt.save_state()
        self.play(FadeIn(group_a_zxyt))
        self.play(Wiggle(group_a_zxyt))
        self.wait() 
        self.play(Wiggle(formulax),Wiggle(formulay))
        self.wait() 
        self.play(Wiggle(formulas),Wiggle(formulat))
        self.wait()
        self.play(FadeOut(group_a_zxyt))
        self.wait()
        
class StaticSurfacePlot3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.camera.background_color = black_color
        # 定义曲面的函数
        def surface_func(x, y):
            return np.sin(x-2) * np.cos(y)
        def surface_func1(x, y):
            return 2*np.sin(x) * np.cos(y)

        # 创建曲面
        surface = Surface(
            lambda u, v: [u, v, surface_func(u, v)],
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(50, 50)  # 曲面分辨率
        ).scale(1.5)

        # 给曲面上色，根据高度变化颜色
        surface.set_style(fill_opacity=1)
        surface.set_fill_by_value(axes=axes, colorscale=[(GREEN, -0.5), (YELLOW, 0), (RED, 0.5)], axis=2)

        # 添加箭头
        arrow1 = Arrow3D(start=[-0.2, 0, 0], end=[0, -2, 0.1], color=RED)
        arrow2 = Arrow3D(start=[-0.2, 0, 0], end=[1, 0 , 2], color=BLUE)

        surface1 = Surface(
            lambda u, v: [u, v, surface_func1(u, v)],
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(50, 50)  # 曲面分辨率
        ).scale(1.5)

        # 给曲面上色，根据高度变化颜色
        surface1.set_style(fill_opacity=1)
        surface1.set_fill_by_value(axes=axes, colorscale=[(GREEN, -1), (YELLOW, 0), (RED, 0.8)], axis=2)
        # 设置初始视角
        self.set_camera_orientation(phi=60 * DEGREES, theta=215 * DEGREES)

        # 添加对象到场景
        self.add(surface)
        self.wait()
        self.play(Transform(surface,surface1))
        self.play(Create(arrow1))
        self.play(Create(arrow2))
        # 移除摄像机动画
        self.wait()

class  Partial_u_xyt(Scene):
    def construct(self):
        self.camera.background_color = black_color
        formulau = MathTex(r"u").scale(2).to_edge(LEFT,buff = 0.5).shift(2*UP).set_color(u_color)
        formulaz = MathTex(r"z").scale(2).next_to(formulau,4*DOWN+7*RIGHT).set_color(z_color)
        formulax = MathTex(r"x").scale(2).next_to(formulau,4*UP+7*RIGHT).set_color(x_color)
        formulay = MathTex(r"y").scale(2).next_to(formulau,0.1*UP+7*RIGHT).set_color(y_color)
        formulat = MathTex(r"t").scale(2).next_to(formulau,0.1*DOWN+14*RIGHT).set_color(t_color)
        formulas = MathTex(r"s").scale(2).move_to([formulat.get_center()[0],formulax.get_center()[1],0]).set_color(t_color)
        
        a_z_x = Arrow(formulaz.get_right(),formulax.get_left(),buff=0.1).set_color(arrow_color)
        a_z_y = Arrow(formulaz.get_right(),formulay.get_left(),buff=0.1).set_color(arrow_color)
        a_x_t = always_redraw(lambda:Arrow(formulax.get_right(),formulat.get_left(),buff=0.1).set_color(arrow_color))
        a_y_t = always_redraw(lambda:Arrow(formulay.get_right(),formulat.get_left(),buff=0.1).set_color(arrow_color))
        a_x_s = always_redraw(lambda:Arrow(formulax.get_right(),formulas.get_left(),buff=0.1).set_color(arrow_color))
        a_y_s = always_redraw(lambda:Arrow(formulay.get_right(),formulas.get_left(),buff=0.1).set_color(arrow_color))
        a_u_x = always_redraw(lambda:Arrow(formulau.get_right(),formulax.get_left(),buff=0.1).set_color(arrow_color))
        a_u_y = always_redraw(lambda:Arrow(formulau.get_right(),formulay.get_left(),buff=0.1).set_color(arrow_color))
        a_u_t = Arrow(formulau.get_right(),formulat.get_left(),buff=0.1).set_color(arrow_color)
        a_u_z = always_redraw(lambda:Arrow(formulau.get_right(),formulaz.get_left(),buff=0.1).set_color(arrow_color))
        
        formulau_d_t_xy = MathTex(r"\frac{d u}{d t}","=",r"\frac{\partial u}{\partial t}","+",r"\frac{\partial u}{\partial x} ",r"\frac{d x}{d t}","+",r"\frac{\partial u}{\partial y}" ,r"\frac{d y}{d t}").scale(1.4)
        formulau_d_t_xy.to_edge(UP+RIGHT,buff=0.5).shift(0.5*LEFT)
        formulau_d_t_xy[0][1].set_color(u_color)
        formulau_d_t_xy[2][1].set_color(u_color)
        formulau_d_t_xy[4][1].set_color(u_color)
        formulau_d_t_xy[7][1].set_color(u_color)
        formulau_d_t_xy[0][4].set_color(t_color)
        formulau_d_t_xy[2][4].set_color(t_color)
        formulau_d_t_xy[5][4].set_color(t_color)
        formulau_d_t_xy[8][4].set_color(t_color)
        formulau_d_t_xy[4][4].set_color(x_color)
        formulau_d_t_xy[5][1].set_color(x_color)
        formulau_d_t_xy[7][4].set_color(y_color)
        formulau_d_t_xy[8][1].set_color(y_color)
        
        nabla_x_y_u = MathTex(r"\left(\nabla_{x, y} u\right) \cdot \mathbf{v}").scale(1.4).move_to(formulau_d_t_xy[6].copy().shift(2*DOWN+0.5*RIGHT).get_center())
        nabla_x_y_u[0][2].set_color(x_color)
        nabla_x_y_u[0][4].set_color(y_color)
        nabla_x_y_u[0][5].set_color(u_color)
        nabla_x_y_u[0][8].set_color(v_color)
        
        formula_u_p_t =  MathTex(r"\frac{\partial u}{\partial t}").scale(2).shift(DOWN)
        formula_u_p_t[0][1].set_color(u_color)
        formula_u_p_t[0][4].set_color(t_color)
        
        
        self.play(AnimationGroup(
            FadeIn(formulau),
            Create(a_u_x),
            FadeIn(formulax),
            Create(a_u_y),
            FadeIn(formulay),
            Create(a_u_t),
            FadeIn(formulat),
            lag_ratio=0.5
    
        ))
        self.wait()
        self.play(Create(a_x_t),Create(a_y_t))
        self.wait()
        self.play(Write(formulau_d_t_xy[2]))
        self.wait()
        self.play(Write(formulau_d_t_xy[4]),Write(formulau_d_t_xy[7]))
        self.wait()
        self.play(Write(formulau_d_t_xy[0:2]),Write(formulau_d_t_xy[3]),Write(formulau_d_t_xy[5:7]),Write(formulau_d_t_xy[8]))
        self.wait()
        self.play(VGroup(formulau_d_t_xy[0], formulau_d_t_xy[1], formulau_d_t_xy[2]).copy().animate.shift(2*DOWN+0.5*RIGHT))
        self.wait()
        self.play(formulau_d_t_xy[3].copy().animate.shift(2*DOWN+0.5*RIGHT))
        self.wait()
        self.play(Transform(VGroup(formulau_d_t_xy[4],formulau_d_t_xy[7]).copy(),nabla_x_y_u[0][0:7]))
        self.wait()
        self.play(FadeIn(nabla_x_y_u[0][7]))
        self.play(Transform(VGroup(formulau_d_t_xy[5],formulau_d_t_xy[8]).copy(),nabla_x_y_u[0][8]))
        self.wait()
        
        # Create multiple concentric circles with different colors
        colors = [RED, RED_B,RED_D,ORANGE, YELLOW_D, GREEN_E,GREEN_C,GREEN, PURPLE]
        circles = VGroup(*[ Ellipse(width=2 + i*1.0, height=1 + i*0.5, stroke_width=5, color=colors[i % len(colors)]) for i in range(7)]).scale(0.98).to_edge(DOWN+LEFT,buff=0.1)
        

        # Create an arrow pointing to one of the circles
        arrow = Arrow(start=circles[6].get_bottom(), end=circles[0].get_bottom(), buff=0.1, color=BLUE)

        # Add all elements to the scene
        self.play(FadeIn(circles))
        self.play(Create(arrow, start= arrow.get_bottom()))
        self.wait()
        self.play(arrow.animate.rotate(PI/2))
        self.wait()
        self.play(arrow.animate.rotate(-PI/2))
        self.wait()
        self.play(arrow.animate.scale(2))
        self.wait()
        self.play(a_u_t.copy().animate.set_color(PINK))
        self.wait()
        self.play(a_u_t.copy().animate.set_color(arrow_color))
        self.wait()
        self.play(FadeOut(circles),FadeOut(arrow))
        self.wait()       
        to_keep = [formulau,formulay,formulax,formulat,a_u_x,a_u_y,a_u_t,a_x_t,a_y_t]
        to_fade = [mobj for mobj in self.mobjects if mobj not in to_keep]
        self.play(*[FadeOut(mobj) for mobj in to_fade])
        self.wait()
        self.play(AnimationGroup(
            Create(a_u_z,start= a_u_z.get_bottom()),
            Write(formulaz),
            lag_ratio= 0.5
        ))
        self.wait()
        self.play(Write(formula_u_p_t))
        self.wait()
        a_u_t.set_color(RED)
        self.play(ApplyWave(a_u_t))
        
        self.wait()
        to_Group = VGroup(formulau,formulay,formulax,formulat,formulaz,a_u_x,a_u_y,a_u_t,a_x_t,a_y_t,a_u_z).copy()
        self.play(to_Group.animate.shift(9*RIGHT))
        a_u_t.set_color(RED)
        self.wait()
        
        to_Group[5:10].set_color(RED)
        self.play(ApplyWave(to_Group[5:10]))
        self.wait()
        
class Solutions(Scene):
    def construct(self):
        self.camera.background_color = black_color
        title1 = Text("解决方案 1：函数方法", color=BLUE).scale(1.3)
        content1 = Text("偏微分方程，量子力学", color=BLUE).scale(1.3).next_to(title1, DOWN)
        title2 = Text("解决方案 2：方程方法", color=RED_E).scale(1.3).next_to(content1, 4*DOWN)
        content2 = Text("热力学，平衡化学", color=RED_E).scale(1.3).next_to(title2, DOWN).align_to(title2, LEFT)
        all_texts = VGroup(title1, content1, title2, content2).move_to(LEFT+UP)
        
        
        formulau = MathTex(r"u").scale(2).to_edge(LEFT,buff = 0.5).shift(2*UP).set_color(u_color)
        formulaz = MathTex(r"z").scale(2).next_to(formulau,4*DOWN+7*RIGHT).set_color(z_color)
        formulax = MathTex(r"x").scale(2).next_to(formulau,4*UP+7*RIGHT).set_color(x_color)
        formulay = MathTex(r"y").scale(2).next_to(formulau,0.1*UP+7*RIGHT).set_color(y_color)
        formulat = MathTex(r"t").scale(2).next_to(formulau,0.1*DOWN+14*RIGHT).set_color(t_color)
        formulas = MathTex(r"s").scale(2).move_to([formulat.get_center()[0],formulax.get_center()[1],0]).set_color(t_color)
        
        a_z_x = Arrow(formulaz.get_right(),formulax.get_left(),buff=0.1).set_color(arrow_color)
        a_z_y = Arrow(formulaz.get_right(),formulay.get_left(),buff=0.1).set_color(arrow_color)
        a_x_t = Arrow(formulax.get_right(),formulat.get_left(),buff=0.1).set_color(arrow_color)
        a_y_t = Arrow(formulay.get_right(),formulat.get_left(),buff=0.1).set_color(arrow_color)
        a_x_s = Arrow(formulax.get_right(),formulas.get_left(),buff=0.1).set_color(arrow_color)
        a_y_s = Arrow(formulay.get_right(),formulas.get_left(),buff=0.1).set_color(arrow_color)
        a_u_x = Arrow(formulau.get_right(),formulax.get_left(),buff=0.1).set_color(arrow_color)
        a_u_y = Arrow(formulau.get_right(),formulay.get_left(),buff=0.1).set_color(arrow_color)
        a_u_t = Arrow(formulau.get_right(),formulat.get_left(),buff=0.1).set_color(arrow_color)
        a_u_z = Arrow(formulau.get_right(),formulaz.get_left(),buff=0.1).set_color(arrow_color)
        
        formulau_d_t_xy = MathTex(r"\frac{d u}{d t}","=",r"\frac{\partial u}{\partial t}","+",r"\frac{\partial u}{\partial x} ",r"\frac{d x}{d t}","+",r"\frac{\partial u}{\partial y}" ,r"\frac{d y}{d t}").scale(1.4)
        formulau_d_t_xy.to_edge(UP+RIGHT,buff=0.5).shift(0.5*LEFT)
        formulau_d_t_xy[0][1].set_color(u_color)
        formulau_d_t_xy[2][1].set_color(u_color)
        formulau_d_t_xy[4][1].set_color(u_color)
        formulau_d_t_xy[7][1].set_color(u_color)
        formulau_d_t_xy[0][4].set_color(t_color)
        formulau_d_t_xy[2][4].set_color(t_color)
        formulau_d_t_xy[5][4].set_color(t_color)
        formulau_d_t_xy[8][4].set_color(t_color)
        formulau_d_t_xy[4][4].set_color(x_color)
        formulau_d_t_xy[5][1].set_color(x_color)
        formulau_d_t_xy[7][4].set_color(y_color)
        formulau_d_t_xy[8][1].set_color(y_color)
        
        nabla_x_y_u = MathTex(r"\left(\nabla_{x, y} u\right) \cdot \mathbf{v}").scale(1.4).move_to(formulau_d_t_xy[6].copy().shift(2*DOWN+0.5*RIGHT).get_center())
        nabla_x_y_u[0][2].set_color(x_color)
        nabla_x_y_u[0][4].set_color(y_color)
        nabla_x_y_u[0][5].set_color(u_color)
        nabla_x_y_u[0][8].set_color(v_color)
        
        formula_u_p_t =  MathTex(r"\frac{\partial u}{\partial t}").scale(1.5).shift(DOWN)
        formula_u_p_t[0][1].set_color(u_color)
        formula_u_p_t[0][4].set_color(t_color)
        
        formulau_f_xyzt =  MathTex(r"u = f(x,y,z,t)").scale(1.5).to_edge(UP,buff=0.2)
        formulau_f_xyzt[0][0].set_color(u_color)
        formulau_f_xyzt[0][2].set_color(f_color)
        formulau_f_xyzt[0][4].set_color(x_color)
        formulau_f_xyzt[0][6].set_color(y_color)
        formulau_f_xyzt[0][8].set_color(z_color)
        formulau_f_xyzt[0][10].set_color(t_color)
        
        formulau_u_xyzt =  MathTex(r"u = u(x,y,z,t)").scale(1.5).to_edge(UP,buff=0.2)
        formulau_u_xyzt[0][0].set_color(u_color)
        formulau_u_xyzt[0][2].set_color(u_color)
        formulau_u_xyzt[0][4].set_color(x_color)
        formulau_u_xyzt[0][6].set_color(y_color)
        formulau_u_xyzt[0][8].set_color(z_color)
        formulau_u_xyzt[0][10].set_color(t_color)
        
        formulax_g_t = MathTex(r"x = g(t)").scale(1.5).next_to(formulau_f_xyzt,DOWN)
        formulax_g_t[0][0].set_color(x_color)
        formulax_g_t[0][4].set_color(t_color)
        
        formulax_x_t = MathTex(r"x = x(t)").scale(1.5).next_to(formulau_f_xyzt,DOWN)
        formulax_x_t[0][0].set_color(x_color)
        formulax_x_t[0][2].set_color(x_color)
        formulax_x_t[0][4].set_color(t_color)
        
        formulay_h_t = MathTex(r"y = h(t)").scale(1.5).next_to(formulax_g_t,DOWN)
        formulay_h_t[0][0].set_color(y_color)
        formulay_h_t[0][4].set_color(t_color)
        
        formulay_y_t = MathTex(r"y = y(t)").scale(1.5).next_to(formulax_g_t,DOWN)
        formulay_y_t[0][0].set_color(y_color)
        formulay_y_t[0][2].set_color(y_color)
        formulay_y_t[0][4].set_color(t_color)
        
        formulaf_p_t = MathTex(r"\frac{\partial f}{\partial t}").scale(1.5).shift(DOWN+4*LEFT)
        formulaf_p_t[0][1].set_color(f_color)
        formulaf_p_t[0][4].set_color(t_color)
        
        formulafxyzt_p_t = MathTex(r"\frac{\partial f(x,y,z,t)}{\partial t}").scale(1.5).shift(DOWN+4*LEFT)
        formulafxyzt_p_t[0][1].set_color(f_color)
        formulafxyzt_p_t[0][3].set_color(x_color)
        formulafxyzt_p_t[0][5].set_color(y_color)
        formulafxyzt_p_t[0][7].set_color(z_color)
        formulafxyzt_p_t[0][9].set_color(t_color)
        formulafxyzt_p_t[0][13].set_color(t_color)
        
        
        formulafx_ht_zt_p_t = MathTex(r"\frac{\partial f(x,h(t),z,t)}{\partial t}").scale(1.5).shift(DOWN+4*LEFT)
        formulafx_ht_zt_p_t[0][1].set_color(f_color)
        formulafx_ht_zt_p_t[0][3].set_color(f_color)
        formulafx_ht_zt_p_t[0][7].set_color(t_color)
        formulafx_ht_zt_p_t[0][-1].set_color(t_color)
        formulafx_ht_zt_p_t[0][-5].set_color(t_color)
        formulafx_ht_zt_p_t[0][-7].set_color(z_color)
        
        formulafu_xt_yt_zt_t = MathTex(r"\frac{\partial u(x(t),y(t),z,t)}{\partial t}").scale(1.5).shift(DOWN+4*RIGHT)
        formulafu_xt_yt_zt_t[0][1].set_color(u_color)
        formulafu_xt_yt_zt_t[0][3].set_color(x_color)
        formulafu_xt_yt_zt_t[0][5].set_color(t_color)
        formulafu_xt_yt_zt_t[0][8].set_color(y_color)
        formulafu_xt_yt_zt_t[0][10].set_color(t_color)
        formulafu_xt_yt_zt_t[0][-5].set_color(t_color)
        formulafu_xt_yt_zt_t[0][-7].set_color(z_color)
        formulafu_xt_yt_zt_t[0][-1].set_color(t_color)
        
        formulauxyzt_p_t = MathTex(r"\frac{\partial u(x,y,z,t)}{\partial t}").scale(1.5).shift(DOWN+4*LEFT)
        formulauxyzt_p_t[0][1].set_color(u_color)
        formulauxyzt_p_t[0][3].set_color(x_color)
        formulauxyzt_p_t[0][5].set_color(y_color)
        formulauxyzt_p_t[0][7].set_color(z_color)
        formulauxyzt_p_t[0][9].set_color(t_color)
        formulauxyzt_p_t[0][13].set_color(t_color)
        
        formulau_p_t_xy = MathTex(r"\left(\frac{\partial u}{\partial t}\right)_{x, y}","=",r"\left(u_t\right)_{x, y}").scale(1.5).shift(DOWN+3*LEFT)
        formulau_p_t_xy[0][2].set_color(u_color)
        formulau_p_t_xy[0][5].set_color(t_color)
        formulau_p_t_xy[0][7].set_color(x_color)
        formulau_p_t_xy[0][9].set_color(y_color)
        formulau_p_t_xy[2][-1].set_color(y_color)
        formulau_p_t_xy[2][-3].set_color(x_color)
        formulau_p_t_xy[2][-5].set_color(t_color)
        formulau_p_t_xy[2][-6].set_color(u_color)
        
        
        self.play(Write(title1),Write(title2))
        self.wait()
        self.play(Write(content1))
        self.wait()
        self.play(Write(content2))
        self.wait()
        self.play(FadeOut(title1),FadeOut(title2),FadeOut(content1),FadeOut(content2))
        
        to_keep = VGroup(formulau,formulay,formulax,formulat,formulaz,formula_u_p_t,a_u_x,a_u_y,a_u_t,a_x_t,a_y_t,a_u_z)
        to_keep[8].set_color(RED)
        to_Group = VGroup(formulau,formulay,formulax,formulat,formulaz,a_u_x,a_u_y,a_u_t,a_x_t,a_y_t,a_u_z).copy().shift(9*RIGHT)
        to_Group[5:10].set_color(RED)
        self.add(to_keep,to_Group)
        self.wait()
        self.play(formula_u_p_t.animate.shift(5*RIGHT))
        
        self.wait()
        self.play(Write(formulau_f_xyzt))
        self.play(ApplyWave(VGroup(a_u_x,a_u_y,a_u_z,a_u_t)))
        self.wait()
        self.play(Write(formulax_g_t))
        self.play(ApplyWave(a_x_t))
        self.wait()
        self.play(Write(formulay_h_t))
        self.play(ApplyWave(a_y_t))
        self.wait()
        self.play(Write(formulaf_p_t))
        self.wait()
        self.play(TransformMatchingShapes(formulaf_p_t[0][0:3],formulafxyzt_p_t[0][0:-2]))
        self.wait()
        self.play(a_u_y.animate.set_color(RED),a_y_t.animate.set_color(RED))
        self.play(ApplyWave(a_u_y),ApplyWave(a_y_t),ApplyWave(a_u_t))
        self.wait()
        self.play(TransformMatchingShapes(formulafxyzt_p_t,formulafx_ht_zt_p_t))
        self.wait()
        self.play(TransformMatchingShapes(formulafx_ht_zt_p_t,formulafxyzt_p_t))
        self.wait()
        self.play(AnimationGroup(
            a_u_y.animate.set_color(arrow_color),
            a_y_t.animate.set_color(arrow_color),
        ),ApplyWave(a_u_y),ApplyWave(a_y_t),ApplyWave(a_u_t))
        self.play(Transform(formulafxyzt_p_t,formulaf_p_t))
        self.wait()
        self.play(AnimationGroup(
                TransformMatchingShapes(formulau_f_xyzt,formulau_u_xyzt),
                TransformMatchingShapes(formulax_g_t,formulax_x_t),
                TransformMatchingShapes(formulay_h_t,formulay_y_t)),
                lag_ratio= 0.5
                  )
        self.wait()
        self.play(FadeOut(formulafxyzt_p_t),FadeOut(formulaf_p_t),FadeOut(formula_u_p_t))
        self.wait()
        
        self.play(FadeIn(formulauxyzt_p_t),FadeIn(formulafu_xt_yt_zt_t))
        self.wait()
        self.play(TransformMatchingShapes(formulafu_xt_yt_zt_t,formula_u_p_t))
        self.wait()
        self.play(TransformMatchingShapes(formula_u_p_t.copy(),formulau_p_t_xy[0:2]),FadeOut(formulauxyzt_p_t))
        self.wait()
        self.play(FadeIn(formulau_p_t_xy[2]))
        self.wait()
        
        
class Applications(Scene):
    def construct(self):
        self.camera.background_color = black_color
        
        formulax = MathTex(r"x").set_color(x_color).to_edge(UP+LEFT,buff=1).shift(DOWN).scale(1.5)
        formulay = MathTex(r"y").set_color(y_color).scale(1.5).next_to(formulax,DOWN)
        formulat = MathTex(r"t").set_color(t_color).scale(1.5).move_to([-4,(formulax.get_center()[1]+formulay.get_center()[1])/2,0])
        formulaPsi = MathTex(r"\Psi").scale(1.5).to_edge(DOWN+LEFT).shift(0.7*UP+0.3*RIGHT).set_color(ORANGE)
        
        formulax_t = MathTex(r"x(t),").to_edge(UP+LEFT,buff=1).scale(2)
        formulax_t[0][0].set_color(x_color)
        formulax_t[0][2].set_color(t_color)
        formulay_t = MathTex(r"y(t)").next_to(formulax_t,3*RIGHT).scale(2)
        formulay_t[0][0].set_color(y_color)
        formulay_t[0][2].set_color(t_color)
        
        formulaPsi_xyt = MathTex(r"\Psi(x, y, t)").scale(2).to_edge(DOWN+LEFT).shift(2.3*UP)
        formulaPsi_xyt[0][0].set_color(ORANGE)
        formulaPsi_xyt[0][2].set_color(x_color)
        formulaPsi_xyt[0][4].set_color(y_color)
        formulaPsi_xyt[0][6].set_color(t_color)
        x = formulax.copy().next_to(formulaPsi,8*RIGHT+UP)
        y = formulay.copy().next_to(formulaPsi,8*RIGHT)
        t = formulat.copy().next_to(formulaPsi,8*RIGHT+DOWN)
        
        a_x_t = Arrow(formulax.get_right(),formulat.get_left(),buff=0.1).set_color(arrow_color)
        a_y_t = Arrow(formulay.get_right(),formulat.get_left(),buff=0.1).set_color(arrow_color)
        a_psi_x = Arrow(formulaPsi.get_right(),x.get_left(),buff=0.1).set_color(arrow_color)
        a_psi_y = Arrow(formulaPsi.get_right(),y.get_left(),buff=0.1).set_color(arrow_color)
        a_psi_t = Arrow(formulaPsi.get_right(),t.get_left(),buff=0.1).set_color(arrow_color)
        
        axes = Axes(
            x_range=[0, 3, 10],
            y_range=[0, 3, 10],
            axis_config={"color": BLUE}
        ).scale(0.5).to_edge(UP+RIGHT)

        
        # 绘制函数 f(x) = x^2
        graph = axes.plot(lambda x: 3*x-x**2, color=WHITE)
        x_value = 0.5
        point = axes.input_to_graph_point(x_value, graph)
        arrow = Arrow(start = axes.coords_to_point(0,0),end = point,buff=0).set_color(ORANGE)

        graph1 = axes.plot(lambda x: 20*x-20*x**2, color=WHITE)
        x_value = 0.5
        point1 = axes.input_to_graph_point(x_value, graph1)
        arrow1 = Arrow(start = axes.coords_to_point(0,0),end = point1,buff=0).set_color(ORANGE)
       
        graph2 = axes.plot(lambda x: 20*x-30*x**2, color=WHITE)
        x_value = 0.5
        point2 = axes.input_to_graph_point(x_value, graph2)
        arrow2 = Arrow(start = axes.coords_to_point(0,0),end = point2,buff=0).set_color(ORANGE)
        
        graph3 = axes.plot(lambda x: 20*x-20*x**2, color=WHITE)
        x_value = 0.5
        point3 = axes.input_to_graph_point(x_value, graph3)
        arrow3 = Arrow(start = axes.coords_to_point(0,0),end = point3,buff=0).set_color(ORANGE)
        
        graph4 = axes.plot(lambda x: x-0.25*x**2+0.25*np.sin(x), color=WHITE)
        x_value = 0.5
        point4 = axes.input_to_graph_point(x_value, graph4)
        arrow4 = Arrow(start = axes.coords_to_point(0,0),end = point4,buff=0).set_color(ORANGE)
        
        self.add(axes, graph,arrow)
        self.play(Create(VGroup(formulax,formulay,formulat,formulax_t,formulay_t,a_x_t,a_y_t)))
        
        self.play(Transform(graph,graph1),Transform(arrow,arrow1))
        self.play(Transform(graph,graph2),Transform(arrow,arrow2))
        self.play(Transform(graph,graph3),Transform(arrow,arrow3))
        self.play(Transform(graph,graph4),Transform(arrow,arrow4))
        self.wait()
        # 动画：时间追踪器从 0 到 2PI 变化
        self.play(Write(VGroup(formulaPsi_xyt,formulaPsi,x,y,t,a_psi_x,a_psi_y,a_psi_t)))
        self.wait()

class QuantumEigenstates(ThreeDScene):
    def construct(self):
        self.camera.background_color = black_color
        axes = ThreeDAxes(x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-2, 2, 0.5])
        time_tracker = ValueTracker(0)  # 创建一个用于追踪时间的 ValueTracker 对象

        # 定义依赖时间的波函数
        def wave_function(u, v, t):
            return np.sin(u * t) * np.cos(v * t)

        # 创建随时间更新的表面
        def create_surface(t):
            return Surface(
                lambda u, v: axes.c2p(u, v, wave_function(u, v, t)),
                u_range=[-PI, PI],
                v_range=[-PI, PI],
                resolution=(30, 30)
            )

        # 使用 always_redraw 来确保每一帧都重新绘制表面
        surface = always_redraw(lambda: create_surface(time_tracker.get_value()))

        # 添加坐标系和表面到场景
        self.add(surface)

        # 设置摄像机角度
        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES)

        # 动画：时间追踪器从 0 到 2PI 变化
        self.play(time_tracker.animate.set_value(2*PI), run_time=20, rate_func=linear)
        self.wait()

class Applictions2(Scene):
    def construct(self):
        self.camera.background_color = black_color
        
        formulaP_p_T_vn= MathTex(r"\left(\frac{\partial P}{\partial T}\right)_{V , n}").scale(2)
        formulaP_p_T_vn[0][2].set_color(P_color)
        formulaP_p_T_vn[0][5].set_color(t_color)
        formulaP_p_T_vn[0][7].set_color(v_color)
        formulaP_p_T_vn[0][9].set_color(n_color)
        
        formulaPV_nRT = MathTex(r"PV = nRT").scale(2)
        formulaPV_nRT[0][0].set_color(P_color)
        formulaPV_nRT[0][1].set_color(v_color)
        formulaPV_nRT[0][3].set_color(n_color)
        formulaPV_nRT[0][4].set_color(R_color)
        formulaPV_nRT[0][5].set_color(t_color)
        
        formulav_n= MathTex(r"\left(\frac{\partial P}{\partial T}\right)_{V / n}").scale(2)
        formulav_n[0][2].set_color(P_color)
        formulav_n[0][5].set_color(t_color)
        formulav_n[0][7].set_color(v_color)
        formulav_n[0][9].set_color(n_color)
        
        vg1 = VGroup(formulav_n,formulaPV_nRT)
        
        image = ImageMobject("image/pvt.jpg").shift(3*RIGHT).scale(0.23)
        
        
        
        
        self.play(Write(formulaPV_nRT))
        self.wait()
        self.play(formulaPV_nRT.animate.to_edge(UP))
        self.play(Write(formulaP_p_T_vn[0][1:6]))
        self.wait()
        self.play(Write(formulaP_p_T_vn[0][0]),Write(formulaP_p_T_vn[0][6:]))
        self.wait()
        self.play(TransformMatchingShapes(formulaP_p_T_vn,formulav_n))
        self.wait() 
        self.play(vg1.animate.to_edge(LEFT))
        self.add(image)
        self.wait() 
        
        cross = Cross(formulaPV_nRT, stroke_color=RED, stroke_width=6)
        self.play(Create(cross))
        self.wait()
        self.play(ApplyWave(formulav_n))
        self.wait()
        self.play(ApplyWave(formulav_n))
        
        reline = Line([3,-2.38,0],[6.15,0.64,0],stroke_width=6,color = RED)
        self.play(FadeIn(reline))
        self.wait()
        
class Applictions3(Scene):
    def construct(self):
        self.camera.background_color = black_color

        formlax_123 = MathTex(r"x_1","+",r"x_2","+",r"x_3","=","1").scale(2)
        formlax_123[0].set_color(BLUE)
        formlax_123[2].set_color(RED)
        formlax_123[4].set_color(GREEN)
        
        formlax_132 = MathTex(r"x_1","+",r"x_3","=","1","-",r"x_2").scale(2)
        formlax_132[0].set_color(BLUE)
        formlax_132[2].set_color(GREEN)
        formlax_132[-1].set_color(RED)
        
        formlax_1312 = MathTex(r"x_1",r"\left(1","+",r"\frac{x_3}{x_1}",r"\right)","=","1","-",r"x_2").scale(2)
        formlax_1312[0].set_color(x1_color)
        formlax_1312[3][0:2].set_color(x1_color)
        formlax_1312[3][3:5].set_color(x3_color)
        formlax_1312[-1].set_color(x2_color)
        
        formlax_1231 = MathTex(r"x_1","=",r"\frac{1-x_2}{1+\frac{x_3}{x_1}}").scale(2)
        formlax_1231[0].set_color(x1_color)
        formlax_1231[2][2:4].set_color(x2_color)
        formlax_1231[2][7:9].set_color(x3_color)
        formlax_1231[2][10:12].set_color(x1_color)
        
        formlax1_p_x2_13 = MathTex(r"\left(\frac{\partial x_1}{\partial x_2}\right)_{x_1 / x_3}").scale(1.5).to_edge(UP).shift(RIGHT)
        formlax1_p_x2_13[0][2:4].set_color(x1_color)
        formlax1_p_x2_13[0][6:8].set_color(x2_color)
        formlax1_p_x2_13[0][9:11].set_color(x1_color)
        formlax1_p_x2_13[0][12:14].set_color(x3_color)
        
        formlax_31 = MathTex("=",r"\frac{-1}{1+\frac{x_3}{x_1}}").scale(1.5).next_to(formlax1_p_x2_13,RIGHT)
        formlax_31[1][-2:].set_color(x1_color)
        formlax_31[1][-5:-3].set_color(x3_color)
        
        formlax_113 = MathTex("=",r"\frac{-x_1}{x_1+x_3}").scale(1.5).next_to(formlax1_p_x2_13,RIGHT)
        formlax_113[1][1:3].set_color(x1_color)
        formlax_113[1][4:6].set_color(x1_color)
        formlax_113[1][-2:].set_color(x3_color)
        
        formlax_12 = MathTex("=",r"\frac{-x_1}{1-x_2}").scale(1.5).next_to(formlax1_p_x2_13,RIGHT)
        formlax_12[1][1:3].set_color(x1_color)
        formlax_12[1][-2:].set_color(x2_color)
        
        vg1 = VGroup(formlax1_p_x2_13,formlax_12)
        
        image = ImageMobject("image/2.png").scale_to_fit_height(config.frame_height-1).to_edge(RIGHT,buff=0)
        
        arrow = Arrow([3.9,1.2,0],[0,-0.9,0],stroke_width=6,color = RED)
        
        
        self.play(Write(formlax_123))
        self.wait()
        self.play(TransformMatchingTex(formlax_123,formlax_132))
        self.wait()
        self.play(TransformMatchingTex(formlax_132,formlax_1312))
        self.wait()
        self.play(TransformMatchingTex(formlax_1312,formlax_1231 ))
        self.wait()
        self.play(formlax_1231.animate.scale(0.75).to_edge(UP+LEFT),FadeIn(formlax1_p_x2_13))
        self.wait()
        self.play(Write(formlax_31))
        self.wait()
        self.play(TransformMatchingShapes(formlax_31,formlax_113))
        self.wait()
        self.play(TransformMatchingTex(formlax_113,formlax_12))
        self.wait()
        self.play(vg1.animate.scale(1/1.5).to_edge(LEFT).shift(3*DOWN))
        self.add(image)
        self.add(arrow)
        self.wait() 
        
class Outro(Scene):
    def construct(self):
        self.camera.background_color = black_color
        title1 = Text("解决方案 1：函数方法", color=BLUE).scale(1.3).to_edge(UP)
        content1 = Text("偏微分方程，量子力学", color=BLUE).scale(1.3).next_to(title1, DOWN)
        title2 = Text("解决方案 2：方程方法", color=RED_E).scale(1.3).next_to(content1, 4*DOWN)
        content2 = Text("热力学，平衡化学", color=RED_E).scale(1.3).next_to(title2, DOWN).align_to(title2, LEFT)
        formulau = MathTex(r"u").scale(2).to_edge(LEFT,buff = 0.5).shift(2*UP).set_color(u_color)
        formulaz = MathTex(r"z").scale(2).next_to(formulau,4*DOWN+7*RIGHT).set_color(z_color)
        formulax = MathTex(r"x").scale(2).next_to(formulau,4*UP+7*RIGHT).set_color(x_color)
        formulay = MathTex(r"y").scale(2).next_to(formulau,0.1*UP+7*RIGHT).set_color(y_color)
        formulat = MathTex(r"t").scale(2).next_to(formulau,0.1*DOWN+14*RIGHT).set_color(t_color)
        formulas = MathTex(r"s").scale(2).move_to([formulat.get_center()[0],formulax.get_center()[1],0]).set_color(t_color)
        
        
        a_z_x = Arrow(formulaz.get_right(),formulax.get_left(),buff=0.1).set_color(arrow_color)
        a_z_y = Arrow(formulaz.get_right(),formulay.get_left(),buff=0.1).set_color(arrow_color)
        a_x_t = Arrow(formulax.get_right(),formulat.get_left(),buff=0.1).set_color(arrow_color)
        a_y_t = Arrow(formulay.get_right(),formulat.get_left(),buff=0.1).set_color(arrow_color)
        a_x_s = Arrow(formulax.get_right(),formulas.get_left(),buff=0.1).set_color(arrow_color)
        a_y_s = Arrow(formulay.get_right(),formulas.get_left(),buff=0.1).set_color(arrow_color)
        a_u_x = Arrow(formulau.get_right(),formulax.get_left(),buff=0.1).set_color(arrow_color)
        a_u_y = Arrow(formulau.get_right(),formulay.get_left(),buff=0.1).set_color(arrow_color)
        a_u_t = Arrow(formulau.get_right(),formulat.get_left(),buff=0.1).set_color(arrow_color)
        a_u_z = Arrow(formulau.get_right(),formulaz.get_left(),buff=0.1).set_color(arrow_color)
              
        formulau_d_t_xy = MathTex(r"\frac{d u}{d t}","=",r"\frac{\partial u}{\partial t}","+",r"\frac{\partial u}{\partial x} ",r"\frac{d x}{d t}","+",r"\frac{\partial u}{\partial y}" ,r"\frac{d y}{d t}").scale(1.4)
        formulau_d_t_xy.to_edge(UP+RIGHT,buff=0.5).shift(0.5*LEFT)
        formulau_d_t_xy[0][1].set_color(u_color)
        formulau_d_t_xy[2][1].set_color(u_color)
        formulau_d_t_xy[4][1].set_color(u_color)
        formulau_d_t_xy[7][1].set_color(u_color)
        formulau_d_t_xy[0][4].set_color(t_color)
        formulau_d_t_xy[2][4].set_color(t_color)
        formulau_d_t_xy[5][4].set_color(t_color)
        formulau_d_t_xy[8][4].set_color(t_color)
        formulau_d_t_xy[4][4].set_color(x_color)
        formulau_d_t_xy[5][1].set_color(x_color)
        formulau_d_t_xy[7][4].set_color(y_color)
        formulau_d_t_xy[8][1].set_color(y_color)
        
        surrounding_rectangle = SurroundingRectangle(formulau_d_t_xy[2], color=ORANGE)
        
        afgp = VGroup(formulau,formulax,formulay,formulaz,formulat,a_u_x,a_u_y,a_u_t,a_x_t,a_y_t,a_u_z).copy().shift(4*DOWN)
        
        formulau_p_t_xy = MathTex(r"\frac{\partial u}{\partial t}","=",r"\left(\frac{\partial u}{\partial t}\right)_{x, y}" ,"+",r"\frac{\partial u}{\partial x} ",r"\frac{d x}{d t}","+",r"\frac{\partial u}{\partial y}" ,r"\frac{d y}{d t}").scale(1.3).shift(DOWN+1.8*RIGHT)
        formulau_p_t_xy[0][1].set_color(u_color)
        formulau_p_t_xy[4][1].set_color(u_color)
        formulau_p_t_xy[7][1].set_color(u_color)
        formulau_p_t_xy[0][4].set_color(t_color)
        formulau_p_t_xy[5][4].set_color(t_color)
        formulau_p_t_xy[8][4].set_color(t_color)
        formulau_p_t_xy[4][4].set_color(x_color)
        formulau_p_t_xy[5][1].set_color(x_color)
        formulau_p_t_xy[7][4].set_color(y_color)
        formulau_p_t_xy[8][1].set_color(y_color)
        formulau_p_t_xy[2][2].set_color(u_color)
        formulau_p_t_xy[2][5].set_color(t_color)
        formulau_p_t_xy[2][7].set_color(x_color)
        formulau_p_t_xy[2][9].set_color(y_color)
        
        surrounding_rectangle1 = SurroundingRectangle(formulau_p_t_xy[0], color=ORANGE)
        
        self.play(FadeIn(title1),FadeIn(title2))
        self.wait()
        self.clear()
        self.play(AnimationGroup(
            Create(formulau),
            Create(a_u_x),
            Create(formulax),
            Create(a_u_y),
            Create(formulay),
            Create(a_u_t),
            Create(a_x_t),
            Create(a_y_t),
            Create(formulat)
        ))
        self.wait()
        self.play(Write(formulau_d_t_xy))
        self.wait()
        self.play(Write(surrounding_rectangle))
        self.wait()
        self.play(Write(afgp))
        self.wait()
        self.play(Write(formulau_p_t_xy))
        self.wait()
        self.play(Write(surrounding_rectangle1))
        self.wait()

class Outro2(Scene):
    def construct(self):
        self.camera.background_color = black_color
        
        formulau = MathTex(r"u").scale(2).to_edge(LEFT,buff = 0.5).shift(2*UP).set_color(u_color)
        formulaz = MathTex(r"z").scale(2).next_to(formulau,4*DOWN+7*RIGHT).set_color(z_color)
        formulax = MathTex(r"x").scale(2).next_to(formulau,4*UP+7*RIGHT).set_color(x_color)
        formulay = MathTex(r"y").scale(2).next_to(formulau,0.1*UP+7*RIGHT).set_color(y_color)
        formulat = MathTex(r"t").scale(2).next_to(formulau,0.1*DOWN+14*RIGHT).set_color(t_color)
        formulas = MathTex(r"s").scale(2).move_to([formulat.get_center()[0],formulax.get_center()[1],0]).set_color(t_color)
        
        formulau__t = MathTex(r"\frac{d u}{d t} \quad ",r"\frac{\partial u}{\partial t} \quad",r" \frac{\delta u}{\delta t} \quad",r"\frac{\mathit{7} u}{\mathit{7} t} \quad", r"\frac{\eth u }{\eth t }").scale(2)
        formulau__t[0][1].set_color(u_color)
        formulau__t[0][4].set_color(t_color)
        formulau__t[2][1].set_color(u_color)
        formulau__t[2][4].set_color(t_color)
        formulau__t[1][1].set_color(u_color)
        formulau__t[1][4].set_color(t_color)
        formulau__t[3][1].set_color(u_color)
        formulau__t[3][4].set_color(t_color)
        formulau__t[4][1].set_color(u_color)
        formulau__t[4][4].set_color(t_color)
        
        formulau_d_t_xy = MathTex(r"\frac{d u}{d t}","=",r"\frac{\partial u}{\partial t}","+",r"\frac{\partial u}{\partial x} ",r"\frac{d x}{d t}","+",r"\frac{\partial u}{\partial y}" ,r"\frac{d y}{d t}").scale(1.5).shift(RIGHT)
        formulau_d_t_xy[0][1].set_color(u_color)
        formulau_d_t_xy[2][1].set_color(u_color)
        formulau_d_t_xy[4][1].set_color(u_color)
        formulau_d_t_xy[7][1].set_color(u_color)
        formulau_d_t_xy[0][4].set_color(t_color)
        formulau_d_t_xy[2][4].set_color(t_color)
        formulau_d_t_xy[5][4].set_color(t_color)
        formulau_d_t_xy[8][4].set_color(t_color)
        formulau_d_t_xy[4][4].set_color(x_color)
        formulau_d_t_xy[5][1].set_color(x_color)
        formulau_d_t_xy[7][4].set_color(y_color)
        formulau_d_t_xy[8][1].set_color(y_color)
        
        a_z_x = Arrow(formulaz.get_right(),formulax.get_left(),buff=0.1).set_color(arrow_color)
        a_z_y = Arrow(formulaz.get_right(),formulay.get_left(),buff=0.1).set_color(arrow_color)
        a_x_t = Arrow(formulax.get_right(),formulat.get_left(),buff=0.1).set_color(arrow_color)
        a_y_t = Arrow(formulay.get_right(),formulat.get_left(),buff=0.1).set_color(arrow_color)
        a_x_s = Arrow(formulax.get_right(),formulas.get_left(),buff=0.1).set_color(arrow_color)
        a_y_s = Arrow(formulay.get_right(),formulas.get_left(),buff=0.1).set_color(arrow_color)
        a_u_x = Arrow(formulau.get_right(),formulax.get_left(),buff=0.1).set_color(arrow_color)
        a_u_y = Arrow(formulau.get_right(),formulay.get_left(),buff=0.1).set_color(arrow_color)
        a_u_t = Arrow(formulau.get_right(),formulat.get_left(),buff=0.1).set_color(arrow_color)
        a_u_z = Arrow(formulau.get_right(),formulaz.get_left(),buff=0.1).set_color(arrow_color)
        
        afgp = VGroup(formulau,formulax,formulay,formulat,a_u_x,a_u_y,a_u_t,a_x_t,a_y_t)
        
        brace_d = Brace(formulau_d_t_xy[4:],DOWN).set_color(YELLOW)
        brace_d_text = Text("对流导数").next_to(brace_d,DOWN).set_color(YELLOW)
        
        brace_u = Brace(formulau_d_t_xy[2:],UP).set_color(YELLOW)
        brace_u_text = Text("物质导数").next_to(brace_u,UP).set_color(YELLOW)
        
        format_D = MathTex(r"\frac{D u}{D t}=").scale(1.6).next_to(formulau_d_t_xy,LEFT)
        format_D[0][1].set_color(u_color)
        format_D[0][4].set_color(t_color)
        self.play(Write(formulau__t[0]))
        self.wait()
        self.play(Write(formulau__t[1:3]))
        self.wait()
        self.play(Write(formulau__t[3:]))
        self.wait()
        self.clear()
        self.add(afgp,formulau_d_t_xy)
        self.wait()
        self.play(Write(brace_d),Write(brace_d_text))
        self.wait()
        self.play(Write(brace_u),Write(brace_u_text))
        self.wait()
        self.play(Write(format_D))
        self.wait()