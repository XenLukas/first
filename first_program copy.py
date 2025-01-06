# Изменить первый элемент списка на 20
numbers = [3, 7, 1, 9, 2, 5, 4, 8, 6, 10]
numbers.append(20)
print(numbers)

# Создать новый список с числами из списка numbers, возведённых в квадрат, используя цикл
new_spisok = []
for i in numbers:
    number_square = i ** 2
    new_spisok.append(number_square)
print(new_spisok)

# Найти сумму чисел в списке, не используя функцию sum, воспользоваться циклом
summa = 0
for i in numbers:
    summa += i
print(summa)

# Создать новый список с числами из списка numbers, где будут числа только больше 5
# Воспользоваться циклом и условием if
new_member = []
for i in numbers:
    if i > 5:
        new_member.append(i)   
print (new_member)

# Перевернуть список используя срезы ([:], [::])
for i in numbers[::-1]: 
    print (i)