#Даны две различные клетки шахматной доски. Напишите программу,  которая определяет, может ли король попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES», если из первой клетки ходом короля можно попасть во вторую, или «NO» в противном случае.
stol1, str1, stol2, str2 = int(input()), int(input()), int(input()), int(input())
if (stol1>=stol2-1 and stol1 <=stol2+1) and (str1>=str2-1 and str1<=str2+1):
    print("YES")
else: print("NO")

