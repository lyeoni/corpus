from pathlib import Path

class Corpus:
    def __init__(self, name):
        self.name = name
        self.corpus = []

    def __len__(self):
        return len(self.corpus)

    def __getitem__(self, i):
        return self.corpus[i]

    def __str__(self):
        s = f'{self.name}'
        return s
