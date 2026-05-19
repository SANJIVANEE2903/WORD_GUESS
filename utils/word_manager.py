# utils/word_manager.py

import random

WORDS = {

    "Programming": [
        "python",
        "developer",
        "database",
        "algorithm",
        "compiler"
    ],

    "Animals": [
        "tiger",
        "elephant",
        "giraffe",
        "penguin"
    ],

    "Countries": [
        "india",
        "canada",
        "brazil",
        "germany"
    ]
}


def get_random_word():

    category = random.choice(list(WORDS.keys()))

    word = random.choice(WORDS[category])

    return category, word