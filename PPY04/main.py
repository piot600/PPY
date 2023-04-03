# ZAD1
#
# def panels(floor_length, floor_width, panel_length, panel_width, amount):
#     fsize = floor_length * floor_width
#     psize = panel_length * panel_width
#     panel_amount = fsize / psize
#     amount = panel_amount / amount
#     if amount - int(amount) > 0:
#         return int(amount) + 1
#     return int(amount)
#
#
# fl = float(input("Podaj długość podłogi: "))
# fw = float(input("Podaj szerokość podłogi: "))
# pl = float(input("Podaj długość panela: "))
# pw = float(input("Podaj szerokość panela: "))
# a = float(input("Podaj liczbe paneli w opakowaniu: "))
# print(panels(fl, fw, pl, pw, a))

# ZAD2
#
# def isPrime2(*numbers):
#     print("Czy liczba pierwsza")
#     for n in numbers:
#         n = int(n)
#         isPrime = True
#         if n < 2:
#             isPrime = False
#         else:
#             for i in range(2, int(n/2+1)):
#                 if n % i == 0:
#                     isPrime = False
#         state = "is prime number" if isPrime else "is not prime"
#         print(f"{n} {state}")
#
#
# numbers = input("Wprowadz liczby oddzielone spacja: ")
# isPrime2(*numbers.split())


# ord()
# chr()

#ZAD3
# def cezar(message, shift, alphabet):
#     message = message.lower()
#     result = ""
#
#     for i in message:
#         if i in alphabet:
#             index = alphabet.index(i)
#             shifted_index = (index + shift) % len(alphabet)
#             result += alphabet[shifted_index]
#         else:
#             result += i
#     return result
#
#
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# alphabet_pol = "aąbcdeęfghijklmnoprstuwzźż"
# print(cezar("The Project Gutenberg eBook of Ali ce’s Adventures in Wonderland, by Lewis Carroll", 2, alphabet))
