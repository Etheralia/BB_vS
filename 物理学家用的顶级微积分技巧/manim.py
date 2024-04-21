from manim import *

class ComplexTransformation(Scene):
    def construct(self):
        self.camera.background_color = DARK_GRAY
        # 初始公式
        formula = MathTex("e^x").scale(3)
        self.play(Write(formula))
        self.wait(1)
        
        d_form = MathTex("'").next_to(formula,RIGHT+0.5*UP).scale(3)
        self.add(d_form)
        self.wait(1)
        self.remove(d_form)
        self.wait(1) 
        
        # 添加积分符号 
        integral_form = MathTex("\\int").next_to(formula,LEFT).scale(3)
        self.add(integral_form)
        self.wait(1)
        self.remove(integral_form)
        self.wait(1)
        self.clear()
        

        formula = MathTex("e^x", "=", "\\int e^x", "\\, dx").scale(2)
        self.play(Write(formula))
        self.wait(1)

        # 创建一个新的公式，不包含 dx
        integral_eq = MathTex("e^x", "=", "\\int e^x").scale(2)
        
        # 使用 TransformMatchingTexMatchingTex 来转换，并移除 dx
        self.play(TransformMatchingTexMatchingTex(formula, integral_eq))
        self.wait(1)

        # 引入等式左边的减法
        subtract_integral = MathTex("e^x", "-", "\\int e^x", "=", "0").scale(2)
        self.play(TransformMatchingTexMatchingTex(integral_eq, subtract_integral))
        self.wait(1)

        # 简化等式
        simplify_subtract = MathTex("(1-", "\\int)", "e^x", "=", "0").scale(2)
        self.play(TransformMatchingTexMatchingTex(subtract_integral, simplify_subtract))
        self.wait(1)

        # 继续变换
        inverse_operator = MathTex("e^x", "=", "\\left(1-\\int\\right)^{-1}0").scale(2)
        self.play(TransformMatchingTex(simplify_subtract , inverse_operator))
        self.wait(1)

        # 清空屏幕
        self.play(FadeOut(inverse_operator))
        self.wait(1)



class ComplexTransformation1(Scene):
    def construct(self):
        self.camera.background_color = DARK_GRAY

        series_expansion = MathTex("(1-x)^{-1}", "=", "\\frac{1}{1-x}", "=", "1+x+x^2+x^3+x^4+\\ldots").shift(UP)
        self.play(Write(series_expansion))
        self.wait(2)

        # 在下面写入新的公式
        integral_series = MathTex("\\frac{1}{1-\\int}", "=", "1+(\\int)+(\\int)^2+(\\int)^3+(\\int)^4+\\ldots")
        integral_series.next_to(series_expansion, DOWN)
        self.play(Write(integral_series))
        self.wait(2)
        
        # 清空屏幕，写公式
        final_formula1 = MathTex("e^x", "=", "\\left(1-\\int\\right)^{-1} 0").scale(2)
        self.remove(series_expansion,integral_series)
        self.play(Write(final_formula1))
        self.wait(1)

        # 清空屏幕，写公式
        final_formula = MathTex("e^x", "=", "\\left(", "1", "+", "\\int", "+", "\\left(", "\\int", "\\right)^2", "+", "\\left(", "\\int", "\\right)^3", "+", "\\left(", "\\int", "\\right)^4", "+", "\\ldots", "\\right)", "0").scale(1.2)
        self.play(TransformMatchingTex(final_formula1, final_formula))
        self.wait(1)
        
        # 变为 e^x = 0 + (C + (\int)^2 + (\int)^3 + ... )
        more_complex = MathTex("e^x", "=", " 0", "+" "(","\\int", "+", "(","\\int",")^2", "+" "(","\\int",")^3","+", "(","\\int",")^4","+" ,"\\ldots",")", "0").scale(1.2)
        self.play(TransformMatchingTex(final_formula, more_complex))
        self.wait(1)

        # 变为 e^x = 0 + (1 + x + ((\int)^3 + (\int)^4 + ...) 0)
        further_simplified = MathTex("e^x", "=", "0","+","(","1","+","x","+","(","(","\\int)^3","+","(\\int)^4 + \\ldots) ","0",")").scale(1.2)
        self.play(TransformMatchingTex(more_complex, further_simplified))
        self.wait(1)

        # 变为 e^x = 0 + 1 + x + \frac{x^2}{2!} + ((\int)^4 + ...)
        taylor_expansion = MathTex("e^x", "=", "0" ,"+" ,"1" ,"+" ,"x" ,"+" ,"\\frac{x^2}{2!}","+" ,"(","(","\\int",")^4" ,"+" ,"\\ldots",")" ,"0").scale(1.2)
        self.play(TransformMatchingTex(further_simplified , taylor_expansion))
        self.wait(1)

        self.clear()
        integral_formula = MathTex("\\int", "0 ", "\\, dx", "=", "0", "?").scale(2)
        integral_formula.set_color_by_tex("\\int", PURPLE)  # 将 "\\int" 文本设为紫色
        self.play(Write(integral_formula))
        self.wait(1)
        integral_formula1 = MathTex("\\int", "0 ").scale(2)
        integral_formula1.set_color_by_tex("\\int", PURPLE)  # 将 "\\int" 文本设为紫色
        self.play(TransformMatchingTex(integral_formula,integral_formula1))
        self.wait(1)
                
        integral_formula12 = MathTex("\\int","(" ,"0 ",")").scale(2)
        integral_formula12.set_color_by_tex("\\int", GREEN_A)  # 将 "\\int" 文本设为紫色
        self.play(TransformMatchingTex(integral_formula1,integral_formula12))
        self.wait(1)
        
        integral_formula13 = MathTex("?","=","\\int","(" ,"0 ",")").scale(2)
        
        self.play(TransformMatchingTex(integral_formula12,integral_formula13))
        self.wait(1)
        
        integral_formula14 = MathTex("?'","=","0 ").scale(2)
        
        self.play(TransformMatchingTex(integral_formula13,integral_formula14))
        self.wait(1)
        
        
        



