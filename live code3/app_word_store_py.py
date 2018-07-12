class WordStore:
    def __init__(self):
        with open("words.txt") as f:
            self._words = {line.strip() for line in f.readlines()}

    def contains(self, word):
        return word in self._words
