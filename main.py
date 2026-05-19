# main.py

import random

from words import words
from score import load_high_score, save_high_score


# =========================================
# SELECT RANDOM CATEGORY & WORD
# =========================================

category = random.choice(list(words.keys()))
secret_word = random.choice(words[category])


# =========================================
# GAME VARIABLES
# =========================================

guessed_letters = []

attempts = 6

score = 0

hint_used = False

game_won = False


# =========================================
# LOAD HIGH SCORE
# =========================================

high_score = load_high_score()


# =========================================
# HANGMAN STAGES
# =========================================

hangman_stages = [

    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,

    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,

    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,

    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,

    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,

    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,

    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]


# =========================================
# WELCOME SCREEN
# =========================================

print("\n🎮 WORD GUESSING GAME")
print("=================================")

print(f"\n📂 Category: {category}")
print(f"🏆 High Score: {high_score}")

print("\n🎯 Rules:")
print("• Guess one letter at a time")
print("• OR guess the full word")
print("• Type 'hint' for one free hint")
print("• Hint reduces score")

print("\n=================================")


# =========================================
# MAIN GAME LOOP
# =========================================

while attempts > 0:

    # Show Hangman
    print(hangman_stages[6 - attempts])

    # =====================================
    # DISPLAY CURRENT WORD
    # =====================================

    display_word = ""

    for letter in secret_word:

        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\n📝 Word:", display_word)

    # =====================================
    # WIN CONDITION
    # =====================================

    if "_" not in display_word:

        game_won = True

        score = attempts * 10

        if hint_used:
            score -= 5

        break

    print(f"\n❤️ Attempts Left: {attempts}")

    # =====================================
    # USER INPUT
    # =====================================

    guess = input(
        "\n🔤 Enter letter / word / 'hint': "
    ).lower().strip()

    # =====================================
    # HINT SYSTEM
    # =====================================

    if guess == "hint":

        if hint_used:

            print("\n⚠️ Hint already used!")

        else:

            hidden_letters = []

            for letter in secret_word:

                if letter not in guessed_letters:
                    hidden_letters.append(letter)

            hint_letter = random.choice(hidden_letters)

            guessed_letters.append(hint_letter)

            hint_used = True

            print(f"\n💡 Hint Letter Revealed: {hint_letter}")

        continue

    # =====================================
    # INPUT VALIDATION
    # =====================================

    if not guess.isalpha():

        print("\n⚠️ Enter alphabet letters only.")
        continue

    # =====================================
    # FULL WORD GUESS
    # =====================================

    if len(guess) > 1:

        if guess == secret_word:

            guessed_letters.extend(secret_word)

            game_won = True

            score = attempts * 10

            if hint_used:
                score -= 5

            print("\n🎉 AMAZING!")
            print("You guessed the full word!")

            break

        else:

            print("\n❌ Wrong word guess!")
            attempts -= 1

        continue

    # =====================================
    # ALREADY GUESSED
    # =====================================

    if guess in guessed_letters:

        print("\n⚠️ Letter already guessed.")
        continue

    # =====================================
    # SAVE LETTER
    # =====================================

    guessed_letters.append(guess)

    # =====================================
    # CORRECT / WRONG GUESS
    # =====================================

    if guess in secret_word:

        print("\n✅ Correct Guess!")

    else:

        print("\n❌ Wrong Guess!")
        attempts -= 1


# =========================================
# FINAL RESULT
# =========================================

if game_won:

    print(hangman_stages[6 - attempts])

    print("\n🎉 CONGRATULATIONS!")
    print(f"✅ The word was: {secret_word}")

    print(f"\n⭐ Your Score: {score}")

    # Save High Score
    if score > high_score:

        print("\n🏆 NEW HIGH SCORE!")

        save_high_score(score)

else:

    print(hangman_stages[6])

    print("\n💀 GAME OVER")
    print(f"📌 The word was: {secret_word}")

print("\n=================================")
print("🎮 Thanks for Playing!")
print("=================================")