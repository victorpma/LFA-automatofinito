from estado import Estado


class Automato:
    def __init__(self, alphabet, initialState, endState, transictions):
        self.__states = []
        self.__alphabet = alphabet
        self.__initialState = initialState
        self.__endState = endState
        self.__transictions = transictions

    @property
    def states(self):
        return self.__states

    def isEndState(self, state):
        if(state in self.__endState):
            return True
        else:
            return False

    def populateTransictions(self):
        for state, transiction in self.__transictions.items():
            newState = Estado(state, self.isEndState(state),
                              self.__alphabet, transiction)
            self.states.append(newState)

    def getStateByName(self, name):
        for state in self.__states:
            if(state.name == name):
                return state

    def isValidAlphabet(self, word):
        for letter in word:
            if letter not in self.__alphabet:
                return False
        return True

    def testAutomato(self, word):
        word = list(word)

        if(self.isValidAlphabet(word)):
            states = []
            endState = self.getStateByName(self.__initialState)

            states.append(endState.name)

            for letter in word:
                endState = self.getStateByName(endState.move(letter))
                states.append(endState.name)

            states = "; ".join(states)
            print("\nEstados: " + states)

            if endState.isEndState:
                print("A PALAVRA PERTENCE AO AUTÔMATO!")
            else:
                print("A PALAVRA NÃO PERTENCE AO AUTÔMATO!")
        else:
            print(
                "A PALAVRA NÃO PERTENCE AO ALFABETO DO AUTÔMATO :(")

    def __str__(self):
        transictions = []
        for x, y in self.__transictions.items():
            transiction = x + ":" + str(y)
            transictions.append(transiction)
        trancictions = "\n".join(transiction)
        return trancictions

    def __repr__(self):
        return self.__str__()
