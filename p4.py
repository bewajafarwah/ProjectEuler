import sys

def checkPali(value):
    strval = str(value)

    for i in range(int(len(strval) / 2)):
        if strval[i] != strval[-1 - i]:
            return False
    return True

def main():
    score = []
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            value = i * j
            if checkPali(value):
                score.append(value)

    max = 1
    for sc in score:
        if max < sc:
            max = sc
    print(max)

if __name__ == '__main__':
    main()
