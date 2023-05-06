class Shape:
    def __init__(self, a:int, b:int) ->None:
        self.a = a
        self.b = b

    def perimeter(self):
        assert False

    def square(self):
        assert False

    def __str__(self) ->str:
        return f'perimeter {self.perimeter()} square {self.square()}'


class Rectangle(Shape):
    def __init__(self, a:int, b:int) ->None:
        Shape.__init__(self, a, b)

    def perimeter(self) ->int:
        return 2 * (self.a + self.b)

    def square(self) ->int:
        return self.a * self.b
    

class Triangle(Shape):

    def __init__(self, a:int, b:int, c:int) ->None:
        Shape.__init__(self, a, b)
        self.c = c

    def perimeter(self) ->int:
        return self.a + self.b + self.c
    
    def square(self) ->float:
        half_prmtr = self.perimeter()/2
        print(half_prmtr)

        return (half_prmtr*(half_prmtr-self.a)*(half_prmtr-self.b)*(half_prmtr-self.c))**0.5


class Point:
    def __init__(self,x:int, y:int) ->None:
        self.x = x
        self.y = y
        
    def distance(self, point) ->int:
        return ((point.x - self.x)**2 + (point.y - self.y)**2)**0.5


class Replacer:
    def __init__(self,a, b) ->None:
        self.a = a
        self.b = b 
 
    def __str__(self) -> str:
        return f'{self.a = },{self.b = }'
 
    def replace(self) ->None:
        self.a, self.b = self.b, self.a


if __name__ == '__main__':
    msg = 'Введите не более 3х целых чисел через запятую ,:'
    while True:
        print('Расчет периметра и площади фигуры')
        data = input(msg).split(',')
        match len(data):
            case 2:
                rctngl = Rectangle(int(data[0]),int(data[1]))
                print(rctngl)
                break
            case 3:
                trngl = Triangle(int(data[0]),int(data[1]), int(data[2]))
                print(trngl)
                break
            case _: 
                continue
    
    print('\n Вычисление расстояние между точками')
    data1 = []
    data2 = []
    while  True:
        msg = f'Введите координаты точки 1:'
        data1 = input(msg).split(',')
        msg = f'Введите координаты точки 2:'
        data2 = input(msg).split(',')
        if data1 and data2: break

    pnt1 = Point(int(data1[0]),int (data1[1]))
    pnt2 = Point(int(data2[0]),int (data2[1]))
    dstnc =  pnt1.distance(pnt2)
    print(dstnc)

    print('\n Изменим значение переменных местами'
          'Введите не более 3х целых чисел через запятую ,')
    data = input(msg).split(',')
    rplc = Replacer(int(data[0]), int(data[1]))
    print(rplc)
    rplc.replace()
    print(rplc)

          
    
        




  





    

    

   
    

    