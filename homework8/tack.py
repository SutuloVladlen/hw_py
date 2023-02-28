#  Фамилия, имя, отчество, номер телефона


def main_menu():
    file_contacts = 'file.txt'
    while True:
        user_choice = input('1 - добавить новый контакт,\n '
                            '2 - найти контакт,\n 3 - посмотреть весь справочник,\n 4 - изменить контакт,\n 5 - удалить контакт,\n 0 - выйти\n')
        if user_choice == '1':
            save_to_file(input_contact(), file_contacts)# print('добавить новый контакт')
        elif user_choice == '2':
            search_field, what = ask_search()
            print(search_contact(file_contact, search_field, what))
        elif user_choice == '3':
            print(print_contacts(read_file_dict(file_contacts)))# print('посмотреть весь справочник')
        elif user_choice == '4':
            change_phone_number(file_contacts)
        elif user_choice == '5':
            delete_contact(file_contacts)
        elif user_choice == '0':
            print('До свидания')
            break


def input_contact():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = int(input('Введите номер телефона: '))
    return last_name, first_name, phone_number


def save_to_file(data: tuple, file, mode='a'):
    data_str = ' '.join(map(str, data))
    # print(data_str)
    # 'cp-1251'
    with open(file, mode, encoding='utf-8') as fd:
        fd.write(f'{data_str}\n')


def read_file_dict(file):
    with open(file, 'r', encoding='utf-8') as fd:
        lines = fd.readlines()
    headers = ['Фамилия', 'Имя', 'Номер телефона']
    list_contacts = []
    for line in lines:
        line = line.strip().split()
        list_contacts.append(dict(zip(headers, line)))
    return list_contacts

def read_file_to_list(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        contact_list = []
        for line in file.readlines():
            contact_list.append(line.split())
    return contact_list

def search_contact(list_contacts: list, param: str, what: str):
    param_dict = {'1': 'Фамилия', '2': 'Имя', '3': 'Номер телефона'}
    list_contacts = read_file_dict(list_contacts)
    found_contacts = []
    for contact in list_contacts:
        if contact[param_dict[param]] == what:
            found_contacts.append(contact)
            return found_contacts
    return "Контакт не найден"


def ask_search():
    print('По какому полю выполнить поиск?')
    search_param = input('1 - по фамилии, 2 - по имени, 3 - по номеру телефона: ')
    what = None
    if search_param == '1':
        what = input('Введите фамилию для поиска: ')
    elif search_param == '2':
        what = input('Введите имя для поиска: ')
    elif search_param == '3':
        what = input('Введите номер для поиска: ')
    return search_param, what


def print_contacts(contact_list: list):
    for contact in contact_list:
        for key, value in contact.items():
            print(f'{key}: {value:10}', end='')
        print()


def show_phonebook(file_name):
    list_of_contacts = sorted(read_file_dict(file_name), key=lambda x: x['Фамилия'])
    print_contacts(list_of_contacts)
    print()
    return list_of_contacts


def search_parameters():
    print('По какому полю выполнить поиск?')
    search_field = int(input('1 - по фамилии\n2 - по имени\n3 - по номеру телефона\n'))
    print()
    search_value = None
    if search_field == 1:
        search_value = input('Введите фамилию для поиска: ')
        print()
    elif search_field == 2:
        search_value = input('Введите имя для поиска: ')
        print()
    elif search_field == 3:
        search_value = input('Введите номер для поиска: ')
        print()
    return search_field, search_value


def find_number(contact_list):
    search_field, search_value = search_parameters()
    found_contacts = []
    for contact in read_file_to_list(contact_list):
        if contact[search_field] == search_value:
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        print('Контакт не найден!')
    else:
        print_contacts(found_contacts)
    print()


def search_to_modify_contact(file_contact): 
    serch_field, serch_value = search_parameters()
    resalt = []
    for contact in read_file_to_list(file_contact):
        print(contact,1432)
        if contact[serch_field-1]==serch_value:
            resalt.append(contact)
    if len(resalt)>1:
        print("Найдено несколько контактов")
        for i in range(len(resalt)):
            print(f"{i+1}: {resalt[i]}")
        num_contact = input(int("Введите номер контакта для изменения или удаления")) 
        return resalt[num_contact-1]
    if len(resalt)==1:
        return resalt[0]
    elif print("Контакт не найден."):
        print()


def change_phone_number(file_contact):
    contact_list = read_file_to_list(file_contact)
    number_to_change = search_to_modify_contact(file_contact)
    contact_list.remove(number_to_change)
    print('Выберите параметр изменения')
    field = input('1 - Фамилия\n2 - Имя\n3 - Номер телефона\n4 - Полностью изменить контакт\n')
    if field == '1':
        number_to_change[0] = input('Введите новую фамилию: ')
    elif field == '2':
        number_to_change[1] = input('Введите новое имя: ')
    elif field == '3':
        number_to_change[2] = input('Введите новый номер телефона: ')
    elif field == '4':
        number_to_change[0] = input('Введите новую фамилию: ')
        number_to_change[1] = input('Введите новое имя: ')
        number_to_change[2] = input('Введите новый номер телефона: ')
    contact_list.append(number_to_change)
    with open(file_contact, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)


def delete_contact(file_contac):
    contact_list = read_file_to_list(file_contac)
    number_to_change = search_to_modify_contact(file_contac)
    contact_list.remove(number_to_change)
    print(f"Контакт {number_to_change} удален из списка контактов")
    with open(file_contac, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)
    


if __name__ == '__main__':
    file_contact = 'file.txt'
    main_menu()
