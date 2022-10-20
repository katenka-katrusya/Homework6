from secrets import choice
import Model
import View

def main_menu():
    while True:
        print('\nГлавное меню:')
        print('1. Показать все контакты')
        print('2. Добавить контакт')
        print('3. Удалить контакт')
        print('4. Изменить контакт')
        print('5. Найти контакт')
        print('6. Сохранить файл')
        print('0. Выйти из программы')
        choice = int(input('Выберите пункт: '))
        match (choice):
            case 1:
                print('\nВсе контакты:')
                show_contacts()
            case 2:
                add_contact()
                print('\nКонтакт добавлен\n')
            case 3:
                remove_contact()
                print('\nКонтакт удален\n')
            case 4:
                change_contact()
                print('\nКонтакт изменён!\n')
            case 5:
                find_contact()
                print('\nКонтакт найден!\n')
            case 6:
                save_file()
                print('\nФайл сохранен!\n')
            case 0:
                break


def start():
    open_file()
    View.printPhoneBook()
    main_menu()

def show_contacts():
    open_file()
    View.printPhoneBook()

def open_file():
    with open(Model.path, "r", encoding="UTF-8") as data:
        contacts_list = data.read().split("\n")
        Model.phonebook = contacts_list

def save_file():
    with open(Model.path, "w", encoding="UTF-8") as data:
        data.write(('\n'.join(Model.phonebook)))

def add_contact():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    last_name = input('Введите отчество: ')
    phone = input('Введите телефон: ')
    contact = f'{name}; {surname}; {last_name}; {phone};\n'
    Model.phonebook.append(contact)
    View.printPhoneBook()

def remove_contact():
    choice = int(input('Введите номер элемента для удаления: '))
    Model.phonebook.pop(choice)
    View.printPhoneBook()

def change_contact():

    choice = int(input('Введите номер элемента для изменения: '))
    choice2 = int(input('Что изменяем (0-имя, 1-фамилия, 2-отчество, 3-телефон): '))

    contact = Model.phonebook.pop(choice).split(';')
    print(contact)
    contact[choice2] = input('Введите новое значение: ')
    print(contact)
    Model.phonebook.insert(choice, ';'.join(contact))
    View.printPhoneBook()

def find_contact():
    name = input("Введите имя, фамилию или отчество: ")
    with open(Model.path, "r", encoding="UTF-8") as data:
        contacts_list = data.read().split("\n")
        Model.phonebook = contacts_list
        for line in contacts_list:
            count=0
            if name in line:
                print(f'\n{line}')
                count+=1