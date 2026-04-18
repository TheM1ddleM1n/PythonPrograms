import random


# Subroutine to demonstrate casting and operators
def MathsDemo(X, Y):
    DivisionResult = X / Y
    print("{} divided by {} is {}".format(X, Y, DivisionResult))
    IntDivisionResult = X // Y
    print("{} integer division by {} is {}".format(X, Y, IntDivisionResult))
    ModResult = X % Y
    print("{} modulus {} is {}".format(X, Y, ModResult))
    ExpResult = X**Y
    print("{} to the power of {} is {}".format(X, Y, ExpResult))


# Main program with random inputs
x = random.randint(1, 100)
y = random.randint(1, 10)
MathsDemo(x, y)
