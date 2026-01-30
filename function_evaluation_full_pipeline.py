"""
SAT Question: Function Evaluation (Full Pipeline)
=================================================

Generated using Math-To-Manim Kimi K2.5 Swarm Pipeline:
1. KimiPrerequisiteExplorer - Built knowledge tree
2. KimiMathematicalEnricher - Added equations and definitions
3. KimiVisualDesigner - Planned visual specifications
4. KimiNarrativeComposer - Created narrative prompt

Question: The function f is defined by f(x) = 8x.
For what value of x does f(x) = 72?

Answer: x = 9

To render:
    manim -pql function_evaluation_full_pipeline.py FunctionEvalSAT
"""

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService


class FunctionEvalSAT(VoiceoverScene):
    """
    Full pipeline generated SAT video with proper voiceover.
    """
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))

        # Colors from visual design
        AXIS_COLOR = BLUE
        FUNCTION_COLOR = RED
        SOLUTION_COLOR = GREEN
        HIGHLIGHT_COLOR = YELLOW

        # ========================================
        # Scene 1: Introduce the function
        # ========================================

        title = Text("SAT Question", font_size=36, color=YELLOW)
        title.to_edge(UP, buff=0.5)

        # Function definition with LaTeX (from knowledge tree equations)
        func_def = MathTex(r"f(x) = 8x", font_size=56, color=FUNCTION_COLOR)
        func_def.next_to(title, DOWN, buff=0.6)

        with self.voiceover(
            text="The function f of x is defined as 8 times x."
        ) as tracker:
            self.play(Write(title), run_time=0.3)
            self.play(Write(func_def), run_time=tracker.duration - 0.3)

        # ========================================
        # Scene 2: State the problem
        # ========================================

        problem = MathTex(r"f(x) = 72", font_size=48, color=HIGHLIGHT_COLOR)
        problem.next_to(func_def, DOWN, buff=0.5)

        question_text = Text("Find x = ?", font_size=32)
        question_text.next_to(problem, DOWN, buff=0.4)

        with self.voiceover(
            text="We need to find the value of x when f of x equals 72."
        ) as tracker:
            self.play(Write(problem), run_time=0.5)
            self.play(Write(question_text), run_time=tracker.duration - 0.5)

        self.wait(0.3)

        # ========================================
        # Scene 3: Set up the equation
        # ========================================

        with self.voiceover(
            text="Since f of x equals 8 x, we can substitute to get 8 x equals 72."
        ) as tracker:
            self.play(
                FadeOut(title),
                FadeOut(question_text),
                func_def.animate.to_edge(UP, buff=0.8).scale(0.8),
                problem.animate.move_to(ORIGIN + UP),
                run_time=0.5
            )

            # Show the equation
            equation = MathTex(r"8x = 72", font_size=56, color=HIGHLIGHT_COLOR)
            equation.next_to(problem, DOWN, buff=0.5)
            self.play(Write(equation), run_time=tracker.duration - 0.5)

        # ========================================
        # Scene 4: Solve step by step
        # ========================================

        with self.voiceover(
            text="To isolate x, we divide both sides by 8."
        ) as tracker:
            step1 = MathTex(r"\frac{8x}{8} = \frac{72}{8}", font_size=48)
            step1.next_to(equation, DOWN, buff=0.4)
            self.play(Write(step1), run_time=tracker.duration)

        with self.voiceover(
            text="This simplifies to x equals 9."
        ) as tracker:
            step2 = MathTex(r"x = 9", font_size=64, color=SOLUTION_COLOR)
            step2.next_to(step1, DOWN, buff=0.4)
            self.play(Write(step2), run_time=tracker.duration)

        # ========================================
        # Scene 5: Highlight the answer
        # ========================================

        box = SurroundingRectangle(step2, color=SOLUTION_COLOR, buff=0.15)

        with self.voiceover(
            text="The answer is x equals 9!"
        ) as tracker:
            self.play(Create(box), run_time=tracker.duration)

        # ========================================
        # Scene 6: Verify the solution
        # ========================================

        with self.voiceover(
            text="Let's verify: f of 9 equals 8 times 9, which is 72. Correct!"
        ) as tracker:
            verify = MathTex(
                r"f(9) = 8 \times 9 = 72 \checkmark",
                font_size=36,
                color=SOLUTION_COLOR
            )
            verify.to_edge(DOWN, buff=1.2)
            self.play(Write(verify), run_time=tracker.duration)

        self.wait(0.5)

        # ========================================
        # Scene 7: End card
        # ========================================

        self.play(FadeOut(verify), run_time=0.3)

        follow_text = Text("Follow for daily SAT tips!", font_size=28, color=BLUE_B)
        follow_text.to_edge(DOWN, buff=0.5)

        self.play(FadeIn(follow_text, shift=UP), run_time=0.5)
        self.wait(1.5)


