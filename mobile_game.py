import random

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from words import words


class WordGame(BoxLayout):

    def __init__(self, **kwargs):

        super().__init__(orientation='vertical', spacing=15, padding=20, **kwargs)

        # =========================
        # GAME VARIABLES
        # =========================

        self.category = random.choice(list(words.keys()))

        self.secret_word = random.choice(words[self.category])

        self.guessed_letters = []

        self.attempts = 6

        self.hint_used = False

        # =========================
        # TITLE
        # =========================

        self.title = Label(
            text="🎮 WORD GUESS GAME",
            font_size=32,
            size_hint=(1, 0.15)
        )

        self.add_widget(self.title)

        # =========================
        # CATEGORY
        # =========================

        self.category_label = Label(
            text=f"📂 Category: {self.category}",
            font_size=24,
            size_hint=(1, 0.1)
        )

        self.add_widget(self.category_label)

        # =========================
        # WORD DISPLAY
        # =========================

        self.word_label = Label(
            text="",
            font_size=40,
            size_hint=(1, 0.2)
        )

        self.add_widget(self.word_label)

        # =========================
        # ATTEMPTS
        # =========================

        self.attempts_label = Label(
            text=f"❤️ Attempts Left: {self.attempts}",
            font_size=24,
            size_hint=(1, 0.1)
        )

        self.add_widget(self.attempts_label)

        # =========================
        # STATUS
        # =========================

        self.status_label = Label(
            text="Start Guessing...",
            font_size=22,
            size_hint=(1, 0.1)
        )

        self.add_widget(self.status_label)

        # =========================
        # INPUT
        # =========================

        self.input_box = TextInput(
            multiline=False,
            font_size=28,
            halign="center",
            size_hint=(1, 0.12)
        )

        self.add_widget(self.input_box)

        # =========================
        # BUTTON LAYOUT
        # =========================

        button_layout = BoxLayout(
            size_hint=(1, 0.15),
            spacing=10
        )

        # GUESS BUTTON
        self.guess_button = Button(
            text="GUESS",
            font_size=24,
            background_color=(0, 0.7, 0.3, 1)
        )

        self.guess_button.bind(on_press=self.process_guess)

        button_layout.add_widget(self.guess_button)

        # HINT BUTTON
        self.hint_button = Button(
            text="HINT",
            font_size=24,
            background_color=(1, 0.6, 0, 1)
        )

        self.hint_button.bind(on_press=self.use_hint)

        button_layout.add_widget(self.hint_button)

        self.add_widget(button_layout)

        # INITIAL DISPLAY
        self.update_display()

    # =====================================
    # UPDATE WORD DISPLAY
    # =====================================

    def update_display(self):

        display_word = ""

        for letter in self.secret_word:

            if letter in self.guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        self.word_label.text = display_word

        self.attempts_label.text = (
            f"❤️ Attempts Left: {self.attempts}"
        )

        # WIN CONDITION
        if "_" not in display_word:

            self.status_label.text = (
                f"🎉 YOU WON! Word: {self.secret_word}"
            )

            self.disable_game()

    # =====================================
    # PROCESS GUESS
    # =====================================

    def process_guess(self, instance):

        guess = self.input_box.text.lower().strip()

        self.input_box.text = ""

        if guess == "":
            return

        # FULL WORD GUESS
        if len(guess) > 1:

            if guess == self.secret_word:

                self.guessed_letters.extend(
                    self.secret_word
                )

                self.update_display()

            else:

                self.attempts -= 1

                self.status_label.text = (
                    "❌ Wrong word guess!"
                )

                self.check_game_over()

            return

        # VALIDATION
        if not guess.isalpha():

            self.status_label.text = (
                "⚠️ Letters only!"
            )

            return

        # ALREADY GUESSED
        if guess in self.guessed_letters:

            self.status_label.text = (
                "⚠️ Already guessed!"
            )

            return

        self.guessed_letters.append(guess)

        # CORRECT / WRONG
        if guess in self.secret_word:

            self.status_label.text = (
                "✅ Correct Guess!"
            )

        else:

            self.attempts -= 1

            self.status_label.text = (
                "❌ Wrong Guess!"
            )

        self.update_display()

        self.check_game_over()

    # =====================================
    # HINT SYSTEM
    # =====================================

    def use_hint(self, instance):

        if self.hint_used:

            self.status_label.text = (
                "⚠️ Hint already used!"
            )

            return

        hidden_letters = []

        for letter in self.secret_word:

            if letter not in self.guessed_letters:
                hidden_letters.append(letter)

        hint_letter = random.choice(hidden_letters)

        self.guessed_letters.append(hint_letter)

        self.hint_used = True

        self.status_label.text = (
            f"💡 Hint: {hint_letter}"
        )

        self.update_display()

    # =====================================
    # GAME OVER
    # =====================================

    def check_game_over(self):

        if self.attempts <= 0:

            self.word_label.text = self.secret_word

            self.status_label.text = (
                f"💀 GAME OVER! Word: {self.secret_word}"
            )

            self.disable_game()

    # =====================================
    # DISABLE GAME
    # =====================================

    def disable_game(self):

        self.guess_button.disabled = True

        self.hint_button.disabled = True

        self.input_box.disabled = True


class WordGameApp(App):

    def build(self):

        return WordGame()


WordGameApp().run()