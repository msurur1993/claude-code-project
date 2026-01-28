"""
SAT Question: Infinitely Many Solutions
=======================================

Question:
(12x + 28)/4 - s/13 = r(x - 8)

If s and r are constants, s > 0, and the equation has
infinitely many solutions, what is the value of s?

Answer: s = 403

To render:
    manim -pql infinitely_many_solutions.py InfinitelySolutionsQuestion

For high quality:
    manim -pqh infinitely_many_solutions.py InfinitelySolutionsQuestion
"""

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
# For better voice quality, uncomment:
# from manim_voiceover.services.elevenlabs import ElevenLabsService


class InfinitelySolutionsQuestion(VoiceoverScene):
    def construct(self):
        # Configure voice service
        self.set_speech_service(GTTSService(lang="en", tld="com"))

        # For ElevenLabs (better quality):
        # self.set_speech_service(ElevenLabsService(voice_name="Adam"))

        # Colors
        HIGHLIGHT = YELLOW
        ANSWER_COLOR = GREEN
        STEP_COLOR = BLUE

        # ========================================
        # INTRO: Show the question
        # ========================================

        title = Text("SAT Practice Question", font_size=32, color=YELLOW)
        title.to_edge(UP, buff=0.5)

        equation = MathTex(
            r"\frac{12x + 28}{4} - \frac{s}{13} = r(x - 8)",
            font_size=44
        )
        equation.next_to(title, DOWN, buff=0.6)

        question_text = Text(
            "If the equation has infinitely many solutions,\nwhat is the value of s?",
            font_size=28,
            line_spacing=1.3
        )
        question_text.next_to(equation, DOWN, buff=0.5)

        with self.voiceover(
            text="Let's solve this SAT question. We have the equation: 12x plus 28, all over 4, minus s over 13, equals r times x minus 8."
        ) as tracker:
            self.play(Write(title), run_time=0.5)
            self.play(Write(equation), run_time=tracker.duration - 0.5)

        with self.voiceover(
            text="We're told that s and r are constants, and the equation has infinitely many solutions. We need to find the value of s."
        ) as tracker:
            self.play(Write(question_text), run_time=tracker.duration)

        self.wait(0.5)

        # ========================================
        # KEY INSIGHT
        # ========================================

        with self.voiceover(
            text="Here's the key insight: An equation has infinitely many solutions when both sides are completely identical. That means the coefficients of x must match, and the constant terms must match."
        ) as tracker:
            self.play(
                FadeOut(title),
                FadeOut(question_text),
                equation.animate.to_edge(UP, buff=0.8),
                run_time=1
            )

            insight_box = Rectangle(
                width=10, height=1.2,
                color=YELLOW,
                fill_opacity=0.1
            )
            insight_text = Text(
                "Infinitely many solutions -> Both sides must be IDENTICAL",
                font_size=26,
                color=YELLOW
            )
            insight_group = VGroup(insight_box, insight_text)
            insight_group.next_to(equation, DOWN, buff=0.5)

            self.play(
                Create(insight_box),
                Write(insight_text),
                run_time=tracker.duration - 1
            )

        self.wait(0.3)

        # ========================================
        # STEP 1: Simplify left side
        # ========================================

        with self.voiceover(
            text="Step 1: Let's simplify the left side. We can split the fraction 12x plus 28 over 4."
        ) as tracker:
            self.play(FadeOut(insight_group), run_time=0.3)

            step1_label = Text("Step 1: Simplify the left side", font_size=26, color=STEP_COLOR)
            step1_label.next_to(equation, DOWN, buff=0.6).to_edge(LEFT, buff=1)

            self.play(Write(step1_label), run_time=tracker.duration - 0.3)

        left_original = MathTex(
            r"\frac{12x + 28}{4} - \frac{s}{13}",
            font_size=40
        )
        left_original.next_to(step1_label, DOWN, buff=0.4)

        with self.voiceover(
            text="12x divided by 4 is 3x. And 28 divided by 4 is 7."
        ) as tracker:
            self.play(Write(left_original), run_time=0.5)
            self.wait(tracker.duration - 0.5)

        left_simplified = MathTex(
            r"= 3x + 7 - \frac{s}{13}",
            font_size=40
        )
        left_simplified.next_to(left_original, DOWN, buff=0.3)

        with self.voiceover(
            text="So the left side simplifies to 3x plus 7 minus s over 13."
        ) as tracker:
            self.play(Write(left_simplified), run_time=tracker.duration)

        # ========================================
        # STEP 2: Expand right side
        # ========================================

        step2_label = Text("Step 2: Expand the right side", font_size=26, color=STEP_COLOR)
        step2_label.next_to(left_simplified, DOWN, buff=0.5).to_edge(LEFT, buff=1)

        with self.voiceover(
            text="Step 2: Now let's expand the right side. r times x minus 8 gives us r x minus 8 r."
        ) as tracker:
            self.play(Write(step2_label), run_time=0.5)

            right_expanded = MathTex(
                r"r(x - 8) = rx - 8r",
                font_size=40
            )
            right_expanded.next_to(step2_label, DOWN, buff=0.4)

            self.play(Write(right_expanded), run_time=tracker.duration - 0.5)

        # ========================================
        # STEP 3: Match coefficients
        # ========================================

        # Clear and reorganize
        with self.voiceover(
            text="Step 3: Now we match both sides. For infinitely many solutions, the coefficient of x on the left must equal the coefficient of x on the right."
        ) as tracker:
            # Move everything up
            old_content = VGroup(step1_label, left_original, left_simplified, step2_label, right_expanded)
            self.play(
                old_content.animate.scale(0.7).to_edge(UP, buff=0.5).shift(LEFT * 2),
                FadeOut(equation),
                run_time=0.8
            )
            self.wait(tracker.duration - 0.8)

        step3_label = Text("Step 3: Match coefficients", font_size=26, color=STEP_COLOR)
        step3_label.next_to(old_content, DOWN, buff=0.4).to_edge(LEFT, buff=1)

        # Show the comparison
        comparison = MathTex(
            r"3x + 7 - \frac{s}{13}", r"=", r"rx - 8r",
            font_size=38
        )
        comparison.next_to(step3_label, DOWN, buff=0.4)

        with self.voiceover(
            text="Looking at our simplified equation: 3x plus 7 minus s over 13 equals r x minus 8r."
        ) as tracker:
            self.play(Write(step3_label), run_time=0.3)
            self.play(Write(comparison), run_time=tracker.duration - 0.3)

        # Match x coefficients
        coeff_x = MathTex(
            r"\text{Coefficients of } x: \quad 3 = r",
            font_size=34,
            color=HIGHLIGHT
        )
        coeff_x.next_to(comparison, DOWN, buff=0.5)

        with self.voiceover(
            text="The coefficient of x on the left is 3. The coefficient of x on the right is r. So r must equal 3."
        ) as tracker:
            self.play(Write(coeff_x), run_time=tracker.duration)

        # Match constants
        coeff_const = MathTex(
            r"\text{Constants: } \quad 7 - \frac{s}{13} = -8r",
            font_size=34,
            color=HIGHLIGHT
        )
        coeff_const.next_to(coeff_x, DOWN, buff=0.3)

        with self.voiceover(
            text="The constant on the left is 7 minus s over 13. The constant on the right is negative 8r."
        ) as tracker:
            self.play(Write(coeff_const), run_time=tracker.duration)

        # ========================================
        # STEP 4: Solve for s
        # ========================================

        step4_label = Text("Step 4: Solve for s", font_size=26, color=STEP_COLOR)
        step4_label.next_to(coeff_const, DOWN, buff=0.5).to_edge(LEFT, buff=1)

        with self.voiceover(
            text="Step 4: Now we substitute r equals 3 into the constant equation."
        ) as tracker:
            self.play(Write(step4_label), run_time=tracker.duration)

        # Substitute r = 3
        solve1 = MathTex(
            r"7 - \frac{s}{13} = -8(3)",
            font_size=36
        )
        solve1.next_to(step4_label, DOWN, buff=0.4)

        with self.voiceover(
            text="7 minus s over 13 equals negative 8 times 3."
        ) as tracker:
            self.play(Write(solve1), run_time=tracker.duration)

        solve2 = MathTex(
            r"7 - \frac{s}{13} = -24",
            font_size=36
        )
        solve2.next_to(solve1, DOWN, buff=0.25)

        with self.voiceover(
            text="Negative 8 times 3 is negative 24."
        ) as tracker:
            self.play(Write(solve2), run_time=tracker.duration)

        solve3 = MathTex(
            r"-\frac{s}{13} = -24 - 7 = -31",
            font_size=36
        )
        solve3.next_to(solve2, DOWN, buff=0.25)

        with self.voiceover(
            text="Subtract 7 from both sides. Negative 24 minus 7 is negative 31."
        ) as tracker:
            self.play(Write(solve3), run_time=tracker.duration)

        solve4 = MathTex(
            r"\frac{s}{13} = 31",
            font_size=36
        )
        solve4.next_to(solve3, DOWN, buff=0.25)

        with self.voiceover(
            text="Multiply both sides by negative 1. So s over 13 equals 31."
        ) as tracker:
            self.play(Write(solve4), run_time=tracker.duration)

        # Final answer
        final_answer = MathTex(
            r"s = 31 \times 13 = 403",
            font_size=44,
            color=ANSWER_COLOR
        )
        final_answer.next_to(solve4, DOWN, buff=0.4)

        with self.voiceover(
            text="Finally, multiply both sides by 13. 31 times 13 equals 403."
        ) as tracker:
            self.play(Write(final_answer), run_time=tracker.duration)

        # Highlight final answer
        box = SurroundingRectangle(final_answer, color=ANSWER_COLOR, buff=0.15)

        with self.voiceover(
            text="Therefore, s equals 403. That's our answer!"
        ) as tracker:
            self.play(Create(box), run_time=0.5)

            answer_label = Text("Answer: s = 403", font_size=36, color=ANSWER_COLOR)
            answer_label.to_edge(DOWN, buff=0.5)
            self.play(FadeIn(answer_label, shift=UP), run_time=tracker.duration - 0.5)

        self.wait(2)


