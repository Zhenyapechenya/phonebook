from sys import exit


FILE_NAME = "src/source.txt"



def get_phonebook_from_file(filename: str = FILE_NAME) -> list:
    """Функция для получения записей из текстового файла. Возвращает список, где каждый элемент - одна запись
    справочника (список строк)
    """
    try:
        with open(filename, "r+", encoding="utf-8") as file:
            result: list = [str.strip("\n").split("*") for str in file.readlines() if str != "\n"]
            return result
    except FileNotFoundError:
        exit('Файл со справочником не найден.\n')



def print_phonebook(phonebook_list: list, items_per_page: int = 10, current_page: int = 1) -> None:
    """Служит для вывода отформатированного списка в терминал. Есть возможность перелиствывания страниц справочника"""
    num_pages: int = len(phonebook_list) // items_per_page + 1
    flag_error: bool = False

    while True:
        start_index: int = (current_page - 1) * items_per_page
        end_index: int = start_index + items_per_page

        print("\033[H\033[J")
        print("\n№   | Имя              | Фамилия                 | Отчество                 "
            "| Название организации        | Рабочий телефон   | Личный телефон")
        for note in phonebook_list[start_index:end_index]:
            number: str = note[0]
            name: str = note[1]
            surname: str = note[2]
            patronymic: str = note[3]
            organization: str = note[4]
            work_phone: str = note[5]
            cellphone: str = note[6]
            print("{:-<150}".format("-"))
            print("{:<6}{:<19}{:<26}{:<27}{:<30}{:<20}{:<20}".format(number, name, surname, patronymic, organization, work_phone, cellphone))
        
        if flag_error == True:
            print("\nНекорректный ввод. Введите номер между 1 и", num_pages)
        user_input: str = input(f"\nВведите номер страницы от 1 до {num_pages} или \"вых\", чтобы вернуться в главное меню: ")
        if user_input == "вых":
            break
        try:
            page_number = int(user_input)
            if page_number < 1 or page_number > num_pages:
                raise ValueError
            current_page = page_number
            flag_error = False
        except ValueError:
            flag_error = True



def add_new_note(filename: str = FILE_NAME) -> None:
    """Функция запрашивает у пользователя необходимые параметры, формирует запись и добавляет ее в справочник"""
    name: str = input("Введите имя: ")
    surname: str = input("Введите фамилию: ")
    patronymic: str = input("Введите отчество: ")
    organization: str = input("Введите название организации: ")
    work_phone: str = input("Введите рабочий телефон: ")
    cellphone: str = input("Введите личный (сотовый) телефон: ")
    number: str = len(get_phonebook_from_file()) + 1
    new_note: str = [str(number), name, surname, patronymic, organization, work_phone, cellphone]
    new_note: str = "*".join(new_note)
    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(new_note + "\n")
    except FileNotFoundError as e:
        exit('Файл со справочником не найден.\n')



def get_edit_line() -> list:
    """Функция возвращает запись, которую в дальнейшем нужно будет отредактировать"""
    flag: bool = False
    number: str = input("Введите номер записи, которую хотите отредактировать. Если хотите снова пролистать справочник, введите \"смт\": ")
    if number == "смт":
        print_phonebook(get_phonebook_from_file())
        main_menu()
    else:
        phonebook_list: list = get_phonebook_from_file()
        for note in phonebook_list:
            if note[0] == number:
                flag = True
                return note

        if (flag == False):
            print("\nТакой записи нет. Попробуйте еще раз.\n")
            return get_edit_line()



def add_edited_note(line_for_edit: list) -> None:
    """Функция запрашивает у пользователя необходимые параметры, формирует запись с новыми параметрами,
    формирует новое содержимое текстового файла и обновляет его.
    """
    str_number_in_file = int(line_for_edit[0]) - 1
    print("\nВыбранная запись: ", " ".join(line_for_edit[1:]))
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
        add_edited_note(line_for_edit)



def get_param_for_find(phonebook_list: list) -> list:
    """Возвращает список параметров, по которым будет производиться поиск"""
    param = input("""
По какому параметру хотите искать? Введите одну или несколько цифр через пробел\n(после последней цифры не нужен):\n
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
        return [-1]
    else:
        param_list: list = param.split(" ")
        for par in param_list:
            if par not in ["0", "1", "2", "3", "4", "5", "6"]:
                print("Таких параметров нет. Попробуйте еще раз.")
                return get_param_for_find(phonebook_list)
        local_result_list: list = phonebook_list
        for p in param_list:
            local_result_list: list = find_notes(p, local_result_list)
        return local_result_list



def find_notes(param: str, phonebook_list: list) -> list:
    """Осуществляет поиск по значению параметра и возвращает соответствующий список.
    В дальнейшем функция вызывается снова, если поиск ведется по нескольким параметрам. Новы поиск производится
    уже не по всему справочнику, а среди записей, соответствующих предыдущему критерию.
    Таким образом поиск происходит быстрее
    """
    value: str = input(f"Введите значение для поиска для параметра {param}: ")
    local_result_list: list = [note for note in phonebook_list if note[int(param)] == value]
    return local_result_list



def main_menu() -> None:
    """Главное меню приложения. В зависимости от введенного параметра вызывает нужный функционал."""
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
        print("\nЗапись добавлена в справочник.")
    elif param == "3":
        add_edited_note(get_edit_line())
        print("\nЗапись отредактирована.")
    elif param == "4":
        founded_list: list = get_param_for_find(get_phonebook_from_file())
        if founded_list == [-1]:
            main_menu()
        else:
            print_phonebook(founded_list)
    elif param == "5":
        exit("Увидимся в следующий раз!\n")
    else:
        print("\nВы ввели неверный параметр. Попробуйте еще раз:")

    main_menu()



main_menu()
