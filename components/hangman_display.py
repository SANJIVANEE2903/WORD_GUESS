# components/hangman_display.py

from kivymd.uix.label import MDLabel


class HangmanDisplay(MDLabel):

    stages = [

        "🙂",

        "😐",

        "😟",

        "😢",

        "😭",

        "💀"
    ]

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.halign = "center"

        self.font_style = "H1"

    def update_stage(self, attempts):

        index = 6 - attempts

        if index >= len(self.stages):

            index = len(self.stages) - 1

        self.text = self.stages[index]