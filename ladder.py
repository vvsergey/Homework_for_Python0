def ladder(number: int) ->None:
    flor = 1
    while flor <= number:
        print(flor * '1')
        flor += 1



if __name__ == '__main__':
    number  = int(input('Вводится натуральное число n: '))
    ladder(number)