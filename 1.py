#Twoim zadaniem jest napisanie i przetestowanie funkcji, która wymaga jednego argumentu (roku)
# i zwraca wartość True jeżeli rok jest przestępny, lub False jeśli nie jest.

def leapYear():

    listYear = [1900, 2000, 2016, 1987]

    for Year in listYear:
        if Year % 4 == 0:
            print(f"{Year} is a leap year.")

        else:
            print(f"{Year} isn't a leap year.")

leapYear()
