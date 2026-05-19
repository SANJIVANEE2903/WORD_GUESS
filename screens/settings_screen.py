# screens/settings_screen.py

from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel


class SettingsScreen(Screen):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        label = MDLabel(

            text="⚙️ SETTINGS",

            halign="center",

            font_style="H3"
        )

        self.add_widget(label)