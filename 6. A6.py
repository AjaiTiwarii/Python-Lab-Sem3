'''part 1'''

import math

class Arithmatic:
    def power(self,a,x):
        print("power method inside class Arithmatic")
        return (a**x)
    def divide(self,a, b):
        print("divide method inside class Arithmatic")
        if(b!=0):
            result = a / b
            return result
        else:
            print("Error: Division by zero is not allowed")
            return None
    def log(self,x):
        print("log method inside class Arithmatic")
        try:
            result = math.log(x,2)
            return result
        except:
            print("Error")
            return None
    
    def angle_converter(self,value):
        print("angle_converter method inside class Arithmatic")
        result = value * (180 / math.pi)
        return result
        
calc = Arithmatic()
print(calc.power(10,2))
print(calc.log(8))
print(calc.divide(10,2))
print(calc.angle_converter(3.14))






'''part 2'''


class Rectangle:
    def calcAreaRectangle(self, height, width):
        return height * width

class Square:
    def calcAreaSquare(self, side):
        return side * side

class Parallelpiped(Rectangle, Square):
    
    def calcVolume(self, height_or_side, length , width=None):
        
        obj1=Rectangle()
        obj2=Square()
        
        if width is None:
            
            area=obj2.calcAreaSquare(height_or_side)
            
        else:
            
            area = obj1.calcAreaRectangle(height_or_side, width)
        
        volume = area * length
        return volume

obj = Parallelpiped()

inputs = int(input("Enter number of inputs"))
if(inputs==2):
    num1=int(input("Enter n1: "))
    num2=int(input("Enter n2: "))

    print("Volume of parallelpiped using square = ", obj.calcVolume(num1, num2))
elif(inputs==3):
    num3=int(input("Enter n3: "))
    num4=int(input("Enter n4: "))
    num5=int(input("Enter n5: "))

    print("Volume of parallelpiped using rectangle = ", obj.calcVolume(num3, num5, num4))
    