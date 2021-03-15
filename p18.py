value = '3 7 4 2 4 6 8 5 9 3'

values = value.strip(' ')
print(values)

last = 4

#ARRAY WILL BE OF SIZE LAST , LAST + (LAST - 1)

arr = []
k = 0

for i in range(last):
	temp = []
	for j in range(2*last-1):
		if (i + j)	