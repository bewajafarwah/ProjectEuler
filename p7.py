import time

count=0
n=1


def isprime(n,primes):
	prime=True
	for i in primes:
		if n%i==0:
			prime=False
			break
		

	return prime

start = time.time()
primes=[2]
while count < 10000:
	n+=2
	if isprime(n,primes) is True:
		count+=1
		primes.append(n)

print(n, time.time() - start)




