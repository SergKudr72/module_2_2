first = int(input("Введите первое целое число: "))
second = int(input("Введите второе целое число: "))
third = int(input("Введите третье целое число: ")) # 3 2 0
if first == second and first == third: # если все числа равны, то 3
    print(3)
elif first == second or first == third or second == third: # если два из трех чисел одинаковые, то 2
    print(2)
else: # если нет одинаковых чисел, то 0
    print(0)


