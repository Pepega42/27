##Задание №2
def rectangle_area(width, height):
    ploshad = width * height
    return ploshad
x = float(input())
y = float(input())
print (rectangle_area(x, y))


##Задание №3
def is_even(number):
    chet = number % 2
    if chet == 0:
        return True
    else:
        return False
    

##Задание №4
def sum_digits(number):
    if number <10:
        return number
    else:
        return number %10 + sum_digits(number//10)
x = int(input())
print(sum digits(x))