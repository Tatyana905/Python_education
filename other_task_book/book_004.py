# Напишите программу, в которой описана функция, возвращающая результатом второе по величине число в списке, переданном функции в качестве аргумента

numbers = [ 1, 13, 2, 35, 5, 6, 7, 12]

def Max_first(list_number):
    sorted_list = sorted(list_number)
    return sorted_list[-2]

print(f"Второй по величине максимальный элемент списка: {Max_first(numbers)}")