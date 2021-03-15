def sosq(n):
    return int((n * (2*n + 1) * (n + 1)) / 6)

def sqos(n):
    return int((n * (n + 1)) / 2) ** 2

def main():
    stop = 100
    print(sqos(stop) - sosq(stop))

if __name__ == '__main__':
    main()
