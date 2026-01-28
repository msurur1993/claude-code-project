"""
SAT Question: Percent Increase (TikTok-ready)
=============================================

Question:
A jacket originally costs $80. The price increases by 25%,
then a coupon takes 20% off the new price. What is the final price?

Answer: $80

To render:
    manim -pql percent_increase.py PercentIncreaseShort

For high quality:
    manim -pqh percent_increase.py PercentIncreaseShort
"""

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService


class PercentIncreaseShort(VoiceoverScene):
    """
    TikTok-ready short video (~15 seconds) for percent increase question.
    """
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))

        # Colors
        PRICE_COLOR = GREEN
        INCREASE_COLOR = RED
        DISCOUNT_COLOR = BLUE
        ANSWER_COLOR = YELLOW

        # ========================================
        # Scene 1: Show jacket + $80
        # ========================================

        # Jacket icon (simplified as a rectangle with hanger)
        jacket = VGroup(
            RoundedRectangle(height=1.5, width=1.2, corner_radius=0.1, color=BLUE_C, fill_opacity=0.7),
            Line(UP * 0.75 + LEFT * 0.3, UP * 1.1, color=WHITE),
            Line(UP * 0.75 + RIGHT * 0.3, UP * 1.1, color=WHITE),
            Arc(radius=0.2, start_angle=0, angle=PI, color=WHITE).move_to(UP * 1.1)
        )
        jacket.scale(0.8).to_edge(UP, buff=1)

        start_price = MathTex(r"\$80", font_size=72, color=PRICE_COLOR)
        start_price.next_to(jacket, DOWN, buff=0.3)

        start_label = Text("Start = 80", font_size=32, color=WHITE)
        start_label.next_to(start_price, DOWN, buff=0.4)

        with self.voiceover(
            text="Jacket is eighty dollars."
        ) as tracker:
            self.play(
                FadeIn(jacket),
                Write(start_price),
                run_time=tracker.duration * 0.7
            )
            self.play(Write(start_label), run_time=tracker.duration * 0.3)

        # ========================================
        # Scene 2: +25% increase
        # ========================================

        increase_label = Text("+25%", font_size=36, color=INCREASE_COLOR)
        increase_label.next_to(start_price, RIGHT, buff=0.5)

        multiplier1 = MathTex(r"\times 1.25", font_size=40, color=INCREASE_COLOR)
        multiplier1.next_to(start_label, DOWN, buff=0.3)

        calc1 = MathTex(r"80 \times 1.25 = 100", font_size=40)
        calc1.next_to(multiplier1, DOWN, buff=0.3)

        new_price = MathTex(r"\$100", font_size=56, color=INCREASE_COLOR)
        new_price.move_to(start_price.get_center())

        with self.voiceover(
            text="A 25% increase means multiply by 1.25, so it becomes one hundred."
        ) as tracker:
            self.play(Write(increase_label), run_time=0.3)
            self.play(Write(multiplier1), run_time=0.5)

            # Circle the 1.25
            circle_mult = SurroundingRectangle(multiplier1, color=INCREASE_COLOR, buff=0.1)
            self.play(Create(circle_mult), run_time=0.3)

            self.play(Write(calc1), run_time=tracker.duration - 1.5)

            # Transform price
            self.play(
                FadeOut(start_price),
                FadeOut(circle_mult),
                run_time=0.2
            )
            self.play(FadeIn(new_price, scale=1.2), run_time=0.2)

        # ========================================
        # Scene 3: 20% off coupon
        # ========================================

        # Coupon
        coupon = VGroup(
            RoundedRectangle(height=0.6, width=1.5, corner_radius=0.1,
                           color=DISCOUNT_COLOR, fill_opacity=0.8),
            Text("20% OFF", font_size=20, color=WHITE)
        )
        coupon[1].move_to(coupon[0].get_center())
        coupon.next_to(increase_label, DOWN, buff=0.2)

        multiplier2 = MathTex(r"\times 0.80", font_size=40, color=DISCOUNT_COLOR)
        multiplier2.next_to(calc1, DOWN, buff=0.3)

        calc2 = MathTex(r"100 \times 0.80 = 80", font_size=40)
        calc2.next_to(multiplier2, DOWN, buff=0.3)

        with self.voiceover(
            text="Then 20% off means multiply by 0.8, so it goes back to eighty."
        ) as tracker:
            self.play(FadeIn(coupon, shift=DOWN), run_time=0.3)
            self.play(Write(multiplier2), run_time=0.4)

            # Show percent to decimal conversion
            cross = Cross(coupon, stroke_width=3, color=RED)
            self.play(Create(cross), run_time=0.2)

            self.play(Write(calc2), run_time=tracker.duration - 1.2)
            self.wait(0.3)

        # ========================================
        # Scene 4: Answer
        # ========================================

        # Clear middle section
        to_fade = VGroup(start_label, increase_label, multiplier1, calc1,
                        coupon, cross, multiplier2, calc2)

        final_price = MathTex(r"\$80", font_size=72, color=ANSWER_COLOR)
        final_price.move_to(new_price.get_center())

        answer_text = Text("Answer: $80", font_size=44, color=ANSWER_COLOR)
        answer_text.next_to(final_price, DOWN, buff=0.5)

        answer_box = SurroundingRectangle(answer_text, color=ANSWER_COLOR, buff=0.15)

        with self.voiceover(
            text="Quick check: 1.25 times 0.8 is exactly one."
        ) as tracker:
            self.play(
                FadeOut(to_fade),
                FadeOut(new_price),
                run_time=0.3
            )
            self.play(FadeIn(final_price, scale=1.3), run_time=0.3)
            self.play(
                Write(answer_text),
                Create(answer_box),
                run_time=tracker.duration - 0.6
            )

        # ========================================
        # Scene 5: Shortcut trick
        # ========================================

        shortcut = MathTex(r"1.25 \times 0.80 = 1.00", font_size=36, color=WHITE)
        shortcut.next_to(answer_box, DOWN, buff=0.4)

        shortcut2 = MathTex(r"80 \times 1.00 = 80", font_size=36, color=WHITE)
        shortcut2.next_to(shortcut, DOWN, buff=0.2)

        tip = Text("Percent changes use multipliers!", font_size=24, color=GRAY_A)
        tip.to_edge(DOWN, buff=0.3)

        with self.voiceover(
            text="Final price is eighty dollars."
        ) as tracker:
            self.play(Write(shortcut), run_time=0.4)
            self.play(Write(shortcut2), run_time=0.3)
            self.play(FadeIn(tip, shift=UP), run_time=tracker.duration - 0.7)

        # End card
        follow_text = Text("Follow for daily SAT tips!", font_size=28, color=BLUE_B)
        follow_text.to_edge(DOWN, buff=0.5)

        self.play(
            ReplacementTransform(tip, follow_text),
            run_time=0.5
        )

        self.wait(1.5)


