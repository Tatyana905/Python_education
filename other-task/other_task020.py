# В 1769 году Леонард Эйлер сформулировал обобщенную версию Великой теоремы Ферма, предполагая,
# что по крайней мере n энных степеней необходимо для получения суммы, которая сама является энной степенью для n > 2.
# Напишите программу для опровержения гипотезы Эйлера (продержавшейся до 1967 года), и найдите четыре
# положительных целых числа, сумма 5-х степеней которых равна 5-й степени другого положительного целого числа.
#
# Таким образом, найдите пять натуральных чисел a, b, c, d, e(не превосходят 150) удовлетворяющих условию:
# a^5+b^5+c^5+d^5=e^5.

for a in range(1, 151):
    for b in range(a + 1, 151):
        for c in range(b + 1, 151):
            for d in range(c + 1, 151):
                e = int(((a ** 5) + (b ** 5) + (c ** 5) + (d ** 5)) ** 0.2)
                if e ** 5 == int((a ** 5) + (b ** 5) + (c ** 5) + (d ** 5)):
                    print(a + b + c + d + e)
                    print(f'a = {a} b = {b} c = {c} b = {b} e = {e}')
                if e**5 > a**5 + b**5 + c**5 + d**5:
                    break
