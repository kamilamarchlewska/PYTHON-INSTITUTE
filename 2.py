# Twoim zadaniem jest napisanie i przetestowanie funkcji,
# która przyjmuje dwa argumenty (rok i miesiąc) i zwraca liczbę dni w danym miesiącu
# (podczas gdy tylko luty jest wrażliwy na wartość rok, twoja funkcja powinna być uniwersalna).

def leapYear():
    year = int(input('Enter the year: '))
    month = int(input('Enter month: '))


    listDays30 = [4, 6, 9, 11]
    listDays31 = [1, 3, 5, 7, 8, 10, 12]

    if year % 4 == 0:
        if month == 2:
            print(f'Month {month} has 29 days')
        elif month in listDays30:
            print(f'Month {month} has 30 days')
        elif month in listDays31:
            print(f'Month {month} has 31 days')

    else:
        if month == 2:
            print(f'Month {month} has 30 days')
        elif month in listDays30:
            print(f'Month {month} has 30 days')
        elif month in listDays31:
            print(f'Month {month} has 31 days')

leapYear()