class PercentIncreaseFull(VoiceoverScene):
    """
    Longer explanation version with more detail.
    """
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))

        # Colors
        HIGHLIGHT = YELLOW
        ANSWER_COLOR = GREEN
        STEP_COLOR = BLUE

        # ========================================
        # INTRO: Show the question
        # ========================================

        title = Text("SAT Practice Question", font_size=32, color=YELLOW)
        title.to_edge(UP, buff=0.5)

        question = Text(
            "A jacket costs $80.\n"
            "Price increases by 25%,\n"
            "then a 20% coupon is applied.\n"
            "What is the final price?",
            font_size=28,
            line_spacing=1.3
        )
        question.next_to(title, DOWN, buff=0.5)

        options = VGroup(
            Text("A) $80", font_size=28),
            Text("B) $76", font_size=28),
            Text("C) $90", font_size=28),
            Text("D) $96", font_size=28),
        ).arrange(RIGHT, buff=0.8)
        options.next_to(question, DOWN, buff=0.5)

        with self.voiceover(
            text="A jacket originally costs 80 dollars. The price increases by 25 percent, then a coupon takes 20 percent off. What's the final price?"
        ) as tracker:
            self.play(Write(title), run_time=0.4)
            self.play(Write(question), run_time=tracker.duration - 0.8)
            self.play(Write(options), run_time=0.4)

        self.wait(0.3)

        # ========================================
        # STEP 1: Calculate 25% increase
        # ========================================

        with self.voiceover(
            text="Step 1: A 25 percent increase means we multiply by 1.25."
        ) as tracker:
            self.play(
                FadeOut(question),
                FadeOut(options),
                run_time=0.3
            )

            step1 = Text("Step 1: 25% Increase", font_size=28, color=STEP_COLOR)
            step1.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=1)
            self.play(Write(step1), run_time=0.4)

            calc1 = MathTex(r"80 \times 1.25 = 100", font_size=42)
            calc1.next_to(step1, DOWN, buff=0.4)
            self.play(Write(calc1), run_time=tracker.duration - 0.7)

        # ========================================
        # STEP 2: Calculate 20% off
        # ========================================

        with self.voiceover(
            text="Step 2: 20 percent off means we keep 80 percent, so multiply by 0.80."
        ) as tracker:
            step2 = Text("Step 2: 20% Off", font_size=28, color=STEP_COLOR)
            step2.next_to(calc1, DOWN, buff=0.5).to_edge(LEFT, buff=1)
            self.play(Write(step2), run_time=0.4)

            calc2 = MathTex(r"100 \times 0.80 = 80", font_size=42)
            calc2.next_to(step2, DOWN, buff=0.4)
            self.play(Write(calc2), run_time=tracker.duration - 0.4)

        # ========================================
        # KEY INSIGHT: Net multiplier
        # ========================================

        with self.voiceover(
            text="Here's the trick: The net multiplier is 1.25 times 0.80, which equals exactly 1. So the price returns to where it started!"
        ) as tracker:
            insight_box = Rectangle(width=8, height=1.2, color=HIGHLIGHT, fill_opacity=0.1)
            insight_text = MathTex(
                r"\text{Net: } 1.25 \times 0.80 = 1.00",
                font_size=36,
                color=HIGHLIGHT
            )
            insight = VGroup(insight_box, insight_text)
            insight_text.move_to(insight_box.get_center())
            insight.next_to(calc2, DOWN, buff=0.5)

            self.play(
                Create(insight_box),
                Write(insight_text),
                run_time=tracker.duration
            )

        # ========================================
        # FINAL ANSWER
        # ========================================

        final = MathTex(r"\text{Final Price: } \$80", font_size=48, color=ANSWER_COLOR)
        final.next_to(insight, DOWN, buff=0.5)
        box = SurroundingRectangle(final, color=ANSWER_COLOR, buff=0.15)

        with self.voiceover(
            text="The final price is 80 dollars. Answer is A!"
        ) as tracker:
            self.play(Write(final), run_time=0.5)
            self.play(Create(box), run_time=0.3)

            # Highlight correct answer
            correct = Text("A) $80", font_size=32, color=ANSWER_COLOR)
            correct.to_edge(DOWN, buff=0.5)
            self.play(FadeIn(correct, shift=UP), run_time=tracker.duration - 0.8)

        self.wait(2)


if __name__ == "__main__":
    print("""
    To render this video:

    # Short TikTok version (~15 seconds):
    manim -pql percent_increase.py PercentIncreaseShort

    # Full explanation version:
    manim -pql percent_increase.py PercentIncreaseFull

    # High quality:
    manim -pqh percent_increase.py PercentIncreaseShort
    """)