# Shorter version for TikTok/Shorts (under 60 seconds)
class InfinitelySolutionsShort(VoiceoverScene):
    """
    Condensed version for short-form content.
    Faster pacing, fewer pauses.
    """
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))

        # Quick intro
        equation = MathTex(
            r"\frac{12x + 28}{4} - \frac{s}{13} = r(x - 8)",
            font_size=42
        ).to_edge(UP, buff=1)

        with self.voiceover(
            text="Find s if this equation has infinitely many solutions."
        ) as tracker:
            self.play(Write(equation), run_time=tracker.duration)

        # Key insight
        with self.voiceover(
            text="Infinitely many solutions means both sides must be identical."
        ) as tracker:
            insight = Text("Both sides must be IDENTICAL", font_size=28, color=YELLOW)
            insight.next_to(equation, DOWN, buff=0.5)
            self.play(Write(insight), run_time=tracker.duration)

        # Simplify
        with self.voiceover(
            text="Simplify: left side becomes 3x plus 7 minus s over 13. Right side is rx minus 8r."
        ) as tracker:
            self.play(FadeOut(insight), run_time=0.2)

            simplified = MathTex(
                r"3x + 7 - \frac{s}{13} = rx - 8r",
                font_size=38
            )
            simplified.next_to(equation, DOWN, buff=0.6)
            self.play(Write(simplified), run_time=tracker.duration - 0.2)

        # Match coefficients
        with self.voiceover(
            text="Match x coefficients: r equals 3. Match constants: 7 minus s over 13 equals negative 24."
        ) as tracker:
            match1 = MathTex(r"r = 3", font_size=34, color=YELLOW)
            match2 = MathTex(r"7 - \frac{s}{13} = -24", font_size=34, color=YELLOW)
            matches = VGroup(match1, match2).arrange(DOWN, buff=0.3)
            matches.next_to(simplified, DOWN, buff=0.5)
            self.play(Write(matches), run_time=tracker.duration)

        # Solve
        with self.voiceover(
            text="Solving: s over 13 equals 31, so s equals 403!"
        ) as tracker:
            answer = MathTex(r"s = 403", font_size=48, color=GREEN)
            answer.next_to(matches, DOWN, buff=0.5)
            box = SurroundingRectangle(answer, color=GREEN, buff=0.15)

            self.play(Write(answer), run_time=tracker.duration * 0.6)
            self.play(Create(box), run_time=tracker.duration * 0.4)

        self.wait(1.5)


if __name__ == "__main__":
    print("""
    To render this video:

    # Full explanation (2-3 minutes):
    manim -pql infinitely_many_solutions.py InfinitelySolutionsQuestion

    # Short version for TikTok (~45 seconds):
    manim -pql infinitely_many_solutions.py InfinitelySolutionsShort

    # High quality for production:
    manim -pqh infinitely_many_solutions.py InfinitelySolutionsQuestion
    """)
