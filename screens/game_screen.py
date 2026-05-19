# screens/game_screen.py

from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel

from components.custom_button import CustomButton
from components.word_display import WordDisplay
from components.hangman_display import HangmanDisplay

from utils.word_manager import get_random_word
from utils.game_logic import GameLogic


class GameScreen(Screen):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        category, word = get_random_word()

        self.logic = GameLogic(word)

        layout = MDBoxLayout(

            orientation="vertical",

            spacing=20,

            padding=20
        )

        self.category_label = MDLabel(

            text=f"📂 {category}",

            halign="center"
        )

        self.hangman = HangmanDisplay()

        self.word_display = WordDisplay(

            text=self.logic.get_display_word()
        )

        self.status = MDLabel(

            text="Start Guessing",

            halign="center"
        )

        self.input_box = MDTextField(

            hint_text="Enter Letter"
        )

        guess_btn = CustomButton(

            text="GUESS"
        )

        guess_btn.bind(
            on_release=self.process_guess
        )

        layout.add_widget(self.category_label)

        layout.add_widget(self.hangman)

        layout.add_widget(self.word_display)

        layout.add_widget(self.status)

        layout.add_widget(self.input_box)

        layout.add_widget(guess_btn)

        self.add_widget(layout)

    def process_guess(self, instance):

        guess = self.input_box.text.lower()

        self.input_box.text = ""

        if guess == "":

            return

        result = self.logic.guess_letter(
            guess
        )

        if result == "correct":

            self.status.text = "✅ Correct"

        elif result == "wrong":

            self.status.text = "❌ Wrong"

        else:

            self.status.text = "⚠️ Already guessed"

        self.word_display.text = (
            self.logic.get_display_word()
        )

        self.hangman.update_stage(
            self.logic.attempts
        )

        if self.logic.is_won():

            self.manager.current = "gameover"

        if self.logic.is_lost():

            self.manager.current = "gameover"