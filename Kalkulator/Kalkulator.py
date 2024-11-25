import math
print ("---Kalkulator---")
print ("--1.Dodawanie--")
print ("--2.Odejmowanie--")
print ("--3.Mnożenie--")
print ("--4.Dzielenie--")
print ("--5.Potęgowanie--")
print ("--6.Pierwiastkowanie--")

dzialanie = input("Wybierz działanie:")

if dzialanie == "1":
    liczby = input("Podaj liczby do dodania, oddzielone spacją: ")
    liczby = [float(num) for num in liczby.split()]
    print("Suma =", sum(liczby))
elif dzialanie == "2":
    liczby = input("Podaj liczby do odjęcia, oddzielone spacją: ")
    liczby = [float(num) for num in liczby.split()]
    wynik = liczby[0] #Dzięki temu wynik zaczyna odejmować od liczby z indexu 0
    for num in liczby[1:]: #dzięki temu zaczynamy odejmowanie od 1 indexu
        wynik -= num
    print("Róźnica =", wynik)
elif dzialanie == "3":
    liczby = input("Podaj liczby do pomnożenia, oddzielone spacją: ")
    liczby = [float(num) for num in liczby.split()]
    wynik = 1
    for num in liczby:
        wynik *= num
    print("Iloczyn =", wynik)
elif dzialanie == "4":
    liczby = input("Podaj liczby do podzielenia, oddzielone spacją: ")
    liczby = [float(num) for num in liczby.split()]
    wynik = liczby[0]

    for num in liczby[1:]:
        if num == 0:
            print("Błąd: nie można dzielić przez zero!")
            break
        wynik /= num
elif dzialanie == "5":
    x = float(input("Podaj podstawę: "))
    y = float(input("Podaj wykładnik: "))
    wynik = math.pow(x, y)
    print(f"Wynik potęgowania {x}^{y} =", wynik)
elif dzialanie == "6":
    x = float(input("Podaj liczbę do spierwiastkowania: "))
    if x >= 0:
        wynik = math.sqrt(x)
        print(f"Pierwiastek kwadratowy z {x} =", wynik)
else:
    print("Brak takiego działania")