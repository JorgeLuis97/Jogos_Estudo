import random


def jogar():

    print("**************************")
    print("Welcome to this Guess Game")
    print("**************************")

    print("Fácil: 1")
    print("Normal: 2")
    print("Difícil: 3")
    numero = random.randrange(1, 101)
    facil = 10
    medio = 3
    dificil = 1
    pontos = 1000

    dificuldade = int(input("Escolha sua dificuldade: "))

    if dificuldade == 1:
        total_de_tentativas = facil
    elif dificuldade == 2:
        total_de_tentativas = medio
    elif dificuldade == 3:
        total_de_tentativas = dificil
    print(numero)

    for rodadas in range(1, total_de_tentativas + 1):
        print(f"Tentativas: {rodadas} de {total_de_tentativas}")
        chute = input("Digite um número entre 1 e 100: ")
        numero2 = int(chute)

        if numero2 < 1 or numero2 > 100:
            print("**************************************")
            print("!!!DIGITE UM NÚMERO ENTRE 1 E 100!!!!")
            print("**************************************")
            continue

        print(f"Você digitou {chute}")
        acertou = numero2 == numero
        maior = numero2 > numero
        menor = numero2 < numero

        if acertou:
            print("Você acertou!")
            print(f"Você fez {pontos} Pontos")
            print("FIM DO JOGO")
            break
        else:
            if maior:
                print("**************************")
                print("Você Errou seu chute foi maior que o número!")
                print("**************************")
            elif menor:
                print("**************************")
                print("Você Errou seu chute foi menor que o número!")
                print("**************************")
                pontos_perdidos = abs(numero - numero2)
                pontos = pontos - pontos_perdidos * 5


if __name__ == "__main__":
    jogar()
