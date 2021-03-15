import numpy as np
from math import log

primes = [2]

def isPrime(n):
    for prime in primes:
        if n % prime == 0:
            return
    primes.append(n)

def lcm(n):
    values = []
    for i in range(2, n + 1):
        values.append(i)

    for i in range(3, n + 1):
        isPrime(i)


    magic = 1

    for prime in primes:
        while True:
            flg = False
            for index in range(len(values)):
                value = values[index]
                if value % prime == 0 and int(value / prime) >= 1:
                    flg = True
                    values[index] = int(values[index] / prime)
            if flg:
                magic *= prime
            else:
                break
    return magic

def accha_lcm(n):
    for i in range(3, n + 1):
        isPrime(i)

    magic = 1

    for index in range(len(primes)):
        prime = primes[index]
        raiseTo = int(log(n) / log(prime))
        magic *= (prime ** raiseTo)

    return magic

def main():
    print(lcm(10))


if __name__ == '__main__':
    main()
