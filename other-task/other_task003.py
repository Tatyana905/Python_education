#Напишите программу, которая приветствует пользователя, выводя слово «Привет» (без кавычек), после которого должна стоять запятая и пробел, а затем введенное имя и восклицательный знак.
name = input()
print("Привет", name, sep = ", ", end ="!")

age = int(input())
if age<=13:
    print("детство")
elif 14 <= age <= 24:
    print("молодость")
elif 25 <= age <= 59:
    print("зрелость")
elif age >= 60:
    print("старость")