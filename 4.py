#Twoim zadaniem jest napisanie funkcji sprawdzającej, czy liczba jest liczbą pierwszą, czy nie.

def header():

    title = 'PRIME NUMBERS 1 - 1000'
    width = len(title)

    print('-' * width)
    print(title)
    print('-' * width)


def numberPrime(numberUser):

    listPrime = []

    for number in range(1, 1001):
        if numberUser % number == 0:
            listPrime.append(numberUser)

    lengthListPrime = len(listPrime)

    if lengthListPrime == 2:
        print(f"{numberUser} is a prime number.")
    else:
        print(f"{numberUser} isn't a prime number.")

header()
numberUser = int(input('Enter the number: '))
if numberUser <= 1000:
    numberPrime(numberUser)
else:
    print('Wrong number.')