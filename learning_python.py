def print_pharse (n:int) -> None:
    while n:
        print('Я учу питон')
        n-=1



if __name__ == '__main__':
    n = int(input("Вводится целое число n"))
    print_pharse(n)
