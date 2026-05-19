# components/custom_button.py

from kivymd.uix.button import MDRaisedButton


class CustomButton(MDRaisedButton):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.font_size = "18sp"

        self.size_hint = (1, None)

        self.height = "50dp"

        self.radius = [20]