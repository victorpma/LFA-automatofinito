class Estado:
    def __init__(self, name, state, alphabet, transiction):
        self.name = name
        self.isEndState = state
        self.alphabet = alphabet
        self.transiction = transiction

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def move(self, letter):
        return self.transiction[letter]
