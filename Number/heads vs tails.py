import random

heads = 0
tails = 0
turns = 0

print('Welcome to the heads and tails coin flipping machine')

while turns != 100:
    flips = random.randint(1, 2)
    if flips == 1:
        heads = heads + 1
    else:
        tails = tails + 1
    turns = heads + tails

print('The number of heads flipped was', heads, 'the number of tails flipped was', tails)
