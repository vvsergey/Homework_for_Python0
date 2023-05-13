def my_sum () -> None:
    summa = 0
    flag = True
    while flag:
        inp = input("Вводится целое число n  или слово 'Хвтаит' для подсчета суммы: ")
        if inp  == 'xватит':  flag = False
        else: summa += int(inp)
    
    print(summa)

if __name__ == '__main__':
    my_sum ()