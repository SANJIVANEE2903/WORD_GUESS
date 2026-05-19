# main.py

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

from screens.home_screen import HomeScreen
from screens.game_screen import GameScreen
from screens.game_over_screen import GameOverScreen
from screens.settings_screen import SettingsScreen


class WordGuessApp(MDApp):

    def build(self):

        self.theme_cls.theme_style = "Dark"

        self.theme_cls.primary_palette = "Blue"

        sm = ScreenManager()

        sm.add_widget(HomeScreen(name="home"))

        sm.add_widget(GameScreen(name="game"))

        sm.add_widget(GameOverScreen(name="gameover"))

        sm.add_widget(SettingsScreen(name="settings"))

        return sm


WordGuessApp().run()