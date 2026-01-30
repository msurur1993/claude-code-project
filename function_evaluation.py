"""
SAT Question: Function Evaluation (TikTok-ready)
================================================

Question:
The function f is defined by f(x) = 8x.
For what value of x does f(x) = 72?

Answer: x = 9

To render:
    manim -pql function_evaluation.py FunctionEvaluationShort
"""

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService


class FunctionEvaluationShort(VoiceoverScene):
    """
    TikTok-ready short video for function evaluation question.
    """
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))

        # Colors
        FUNCTION_COLOR = BLUE
        VALUE_COLOR = ORANGE
        ANSWER_COLOR = GREEN
        STEP_COLOR = YELLOW

        # ========================================
        # Scene 1: Show the function
        # ========================================

        title = Text("SAT Question", font_size=36, color=YELLOW)
        title.to_edge(UP, buff=0.5)

        function_def = MathTex(r"f(x) = 8x", font_size=56, color=FUNCTION_COLOR)
        function_def.next_to(title, DOWN, buff=0.6)

        with self.voiceover(
            text="The function f of x equals 8 x."
        ) as tracker:
            self.play(Write(title), run_time=0.3)
            self.play(Write(function_def), run_time=tracker.duration - 0.3)

        # ========================================
        # Scene 2: Show what we need to find
        # ========================================

        question = MathTex(r"f(x) = 72", font_size=48, color=VALUE_COLOR)
        question.next_to(function_def, DOWN, buff=0.5)

        find_text = Text("Find x = ?", font_size=32, color=WHITE)
        find_text.next_to(question, DOWN, buff=0.4)

        with self.voiceover(
            text="For what value of x does f of x equal 72?"
        ) as tracker:
            self.play(Write(question), run_time=0.5)
            self.play(Write(find_text), run_time=tracker.duration - 0.5)

        self.wait(0.3)

        # ========================================
        # Scene 3: Set up the equation
        # ========================================

        with self.voiceover(
            text="Since f of x equals 8 x, we substitute."
        ) as tracker:
            self.play(
                FadeOut(title),
                FadeOut(find_text),
                function_def.animate.to_edge(UP, buff=0.8),
                question.animate.move_to(ORIGIN + UP * 0.5),
                run_time=0.5
            )
            self.wait(tracker.duration - 0.5)

        # Show substitution
        equation = MathTex(r"8x = 72", font_size=56, color=STEP_COLOR)
        equation.next_to(question, DOWN, buff=0.5)

        with self.voiceover(
            text="8 x equals 72."
        ) as tracker:
            self.play(Write(equation), run_time=tracker.duration)

        # ========================================
        # Scene 4: Solve for x
        # ========================================

        solve_step = MathTex(r"x = \frac{72}{8}", font_size=56)
        solve_step.next_to(equation, DOWN, buff=0.4)

        with self.voiceover(
            text="Divide both sides by 8."
        ) as tracker:
            self.play(Write(solve_step), run_time=tracker.duration)

        # ========================================
        # Scene 5: Final answer
        # ========================================

        answer = MathTex(r"x = 9", font_size=72, color=ANSWER_COLOR)
        answer.next_to(solve_step, DOWN, buff=0.5)

        box = SurroundingRectangle(answer, color=ANSWER_COLOR, buff=0.15)

        with self.voiceover(
            text="x equals 9. That's our answer!"
        ) as tracker:
            self.play(Write(answer), run_time=0.4)
            self.play(Create(box), run_time=0.3)
            self.wait(tracker.duration - 0.7)

        # ========================================
        # Scene 6: Verification (quick)
        # ========================================

        verify = MathTex(r"f(9) = 8 \times 9 = 72 \checkmark", font_size=36, color=GREEN_A)
        verify.to_edge(DOWN, buff=1.5)

        with self.voiceover(
            text="Check: f of 9 equals 8 times 9, which is 72."
        ) as tracker:
            self.play(Write(verify), run_time=tracker.duration)

        # End card
        self.play(FadeOut(verify), run_time=0.3)

        follow_text = Text("Follow for daily SAT tips!", font_size=28, color=BLUE_B)
        follow_text.to_edge(DOWN, buff=0.5)

        self.play(FadeIn(follow_text, shift=UP), run_time=0.5)
        self.wait(1.5)


class FunctionEvaluationFull(VoiceoverScene):
    """
    Longer explanation version.
    """
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))

        # Colors
        HIGHLIGHT = YELLOW
        ANSWER_COLOR = GREEN

        # Title
        title = Text("SAT Practice Question", font_size=32, color=YELLOW)
        title.to_edge(UP, buff=0.5)

        # Question
        question_text = VGroup(
            Text("The function f is defined by", font_size=26),
            MathTex(r"f(x) = 8x", font_size=40, color=BLUE),
            Text("For what value of x does f(x) = 72?", font_size=26)
        ).arrange(DOWN, buff=0.3)
        question_text.next_to(title, DOWN, buff=0.5)

        with self.voiceover(
            text="The function f is defined by f of x equals 8 x. For what value of x does f of x equal 72?"
        ) as tracker:
            self.play(Write(title), run_time=0.3)
            self.play(Write(question_text), run_time=tracker.duration - 0.3)

        self.wait(0.5)

        # Explain the concept
        with self.voiceover(
            text="This is asking: what input gives us an output of 72?"
        ) as tracker:
            concept = Text("Input → f(x) = 8x → Output", font_size=24, color=GRAY_A)
            concept.next_to(question_text, DOWN, buff=0.5)
            self.play(Write(concept), run_time=tracker.duration)

        # Set up equation
        with self.voiceover(
            text="We set 8 x equal to 72 and solve for x."
        ) as tracker:
            self.play(FadeOut(concept), FadeOut(question_text), run_time=0.3)

            equation = MathTex(r"8x = 72", font_size=56, color=HIGHLIGHT)
            equation.move_to(ORIGIN)
            self.play(Write(equation), run_time=tracker.duration - 0.3)

        # Solve
        with self.voiceover(
            text="Divide both sides by 8."
        ) as tracker:
            step1 = MathTex(r"\frac{8x}{8} = \frac{72}{8}", font_size=48)
            step1.next_to(equation, DOWN, buff=0.5)
            self.play(Write(step1), run_time=tracker.duration)

        with self.voiceover(
            text="x equals 72 divided by 8, which is 9."
        ) as tracker:
            step2 = MathTex(r"x = 9", font_size=64, color=ANSWER_COLOR)
            step2.next_to(step1, DOWN, buff=0.5)
            box = SurroundingRectangle(step2, color=ANSWER_COLOR, buff=0.15)
            self.play(Write(step2), run_time=0.5)
            self.play(Create(box), run_time=tracker.duration - 0.5)

        # Verify
        with self.voiceover(
            text="Let's verify: f of 9 equals 8 times 9, which equals 72. Correct!"
        ) as tracker:
            verify = VGroup(
                MathTex(r"f(9) = 8(9) = 72", font_size=36),
                Text("✓ Correct!", font_size=28, color=GREEN)
            ).arrange(RIGHT, buff=0.5)
            verify.next_to(box, DOWN, buff=0.5)
            self.play(Write(verify), run_time=tracker.duration)

        self.wait(2)


if __name__ == "__main__":
    print("""
    To render:

    # Short TikTok version:
    manim -pql function_evaluation.py FunctionEvaluationShort

    # Full explanation:
    manim -pql function_evaluation.py FunctionEvaluationFull
    """)
