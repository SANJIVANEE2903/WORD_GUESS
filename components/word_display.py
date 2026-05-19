# components/word_display.py

from kivymd.uix.label import MDLabel


class WordDisplay(MDLabel):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.halign = "center"

        self.font_style = "H3"

        self.bold = True