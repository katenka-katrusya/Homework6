# Урок 6. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension. Продолжение
# Просмотреть свои предыдущие ДЗ и попробовать применить к ним lambda, filter, map, zip, enumerate, list comprehension, там где это возможно.
# Формат сдачи: создаем новый репозиторий, в первую часть (закомментированную) вставляем изначальную версию задания, во вторую с изменениями. 
# Отправляем так же ссылкой два-три примера, желательно с разными примерами (lambda, filter, map, zip, enumerate, list comprehension)


# import random

# size = int(input("Введите размер списка: "))

# list = []
# for i in range(size):
#     list.append(random.randint(-10, 10 + 1))
# print("Изначальный список --> ", list)

# new_list = []
# for  i in range(0, len(list)):
#     j = random.randrange(0, len(list))
#     new_list.append(list[j])
#     list.remove(list[j])
# print("Перемешанный список --> ", new_list)


import random

size = int(input("Введите размер списка: "))

list = [random.randint(-10, 10 + 1) for i in range(size)]
print("Изначальный список --> ", list)
# ниже нет изменений
new_list = []
for  i in range(0, len(list)):
    j = random.randrange(0, len(list))
    new_list.append(list[j])
    list.remove(list[j])
print("Перемешанный список --> ", new_list)





# Эту задачу я вообще неправильно решила, так что вот

# string = "dsms 12mgk 3 11; p srvkmm cbdd, ;ps03l[- -- vnd"
# print(f"\nДана строка: {string}")

# element = input("Введите элемент, который хотите удалить: ")

# неправильный вариант, надо было читать внимательнее

# if element not in string:
#     print(f"Данного элемента нет в строке")
# else: 
#     result = string.replace(element, '')
#     print(f"Новая строка: {result}\n")

string = "dsms 12mgk 3 11; p srvkmm cbdd, ;ps03l[- -- vnd"
print(f"\nДана строка: {string}")

element = input("Введите элемент, который хотите удалить: ")

def Del(string):
    string = list(filter(lambda x: element not in x, string.split()))
    return " ".join(string)

text_del = Del(string)
print(text_del)