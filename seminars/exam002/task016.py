# 7. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на шестой день спортсмен достиг результата — не менее 3 км.

print("Ежедневная пробежка. Программа вычисляет количество дней требуемых для достижения желаемого километража, при условии ежедневного увеличения на 10% относительно предыдущего дня.")
a = float(input("Введите начальные значения первого дня в километрах: "))
b = float(input("Введите желаемое значения в километрах: "))
day = 1
print(f"{day}-й день: {a} км")
while a < b:
    a = a + a * 0.1
    day += 1
    print(f"{day}-й день: {round(a, 2)} км")
print(f"На {day} день спортсмен достиг результата — не менее {b} км. ")