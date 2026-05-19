# score.py

SCORE_FILE = "assets/highscore.txt"


def load_high_score():
    """
    Load high score from file
    """

    try:
        with open(SCORE_FILE, "r") as file:
            score = file.read()

            if score.strip() == "":
                return 0

            return int(score)

    except FileNotFoundError:
        return 0


def save_high_score(score):
    """
    Save high score to file
    """

    with open(SCORE_FILE, "w") as file:
        file.write(str(score))