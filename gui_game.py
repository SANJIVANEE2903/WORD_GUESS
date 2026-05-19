import random
import tkinter as tk
from tkinter import messagebox

from words import words
from score import load_high_score, save_high_score


# =========================================
# MAIN WINDOW
# =========================================

root = tk.Tk()

root.title("Word Guessing Game")

root.geometry("900x700")

root.config(bg="#121212")

root.resizable(False, False)


# =========================================
# GAME VARIABLES
# =========================================

category = random.choice(list(words.keys()))
secret_word = random.choice(words[category])

guessed_letters = []

attempts = 6

hint_used = False

score = 0

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
# FUNCTIONS
# =========================================

def update_display():

    display_word = ""

    for letter in secret_word:

        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    word_label.config(text=display_word)

    attempts_label.config(
        text=f"❤️ Attempts Left: {attempts}"
    )

    hangman_label.config(
        text=hangman_stages[6 - attempts]
    )

    high_score_label.config(
        text=f"🏆 High Score: {high_score}"
    )

    # WIN CONDITION
    if "_" not in display_word:

        end_game(True)


def end_game(win):

    global score
    global high_score

    input_box.config(state="disabled")

    guess_button.config(state="disabled")

    hint_button.config(state="disabled")

    if win:

        score = attempts * 10

        if hint_used:
            score -= 5

        result = (
            f"🎉 Congratulations!\n\n"
            f"You guessed the word:\n{secret_word}\n\n"
            f"⭐ Score: {score}"
        )

        if score > high_score:

            high_score = score

            save_high_score(score)

            result += "\n\n🏆 NEW HIGH SCORE!"

        messagebox.showinfo(
            "YOU WIN",
            result
        )

    else:

        messagebox.showerror(
            "GAME OVER",
            f"💀 The word was:\n{secret_word}"
        )


def process_guess():

    global attempts

    guess = input_box.get().lower().strip()

    input_box.delete(0, tk.END)

    if guess == "":
        return

    # HINT
    if guess == "hint":

        use_hint()
        return

    # FULL WORD GUESS
    if len(guess) > 1:

        if guess == secret_word:

            guessed_letters.extend(secret_word)

            update_display()

        else:

            attempts -= 1

            status_label.config(
                text="❌ Wrong word guess!"
            )

            update_display()

        if attempts == 0:
            end_game(False)

        return

    # VALIDATION
    if not guess.isalpha():

        status_label.config(
            text="⚠️ Enter letters only!"
        )

        return

    # ALREADY GUESSED
    if guess in guessed_letters:

        status_label.config(
            text="⚠️ Letter already guessed!"
        )

        return

    guessed_letters.append(guess)

    # CORRECT / WRONG
    if guess in secret_word:

        status_label.config(
            text="✅ Correct Guess!"
        )

    else:

        attempts -= 1

        status_label.config(
            text="❌ Wrong Guess!"
        )

    update_display()

    if attempts == 0:

        end_game(False)


def use_hint():

    global hint_used

    if hint_used:

        status_label.config(
            text="⚠️ Hint already used!"
        )

        return

    hidden_letters = []

    for letter in secret_word:

        if letter not in guessed_letters:
            hidden_letters.append(letter)

    hint_letter = random.choice(hidden_letters)

    guessed_letters.append(hint_letter)

    hint_used = True

    status_label.config(
        text=f"💡 Hint Letter: {hint_letter}"
    )

    update_display()


# =========================================
# TITLE
# =========================================

title_label = tk.Label(
    root,
    text="🎮 WORD GUESSING GAME",
    font=("Arial", 28, "bold"),
    bg="#121212",
    fg="white"
)

title_label.pack(pady=15)


# =========================================
# CATEGORY
# =========================================

category_label = tk.Label(
    root,
    text=f"📂 Category: {category}",
    font=("Arial", 18),
    bg="#121212",
    fg="#00ffcc"
)

category_label.pack()


# =========================================
# HIGH SCORE
# =========================================

high_score_label = tk.Label(
    root,
    text=f"🏆 High Score: {high_score}",
    font=("Arial", 16),
    bg="#121212",
    fg="gold"
)

high_score_label.pack(pady=10)


# =========================================
# HANGMAN
# =========================================

hangman_label = tk.Label(
    root,
    text=hangman_stages[0],
    font=("Courier", 18),
    bg="#121212",
    fg="white",
    justify="left"
)

hangman_label.pack(pady=10)


# =========================================
# WORD DISPLAY
# =========================================

word_label = tk.Label(
    root,
    text="",
    font=("Arial", 34, "bold"),
    bg="#121212",
    fg="white"
)

word_label.pack(pady=25)


# =========================================
# ATTEMPTS
# =========================================

attempts_label = tk.Label(
    root,
    text=f"❤️ Attempts Left: {attempts}",
    font=("Arial", 18),
    bg="#121212",
    fg="#ff6666"
)

attempts_label.pack(pady=10)


# =========================================
# INPUT LABEL
# =========================================

input_label = tk.Label(
    root,
    text="Enter Letter or Full Word",
    font=("Arial", 16),
    bg="#121212",
    fg="white"
)

input_label.pack(pady=5)


# =========================================
# INPUT BOX
# =========================================

input_box = tk.Entry(
    root,
    font=("Arial", 24),
    justify="center",
    width=20,
    bg="white",
    fg="black"
)

input_box.pack(pady=15)

input_box.focus()


# =========================================
# BUTTON FRAME
# =========================================

button_frame = tk.Frame(
    root,
    bg="#121212"
)

button_frame.pack(pady=10)


# =========================================
# GUESS BUTTON
# =========================================

guess_button = tk.Button(
    button_frame,
    text="GUESS",
    font=("Arial", 16, "bold"),
    bg="#00cc66",
    fg="white",
    width=12,
    height=2,
    command=process_guess
)

guess_button.grid(row=0, column=0, padx=15)


# =========================================
# HINT BUTTON
# =========================================

hint_button = tk.Button(
    button_frame,
    text="HINT",
    font=("Arial", 16, "bold"),
    bg="#ff9900",
    fg="white",
    width=12,
    height=2,
    command=use_hint
)

hint_button.grid(row=0, column=1, padx=15)


# =========================================
# STATUS LABEL
# =========================================

status_label = tk.Label(
    root,
    text="Start Guessing...",
    font=("Arial", 16),
    bg="#121212",
    fg="#cccccc"
)

status_label.pack(pady=20)


# =========================================
# ENTER KEY SUPPORT
# =========================================

root.bind(
    "<Return>",
    lambda event: process_guess()
)


# =========================================
# INITIAL DISPLAY
# =========================================

update_display()


# =========================================
# START GUI
# =========================================

root.mainloop()