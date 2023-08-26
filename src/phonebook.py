from sys import exit


FILE_NAME = "src/source.txt"



def get_phonebook_from_file(filename: str = FILE_NAME) -> list:
    try:
        with open(filename, "r+", encoding="utf-8") as file:
            result = [str.strip("\n").split("*") for str in file.readlines() if str != "\n"]
            return result
    except FileNotFoundError as e:
        exit('Файл со справочником не найден.')



def print_phonebook(phonebook_list: list, items_per_page: int = 10, current_page: int = 1) -> None:   
    num_pages = len(phonebook_list) // items_per_page + 1
    flag_error = 0
    
    while True:
        start_index = (current_page - 1) * items_per_page
        end_index = start_index + items_per_page

        print("\033[H\033[J")
        print("\n№   | Имя              | Фамилия                 | Отчество                 "
            "| Название организации        | Рабочий телефон   | Личный телефон")
        for note in phonebook_list[start_index:end_index]:
            number = note[0]
            name = note[1]
            surname = note[2]
            patronymic = note[3]
            organization = note[4]
            work_phone = note[5]
            cellphone = note[6]
            print("{:-<150}".format("-"))
            print("{:<6}{:<19}{:<26}{:<27}{:<30}{:<20}{:<20}".format(number, name, surname, patronymic, organization, work_phone, cellphone))
        
        if flag_error == 1:
            print("\nНекорректный ввод. Введите номер между 1 и", num_pages)
        user_input = input(f"\nВведите номер страницы от 1 до {num_pages} или \"вых\", чтобы вернуться в главное меню: ")
        if user_input == "вых":
            break
        try:
            page_number = int(user_input)
            if page_number < 1 or page_number > num_pages:
                raise ValueError
            current_page = page_number
        except ValueError:
            flag_error = 1



def add_new_note(filename: str = FILE_NAME) -> None:
    # ДОБАВИТЬ ВАЛИДАЦИЮ ВХОДНЫХ ДАННЫХ
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    patronymic = input("Введите отчество: ")
    organization = input("Введите название организации: ")
    work_phone = input("Введите рабочий телефон: ")
    cellphone = input("Введите личный (сотовый) телефон: ")
    number = len(get_phonebook_from_file()) + 1
    new_note = [str(number), name, surname, patronymic, organization, work_phone, cellphone]
    new_note = "*".join(new_note)
    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(new_note + "\n")
    except FileNotFoundError as e:
        exit('Файл со справочником не найден.')



def get_edit_str() -> str:
    number = input("Введите номер записи, которую хотите отредактировать. Если хотите снова пролистать справочник, введите \"смт\": ")
    if number == "смт":
        print_phonebook(get_phonebook_from_file())
        main_menu()
    # ДОБАВИТЬ ВАЛИДАЦИЮ ВХОДНЫХ ДАННЫХ
    else:
        phonebook_list = get_phonebook_from_file()
        for note in phonebook_list:
            if note[0] == number:
                return note



def add_edited_note(line_for_edit: list) -> None:
    str_number_in_file = int(line_for_edit[0]) - 1
    print("\nВыбранная запись: ", " ".join(line_for_edit))
    param = input("""
    Какой параметр хотите изменить? Введите соответствующую цифру:\n
    [1] - Имя
    [2] - Фамилия
    [3] - Отчество
    [4] - Название организации
    [5] - Рабочий телефон
    [6] - Личный телефон\n
    """)

    if param in ["1", "2", "3", "4", "5", "6"]:
        line_for_edit[int(param)] = input("\nВведите новое значение: ")
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                lines = file.readlines()
                tmpstr = "*".join(line_for_edit) + "\n"
                lines[str_number_in_file] = tmpstr
                new_data = lines
            with open(FILE_NAME, "w", encoding="utf-8") as f:
                f.write("".join(new_data))
        except FileNotFoundError as e:
            exit('Файл со справочником не найден.')
    else:
        print("Вы ввели неверный параметр. Попробуйте еще раз:")
        main_menu()

    # ДОБАВИТЬ ВАЛИДАЦИЮ ??????????????????????????????????



def get_param_for_find(phonebook_list: list) -> list:
    param = input("""
    По какому параметру хотите искать? Введите одну или несколько цифр через пробел:\n
    [0] - Порядковый номер
    [1] - Имя
    [2] - Фамилия
    [3] - Отчество
    [4] - Название организации
    [5] - Рабочий телефон
    [6] - Личный телефон
    [7] - Вернуться в главное меню\n             
    """)

    if "7" in param:
        print("\033[H\033[J")
    else:
        param_list = param.split(" ")
        local_result_list = phonebook_list
        for p in param_list:
            local_result_list = find_notes(p, local_result_list)
        return local_result_list
            


def find_notes(param: str, phonebook_list: list) -> list:
    value = input(f"Введите значение для поиска для параметра {param}: ")
    local_result_list = [note for note in phonebook_list if note[int(param)] == value]
    return local_result_list



def main_menu() -> None:
    param = input(
    """
    [1] - Показать справочник
    [2] - Добавить новую запись в справочник
    [3] - Редактировать запись
    [4] - Поиск записей по одной или нескольким характеристикам
    [5] - Закрыть приложение\n
    """)
    print("\033[H\033[J")

    if param == "1":
        print_phonebook(get_phonebook_from_file())
    elif param == "2":
        add_new_note()
        print("\Запись добавлена в справочник.")
    elif param == "3":
        add_edited_note(get_edit_str())
        print("\nЗапись отредактирована.")
    elif param == "4":  
        list_from_file = get_phonebook_from_file()
        print_phonebook(get_param_for_find(list_from_file))
    elif param == "5":
        exit("Увидимся в следующий раз!\n")
    else:
        print("\nВы ввели неверный параметр. Попробуйте еще раз:")

    main_menu()



main_menu()
