import math
#Easy

a = input ("Введите целое число:")
for i in a:
    print (i)



a = input ("Введите число")
b = input ("Введите другое число:")
с = ""
c = a
a = b
b = c
print (a)
print (b)



age=int(input("Сколько вам лет?"))
if age >= 18:
    print ("Доступ разрешен")
else:
    print ("Извините, пользование данным ресурсом только с 18 лет")


#Normal

a = int(input("Введите целое число:"))
m = a%10
a = a//10
while a > 0:
    if a%10 >m:
        m = a%10
    a = a//10
print (m)



a = int(input("a:"))
b = int(input("b:"))
a = a + b
b = a - b
a = a - b
print (a), print(b)



a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
D = b**2 -4*a*c
if D >= 0:
    x1 = (-b + math.sqrt(D))/(2*a)
    x2 = (-b - math.sqrt(D))/(2*a)
    print ("X1=", x1)
    print ("X2=", x2)
else:
    print ("Корней нет!")