class TransformScene(Scene):
    def construct(self):
        # 设置背景颜色
        self.camera.background_color = DARK_GRAY

        # 初始化所有表达式
        equations = [
            MathTex("e^x", "=", "0", "+", "\\left(", "\\int", "+", "\\left(\\int\\right)^2", "+", "\\left(\\int\\right)^3","+", "\\left(\\int\\right)^4", "+", "\\dots", "\\right)", "0").scale(1.1),
            MathTex("e^x", "=", "0", "+", "C", "+", "\\left(", "\\left(\\int\\right)^2", "+", "\\left(\\int\\right)^3","+", "\\left(\\int\\right)^4", "+", "\\dots", "\\right)", "0").scale(1.1),
            MathTex("e^x", "=", "0", "+", "1", "+", "\\left(", "\\left(\\int\\right)^2", "+", "\\left(\\int\\right)^3", "+", "\\left(\\int\\right)^4","+", "\\dots", "\\right)", "0").scale(1.1),
            MathTex("e^x", "=", "0", "+", "1", "+", "x", "+", "\\left(", "\\left(\\int\\right)^3", "+", "\\left(\\int\\right)^4", "+", "\\dots", "\\right)", "0").scale(1.1),
            MathTex("e^x", "=", "0", "+", "1", "+", "x", "+", "\\frac{x^2}{2!}", "+", "\\left(", "\\left(\\int\\right)^4", "+", "\\dots", "\\right)", "0").scale(1.1),
            MathTex("e^x", "=", "0", "+", "1", "+", "x", "+", "\\frac{x^2}{2!}", "+", "\\frac{x^3}{3!}", "+", "\\frac{x^4}{4!}", "+", "\\dots").scale(1.1),
            MathTex("e^x", "=", "1", "+", "x", "+", "\\frac{x^2}{2!}", "+", "\\frac{x^3}{3!}", "+", "\\frac{x^4}{4!}", "+", "\\dots").scale(1.1),
            MathTex("(1-x)^{-1}", "=", "\\frac{1}{1-x}", "=", "1", "+", "x", "+", "x^2", "+", "x^3", "+", "x^4", "+", "\\ldots").scale(1.1),
            MathTex("\\frac{1}{1-\\int}", "=", "1", "+", "\\left(\\int\\right)", "+", "\\left(\\int\\right)^2", "+", "\\left(\\int\\right)^3", "+", "\\left(\\int\\right)^4", "+", "\\dots").scale(1.1)
        ]

        # 初始表达式
        current_expression = equations[0]
        self.play(Write(current_expression))

        # 逐步变换到下一个表达式
        for new_expression in equations[1:7]:
            self.play(TransformMatchingTex(current_expression, new_expression))
            current_expression = new_expression
            self.wait(2)
        # 等待一会儿然后清空屏幕
        self.wait(2)
        self.play(FadeOut(current_expression))

        # 写入最后两个公式
        self.play(Write(equations[-2].shift(UP)))
        self.wait(2)
        self.play(Write(equations[-1].next_to(equations[-2],DOWN)))
        self.wait(2)


