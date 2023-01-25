f1=1
f2=2

n = int(input("введите значение: "))
print(f1, f2, end= " ")

for i in range(2, n):
    f1,f2 = f2, f1 + f2
    print(f2, end=" ")
