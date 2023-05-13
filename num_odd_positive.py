def sum_of_odd_number() -> None:
    count = 10
    count_of_odd_number = 0
    while count:
        number = int(input("С клавиатуры вводится 10 целых чисел: "))
        count -=1
        if number > 0 and number % 2: count_of_odd_number +=1
    
    print(count_of_odd_number )


if __name__ == '__main__':
   
    sum_of_odd_number()