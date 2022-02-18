import math
def solve(numheads,numlegs):
    rabbit = numlegs/2 - numheads
    chicken = numheads - rabbit
    if rabbit==math.floor(rabbit) and chicken==math.floor(chicken):
        print(int(chicken),int(rabbit))
    else:
        print('IMPOSSIBLE')
numheads = int(input())
numlegs = int(input())
solve(numheads,numlegs)

