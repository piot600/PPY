# Lista1

'''
UWAGA! Nie należy zmieniać nazw funkcji, oraz wartości zmiennych podanych w pliku
poza wartościami ze stringiem "PODAJ WYNIK" - w tych zmiennych należy przechowywać wynik
dotyczący poszczególnych zadań w_1, w_2 ... w_6.

Ciało funkcji wpisujemy w kodzie zamiast "pass".

Wyniki z każdego zadania powinny wyświetlać się w jednej linijce.
Nie należy wyświetlań nic poza wynikiem działania kodu z poszczególnych zadań
w kolejności tak jak w pliku.
Plik należy zapisać w postaci: imie_nazwisko_lista1.py
'''

import random

# 1. Ile unikatowych elementów znajduje się w liście:
# 1 pkt
lista_1 = [0, 7, 8, 3, 3, 0, 7, 0, 3]
uniq_el = set(lista_1)
w_1 = len(uniq_el)
print(w_1)

# 2. Napisz kod, który podmieni losowy znak ze stringa
s_2 = "ala ma kota"
result = ""
rand_index = random.randint(0, len(s_2) - 1)
for i in range(len(s_2)):
    if i == rand_index:
        result += '0'
    else:
        result += s_2[i]

# na '0':
# 2 pkt

w_2 = result
print(w_2)

# 3. Napisz kod który podmieni z lista_3 język programowania R na JS, następnie wyświetl podmieniony JS.
# Przed JS nadal musi znajdować się python w strukturze takiego samego typu jak w przykladowej lista_3.
# 2pkt
lista_3 = [[{1: 'java', 0: ('python', 'R')}, 'c++'], ['word', 'excel']]
tmp_list = list(lista_3[0][0][0])
tmp_list[1] = 'JS'
lista_3[0][0][0] = tuple(tmp_list)
w_3 = lista_3
print(w_3)

# 4. Jakiego typu dane z poniższych nie mogą być kluczami słownika?
# boolean,float,int,string,tuple,list,set. Odpowiedź umieśc w stringu w_4
# 1 pkt

w_4 = "list, set"
print(w_4)

# 5. Dla stringa wypisz
# ile razy pojawił się dany znak, w kolejności alfabetycznej.
# Użyj słownika - wynik również ma być słownikiem.
# Sprawdzamy tylko te znaki, które występują w podanym stringu.
# 2 pkt

s_5 = "ala ma kota imie ma macko"
dictionary = {}
chars_list = []

for i in range(len(s_5)):
    chars_list.append(s_5[i])

chars_list.sort()

for i in range(len(s_5)):
    dictionary[chars_list[i]] = 0

for i in range(len(s_5)):
    dictionary[chars_list[i]] += 1

w_5 = dictionary
print(w_5)

# 6. Napisz kod który sprawdzi, czy w poprzednim stringu s_5,
# jakikolwiek znak wystąpił dokładnie 3 razy. Wyświetl Tak jeżeli wystąpił,
# Nie jeżeli nie wystąpił.
# 1 pkt

tmp = False
for i in dictionary:
    if dictionary[i] == 3:
        tmp = True

w_6 = "Tak" if tmp else "Nie"
print(w_6)


# 7. Napisz funkcję sprawdzającą czy podane słowa/zdania są palindromem
# i zwróci True lub False ( jest/ nie jest).
# Pomiń znaki nie będące literami, wielkość liter nie ma znaczenia
# 3pkt

def palindrom(s):
    word = ''.join(filter(str.isalpha, s)).lower()
    return word == word[::-1]


s_7_1 = "Nowy Targ, góry, Zakopane – na pokazy róg, graty won"
print(palindrom(s_7_1))


# 8. Napisz funkcję, która zwróci
# wszystkie liczby od 1 do n w jednym stringu rozdzielone przecinkami,
# jednak jeżeli liczba jest podzielna przez:
# trzy – zamiast liczby mamy „Fizz”,
# pięć – zamiast liczby mamy „Buzz”,
# trzy i pięć zamiast liczby mamy „FizzBuzz”.
# wszystkie liczby/słowa mają zostać zwróćone w jednej linii, oraz być rozdzielone przecinkiem
# BEZ spacji
# 2 pkt

def fizzbuzz(n):
    result = ""
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            result += "FizzBuzz"
        elif i % 3 == 0:
            result += "Fizz"
        elif i % 5 == 0:
            result += "Buzz"
        else:
            result += str(i)
        if i != n:
            result += ","
    return result


n_8 = 16
print(fizzbuzz(n_8))

# 9. Napisz funkcję zwracającą n-ty element ciągu Fibonacciego
# przy F(0)= 0 i F(1) = 1.
# bez rekurencji:
# 3 pkt

n_9 = 6


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return c


print(fibonacci(n_9))


# 10. Napisz funkcję, która dla podanej posortowanej listy
# zwróci index wyszukiwanego elementu za pomocą wyszkukiwania binarnego,
# lub zwróci None gdy nie ma elementu w liscie:
# 3 pkt


def binary_search(lista, e):
    left = 0
    right = len(lista) - 1

    while left <= right:
        mid = (left + right) // 2
        if lista[mid] == e:
            return mid
        elif lista[mid] < e:
            left = mid + 1
        else:
            right = mid - 1
        return None


l_10 = [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]
print(binary_search(l_10, 2))