class FunctionEvalWithGraph(VoiceoverScene):
    """
    Extended version with coordinate plane visualization.
    Based on visual design specs from the pipeline.
    """
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))

        # ========================================
        # Scene 1: Show coordinate plane with function
        # ========================================

        with self.voiceover(
            text="Let's visualize the function f of x equals 8 x on a coordinate plane."
        ) as tracker:
            # Create axes
            axes = Axes(
                x_range=[0, 12, 2],
                y_range=[0, 100, 20],
                x_length=6,
                y_length=5,
                axis_config={"color": BLUE},
                tips=False
            )
            axes.to_edge(LEFT, buff=1)

            # Labels
            x_label = axes.get_x_axis_label("x")
            y_label = axes.get_y_axis_label("f(x)")

            self.play(Create(axes), Write(x_label), Write(y_label), run_time=tracker.duration)

        # ========================================
        # Scene 2: Draw the function
        # ========================================

        with self.voiceover(
            text="The function f of x equals 8 x is a straight line through the origin."
        ) as tracker:
            # Plot f(x) = 8x
            graph = axes.plot(lambda x: 8 * x, x_range=[0, 11], color=RED)
            graph_label = MathTex(r"f(x) = 8x", font_size=32, color=RED)
            graph_label.next_to(graph, UP + RIGHT, buff=0.2)

            self.play(Create(graph), Write(graph_label), run_time=tracker.duration)

        # ========================================
        # Scene 3: Find the point where f(x) = 72
        # ========================================

        with self.voiceover(
            text="We want to find x when f of x equals 72. That's the point where the line reaches 72 on the y-axis."
        ) as tracker:
            # Horizontal line at y = 72
            h_line = DashedLine(
                axes.c2p(0, 72),
                axes.c2p(9, 72),
                color=YELLOW
            )
            y_72_label = MathTex(r"72", font_size=28, color=YELLOW)
            y_72_label.next_to(axes.c2p(0, 72), LEFT, buff=0.2)

            self.play(Create(h_line), Write(y_72_label), run_time=tracker.duration)

        # ========================================
        # Scene 4: Mark the solution point
        # ========================================

        with self.voiceover(
            text="The intersection occurs at x equals 9."
        ) as tracker:
            # Vertical line at x = 9
            v_line = DashedLine(
                axes.c2p(9, 0),
                axes.c2p(9, 72),
                color=GREEN
            )

            # Point at (9, 72)
            point = Dot(axes.c2p(9, 72), color=GREEN, radius=0.15)
            point_label = MathTex(r"(9, 72)", font_size=28, color=GREEN)
            point_label.next_to(point, UP + RIGHT, buff=0.1)

            x_9_label = MathTex(r"9", font_size=28, color=GREEN)
            x_9_label.next_to(axes.c2p(9, 0), DOWN, buff=0.2)

            self.play(
                Create(v_line),
                Create(point),
                Write(point_label),
                Write(x_9_label),
                run_time=tracker.duration
            )

        # ========================================
        # Scene 5: Show answer
        # ========================================

        answer_box = VGroup(
            Rectangle(width=3, height=1.2, color=GREEN, fill_opacity=0.2),
            MathTex(r"x = 9", font_size=48, color=GREEN)
        )
        answer_box[1].move_to(answer_box[0].get_center())
        answer_box.to_edge(RIGHT, buff=1).shift(UP)

        with self.voiceover(
            text="So x equals 9 is our answer!"
        ) as tracker:
            self.play(Create(answer_box), run_time=tracker.duration)

        # End card
        follow_text = Text("Follow for daily SAT tips!", font_size=24, color=BLUE_B)
        follow_text.to_edge(DOWN, buff=0.3)

        self.play(FadeIn(follow_text), run_time=0.5)
        self.wait(2)


if __name__ == "__main__":
    print("""
    To render:

    # Basic version (TikTok-ready):
    manim -pql function_evaluation_full_pipeline.py FunctionEvalSAT

    # Extended version with graph:
    manim -pql function_evaluation_full_pipeline.py FunctionEvalWithGraph
    """)
