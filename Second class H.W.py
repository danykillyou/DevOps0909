x = 5
y = 3
if x > y:
    print("BIG")
else:
    print("small")

# B
for i in range(5):
    print(i)

# C

z = 2
if z == 1:
    print("summer")
elif z == 2:
    print("winter")
elif z == 3:
    print("fall")
elif z == 4:
    print("spring")

# D
# the loop will run 10 times and the last print will be 10

# E
from forex_python.converter import CurrencyRates

Age = 44
Name = 'Diana'
# First_Letter = D
Currency = CurrencyRates()
Abroad = False
Appartment = 5
print(Age)
print(Name[0])
x = Currency.get_rate('ILS', 'USD')
print(1 / float(x))
print(Age + 1 / float(x))

# F
Phone_Num = input('pls enter your phone number ')
print(f'THE PHONE IS: {Phone_Num}')


# G
def printHello():
    print('hello')


def calculate():
    print(str(5 + 3.2))


# H
def printName(Name):
    print(Name)


printName(input('pls enter your name '))


def numRecieve(Num):
    print(str(int(Num) / 2))


numRecieve(input('pls enter THE NUMBER '))


# I
def addNum(num1, num2):
    print(float(num1) + float(num2))


addNum(input('pls enter THE NUMBER1 '), input('pls enter THE NUMBER2 '))


def addName(name1, name2):
    x = name1 + " " + name2
    #    print(x)
    return (x)


print(addName(input('pls enter name1 '), input('pls enter THE name2 ')))

# K
u = ''
for i in range(5):
    u = u + '*'
    print(u)

# L

for i in range(-3, 4):
    print(" " * (3 - (i.__abs__())) + "*" + " " * ((i.__abs__()) * 2 - 1) + "*" * int((i.__abs__()) % 2.5 / 3 + 0.999))


# M
def numRecieve():
    n1 = input('pls enter THE NUMBER ')
    return n1


def printSum(numForLoop):
    sum1 = 0
    for i in numForLoop:
        sum1 = sum1 + int(i)
    return sum1


#       print(sum1)

# print(numRecieve())
numForLoop = numRecieve()
print(printSum(numForLoop))

