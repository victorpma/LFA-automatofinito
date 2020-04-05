import json
from automato import Automato


def main():

    def readAutomato():
        with open('InsiraSeuAutomatoAqui/automato.json') as file:
            automatoJson = json.load(file)

        alphabet = automatoJson["alfabeto"]
        stateInitial = automatoJson["estadoInicial"]
        stateEnd = automatoJson["estadoFinal"]
        transictions = automatoJson["transicoes"]

        newAutomato = Automato(alphabet, stateInitial, stateEnd, transictions)
        newAutomato.populateTransictions()

        return newAutomato

    while True:
        print("----------------- MENU -----------------")
        print("ATENÇÃO: Antes de iniciar os testes, insira seu autômato na pasta 'InsiraSeuAutomatoAqui', lá possui um exemplo, mas caso queira testar com o exemplo base, fique à vontade ;)")
        print("\n1- Testar Autômato\n2- Minimizar Autômato\n3- Finalizar")

        optionInput = int(input("\nEscolha uma opção acima: "))

        if optionInput == 1:
            optionWordTest = input(
                "\nInforme uma palavra para testar o autômato: ")
            automato = readAutomato()
            automato.testAutomato(optionWordTest)
        else:
            print("Opção inválida, tente novamente!")
            break


if __name__ == "__main__":
    main()
