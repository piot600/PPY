# ZAD1
# numbers = input("Podaj liczby oddzielone przecinkami: ")
# numbers_list = numbers.split(",")
# mini = int(numbers_list[0])
# maxi = int(numbers_list[0])
#
# for i in numbers_list:
#     if int(i) > maxi:
#         maxi = int(i)
#     if int(i) < mini:
#         mini = int(i)
#
# print("max : " + str(maxi))
# print("min : " + str(mini))


# ZAD2
# import random
#
# cities = ["Warszawa", "Kraków", "Wrocław", "Łódź", "Poznań", "Gdańsk", "Szczecin", "Bydgoszcz", "Lublin", "Białystok"]
# mix_cities = []
# for i in range(len(cities)):
#     tmp = random.randint(0, len(cities) - 1)
#     mix_cities.append(cities[tmp])
#     cities.remove(cities[tmp])
#
# print(mix_cities)

# ZAD3
import getpass
import random

print("******PAPIER NOŻYCE KAMIEŃ******\n")
rounds = int(input("Podaj liczbe rund: "))
mode = int(input("Wybierz tryb gry 1) 1-osobowy 2) 2-osobowy : "))
game_list = ["PAPIER", "NOŻYCE", "KAMIEŃ"]
w = 0
l = 0
d = 0
if mode == 1:
    for i in range(rounds):
        print("------RUNDA " + str(i + 1) + "------")
        player = int(input("0)PAPIER 1)NOŻYCE 2)KAMIEŃ : "))
        computer = random.randint(0, 2)

        print("Gracz: " + game_list[player])
        print("Komputer: " + game_list[computer])
        if player == computer:
            print("REMIS!!!")
            d = d + 1
        elif (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
            print("WYGRYWA GRACZ!!!")
            w = w + 1
        else:
            print("PRZEGRYWASZ!!!")
            l = l + 1
        print("Wyniki [ wygrane-" + str(w) + " przegrane-" + str(l) + " remisy-" + str(d) + " ]\n")
elif mode == 2:
    player1 = input("Podaj nazwe pierwszego gracza: ")
    player2 = input("Podaj nazwe drugiego gracza: ")
    for i in range(rounds):
        print("------RUNDA " + str(i + 1) + "------")
        p1 = int(getpass.getpass(player1 + " : 0)PAPIER 1)NOŻYCE 2)KAMIEŃ : "))
        p2 = int(getpass.getpass(player2 + " : 0)PAPIER 1)NOŻYCE 2)KAMIEŃ : "))
        print(player1 + ": " + game_list[p1])
        print(player2 + ": " + game_list[p2])

        if p1 == p2:
            print("REMIS!!!")
            d = d + 1
        elif (p1 == 0 and p2 == 2) or (p1 == 1 and p2 == 0) or (p1 == 2 and p2 == 1):
            print("WYGRYWA "+player1+"!!!")
            w = w + 1
        else:
            print("WYGRYWA "+player2+"!!!")
            l = l + 1
        print("Wyniki [ "+player1+" wygrane-" + str(w) +" "+player2+" wygrane-" + str(l) + " remisy-" + str(d) + " ]\n")