import numpy as np
import time

def sieve(end):
    grid = np.zeros(end + 1)

    i = 2
    while i < end + 1:
        if grid[i] == 1:
            i += 1
            continue
        for number in range(i + i, end + 1, i):
            grid[number] = 1
        i+=1
    return grid

def converGrid(grid):
    primes = []
    for i in range(len(grid)):
        if grid[i] == 0:
            primes.append(i)
    return primes[2:]

def checkSums(primes):
    sum = 0
    for value in primes:
        sum += value
    return sum
    #SLIDING WINDOW

def main():
    start = time.time()
    end = 2000000

    grid = sieve(end)
    primes = converGrid(grid)
    print(len(primes), checkSums(primes))
    print(time.time() - start)

if __name__ == '__main__':
    main()
