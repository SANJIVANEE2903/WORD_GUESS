# screens/game_over_screen.py

from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel


class GameOverScreen(Screen):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        label = MDLabel(

            text="🎮 GAME OVER",

            halign="center",

            font_style="H2"
        )

        self.add_widget(label)