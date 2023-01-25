try:
    chislo1 = int(input("Введите четырехзначное число: "))
except ValueError:
    print("Вы ввели не число")
if  1000 < chislo1 < 10000:
    chislo2 = int(str(chislo1)[-1:-5:-1])
    print(chislo2)
else:
    print("Число не четырехзначное")

try:
    chislo = int(input("введите число: "))
    maximum = 0
except ValueError:
    print("Вы ввели не число")
while chislo > 0:
    if  chislo % 10 > maximum:
         maximum = chislo % 10
    chislo = chislo // 10
print(maximum)
