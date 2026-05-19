# screens/home_screen.py

from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel

from components.custom_button import CustomButton


class HomeScreen(Screen):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        layout = MDBoxLayout(

            orientation="vertical",

            spacing=20,

            padding=30
        )

        title = MDLabel(

            text="🎮 WORD GUESS",

            halign="center",

            font_style="H3"
        )

        play_btn = CustomButton(

            text="PLAY"
        )

        play_btn.bind(
            on_release=self.start_game
        )

        settings_btn = CustomButton(

            text="SETTINGS"
        )

        layout.add_widget(title)

        layout.add_widget(play_btn)

        layout.add_widget(settings_btn)

        self.add_widget(layout)

    def start_game(self, instance):

        self.manager.current = "game"