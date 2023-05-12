"""
1. С некоторого момента прошло 234 дня. Сколько полных
недель прошло за этот период?
"""
# Ваш код
def full_weeks(day=234)->int:
    return day // 7

"""
2. Написать программу, которая решает следующую задачу:
«N школьников делят k яблок поровну так, чтобы каждому достались только целые яблоки, остальные яблоки остаются в корзинке. 
Определить, сколько яблок достанется каждому школьнику и сколько яблок останется в корзинке».
"""
# Ваш код
def sharing_apples(N:int, K:int) -> str:
    return  f'каждому ученику достанется по {K//N} яблок, в корзине останется лежать {K%N} яблок '

"""  
3. Дан прямоугольник с размерами 543×130 мм. Сколько квадратов со стороной 130 мм можно отрезать от него?
"""
# Ваш код
class Rectangle():
    def __init__(self,side_a:int, side_b:int) -> None:
        self.side_a = side_a
        self.side_b = side_b

    def square (self) -> int:
        return self.side_a * self.side_b
    
    @property
    def a_side(self) -> int:
        return self.side_a
    
    @property
    def b_side(self) -> int:
        return self.side_b
    
    @staticmethod
    def squares_in_rectangle(a, b) -> str:
        return f'можно отрезать {a.square()//b.square()} квадратов со стороной {b.a_side}мм от прямогульника с размерами {a.a_side}x{a.b_side}мм'


"""  
4. В купейном вагоне имеется 9 купе с четырьмя местами для пассажиров в каждом. 
   Определить номер купе, в котором находится место с заданным номером (нумерация мест сквозная, начинается с 1).
"""
# Ваш код
def defain_place(place_number:int) -> int:
    return (place_number+3) // 4


"""  
5. В подъезде №1 пятиэтажного жилого дома 15 квартир.
Определить, на каком этаже этого подъезда находится квартира с заданным номером.
"""
# Ваш код
def defain_apartament (apartaments_number: int) ->  int:
    return (apartaments_number + 2) // int (15/3)

"""
6*. Даны два целых числа a и b. 
Если a делится на b или b делится на a нацело, то вывести 1, иначе – любое другое число.
Условные операторы и операторы цикла не использовать.
"""
# Ваш код
def dividend_divisor (a:int, b:int) -> int:
    return int(a%b==0) or int(b%a==0) 

if __name__ == '__main__':
    
    print(full_weeks())

    print(sharing_apples(10,15))

    rect_a = Rectangle(543,130)
    rect_b = Rectangle(130,130)
    print(Rectangle.squares_in_rectangle(rect_a, rect_b))

    print(defain_place(35))

    print(defain_apartament(14))
    
    print(dividend_divisor(5,2))


