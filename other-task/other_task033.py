# Камень, ножницы, бумага, ящерица, Спок
a, b = input(), input()
win_Timur = [
    'каменьножницы', 'ножницыбумага', 'бумагакамень','Споккамень','ножницыящерица',
    'ящерицабумага','ящерицаСпок', 'каменьящерица']

if a == b:
    print("ничья")
elif a+b in win_Timur:
    print("Тимур")
else:
    print("Руслан")
