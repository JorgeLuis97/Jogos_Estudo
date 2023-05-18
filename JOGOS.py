import Advinhação
import Forca

print("**************************")
print("******Chose your Game*****")
print("**************************")

print("(1) Guess game , (2) Forca")

jogo = int(input("Escolha seu Jogo: "))


if jogo == 1:
    print("Jogando Guess game")
    Advinhação.jogar()
elif jogo == 2:
    print("Jogando Forca")
    Forca.jogar()
