# utils/game_logic.py

class GameLogic:

    def __init__(self, secret_word):

        self.secret_word = secret_word

        self.guessed_letters = []

        self.attempts = 6

    def guess_letter(self, letter):

        if letter in self.guessed_letters:

            return "already"

        self.guessed_letters.append(letter)

        if letter in self.secret_word:

            return "correct"

        self.attempts -= 1

        return "wrong"

    def get_display_word(self):

        display = ""

        for letter in self.secret_word:

            if letter in self.guessed_letters:

                display += letter + " "

            else:

                display += "_ "

        return display

    def is_won(self):

        return "_" not in self.get_display_word()

    def is_lost(self):

        return self.attempts <= 0