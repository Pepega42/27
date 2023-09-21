import math
def plus():
    numb1 = float(input("Введите первое число: "))
    numb2 = float(input("Введите второе число: "))
    print(numb1 + numb2)
def minus():
    numb1 = float(input("Введите первое число: "))
    numb2 = float(input("Введите второе число: "))
    print(numb1 - numb2)
def delenie():
    numb1 = float(input("Введите первое число: "))
    numb2 = float(input("Введите второе число: "))
    print(numb1 / numb2)
def umnoz():
    numb1 = float(input("Введите первое число: "))
    numb2 = float(input("Введите второе число: "))
    print(numb1 * numb2)
def stepen():
    numb1 = float(input("Введите первое число: "))
    numb2 = float(input("Введите второе число: "))
    print(numb1 ** numb2)   
def koren():
    numb1 = float(input("Введите первое число: "))
    print(math.sqrt(numb1))
def fact():
    numb1 = float(input("Введите первое число: "))
    print(math.factorial(numb1))
def sinus():
    numb1 = float(input("Введите первое число: "))
    numb1 = math.radians(numb1)
    print(math.sin(numb1))
def cosinus():
    numb1 = float(input("Введите первое число: "))
    numb1 = math.radians(numb1)
    print(math.cos(numb1))
def tangens():
    numb1 = float(input("Введите первое число: "))
    numb1 = math.radians(numb1)
    print(math.tan(numb1))






while True:
    calc = input("+, -, /, *, **, sqrt, !, sin, cos, tg: ")    
    if calc == "+":
        try:
            sum()
        except:
            print("Данное число не сработает")
    elif calc == "-":
        try: 
            minus ()
        except:
            print("Данное число не сработает")
    elif calc == "*":
        try:    
            umnoz()
        except:
            print("Данное число не сработает")
    elif calc == "/":
        try:
            delenie()
        except:
            print("Данное число не сработает")
    elif calc == "**":
        try:
            stepen()  
        except:
            print("Данное число не сработает")
    elif calc == "sqrt":
        try:    
            koren()
        except:
            print("Данное число не сработает")
    elif calc == "!":
        try:    
            fact()
        except:
            print("Данное число не сработает")
    elif calc == "sin":
        try:    
            sinus()
        except:
            print("Данное число не сработает")
    elif calc == "cos":
        try:    
            numb1 = float(input("Введите первое число: "))
            cosinus()
        except:
            print("Данное число не сработает")
    elif calc == "tg":
        try:    
            tangens
        except:
            print("Данное число не сработает")
    else:
        break
