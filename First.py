#8 bittes szám bin to dec
import re
from math import sqrt
meret = 8
binNumber = str(input("Adj meg egy bin számot:"))
bits =  [None] * meret
max_bit_number = 128
bit_numbers = [None] * meret
finalNumber = 0

def bitNumber():
    inic = 0
    while inic < 8:
        if (inic == 0):
            bit_numbers[inic] = max_bit_number
        else:
            bit_numbers[inic] = bit_numbers[inic - 1] / 2
        inic += 1


def bitsToArray():
    inic = 0
    for x in binNumber:
        bits[inic] = int(x)
        inic +=1

def bitsInBitNumbers():
    finalNumber = 0
    inic = 0
    numbers = [None] * meret
    while inic < len(numbers):
        numbers[inic] = bits[inic] * bit_numbers[inic]
        inic += 1
    for x in numbers:
        finalNumber += x
    print (finalNumber)

bitNumber()
bitsToArray()
bitsInBitNumbers()


