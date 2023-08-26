from sys import exit



items_per_page = 10
current_page = 1


class Phonebook:

    FILE_NAME = "source.txt"


    def get_phonebook_from_file(self, filename: str) -> list:
        try:
            with open(filename, "r+", encoding="utf-8") as file:
                result = [str.strip("\n").split("*") for str in file.readlines() if str != "\n"]
                return result
        except FileNotFoundError as e:
            print(e)


    def print_phonebook(self, phonebook_list, start, end) -> None:
        print("\033[H\033[J")
        print("\n№   | Имя              | Фамилия                 | Отчество                 "
              "| Название организации        | Рабочий телефон   | Личный телефон")
        
        # items_per_page = 10
        # current_page = 1
        num_pages = len(phonebook_list) // items_per_page + 1

        while True:
            # выводим элементы списка для текущей страницы
            start_index = (current_page - 1) * items_per_page
            end_index = start_index + items_per_page
            print(phonebook_list[start_index:end_index])


            one.print_phonebook(phonebook_list, start_index, end_index)

            # спрашиваем у пользователя, хочет ли он перейти на другую страницу
            user_input = input("\nEnter page number or 'q' to quit: ")
            if user_input == 'q':
                break

            # обрабатываем пользовательский ввод
            try:
                page_number = int(user_input)
                if page_number < 1 or page_number > num_pages:
                    raise ValueError
                current_page = page_number
            except ValueError:
                print("\nInvalid input. Please enter a number between 1 and", num_pages)



        for note in phonebook_list[start:end]:
            number = note[0]
            name = note[1]
            surname = note[2]
            patronymic = note[3]
            organization = note[4]
            work_phone = note[5]
            cellphone = note[6]
            print("{:-<150}".format("-"))
            print("{:<6}{:<19}{:<26}{:<27}{:<30}{:<20}{:<20}".format(number, name, surname, patronymic, organization, work_phone, cellphone))
        # ДОБАВИТЬ ПРОЛИСТЫВАНИЕ


    def add_new_note(self, filename: str) -> None:
        # ДОБАВИТЬ ВАЛИДАЦИЮ ВХОДНЫХ ДАННЫХ
        name = input("Введите имя: ")
        surname = input("Введите фамилию: ")
        patronymic = input("Введите отчество: ")
        organization = input("Введите название организации: ")
        work_phone = input("Введите рабочий телефон: ")
        cellphone = input("Введите личный (сотовый) телефон: ")
        number = len(self.get_phonebook_from_file(self.FILE_NAME)) + 1
        new_note = [str(number), name, surname, patronymic, organization, work_phone, cellphone]
        new_note = "*".join(new_note)
        try:
            with open(filename, "a", encoding="utf-8") as file:
                file.write(new_note + "\n")
        except FileNotFoundError as e:
            print(e)



    def get_edit_str(self) -> str:
        number = input("Введите номер записи, которую хотите отредактировать. Если хотите снова пролистать справочник, введите \"смт\": ")
        
        if number == "смт":
            one.print_phonebook(one.get_phonebook_from_file(one.FILE_NAME))
            main_menu()
        # ДОБАВИТЬ ВАЛИДАЦИЮ ВХОДНЫХ ДАННЫХ
        else:
            phonebook_list = self.get_phonebook_from_file(self.FILE_NAME)
            for note in phonebook_list:
                if note[0] == number:
                    return note



    def add_edited_note(self, line_for_edit: list) -> None:
        str_number_in_file = int(line_for_edit[0]) - 1
        print("\nВыбранная запись: ", " ".join(line_for_edit))
        param = input("""
        Какой параметр хотите изменить? Введите соответствующую цифру:
        
        [1] - Имя
        [2] - Фамилия
        [3] - Отчество
        [4] - Название организации
        [5] - Рабочий телефон
        [6] - Личный телефон
                      
        """)

        if param in ["1", "2", "3", "4", "5", "6"]:
            line_for_edit[int(param)] = input("\nВведите новое значение: ")
            try:
                with open(self.FILE_NAME, "r", encoding="utf-8") as file:
                    lines = file.readlines()
                    tmpstr = "*".join(line_for_edit) + "\n"
                    lines[str_number_in_file] = tmpstr
                    new_data = lines
                with open(self.FILE_NAME, "w", encoding="utf-8") as f:
                    f.write("".join(new_data))
            except FileNotFoundError as e:
                print(e)
        else:
            print("Вы ввели неверный параметр. Попробуйте еще раз:")
            main_menu()

        # ДОБАВИТЬ ВАЛИДАЦИЮ ??????????????????????????????????
 



    def get_param_for_find(self, phonebook_list) -> list:
        param = input("""
        По какому параметру хотите искать? Введите одну или несколько цифр через пробел:
                      
        [0] - Порядковый номер
        [1] - Имя
        [2] - Фамилия
        [3] - Отчество
        [4] - Название организации
        [5] - Рабочий телефон
        [6] - Личный телефон
        [7] - Вернуться в главное меню
                      
        """)

        if "7" in param:
            print("\033[H\033[J")
        else:
            param_list = param.split(" ")
            local_result_list = phonebook_list
            for p in param_list:
                local_result_list = self.find_notes(p, local_result_list)
            return local_result_list
            

    def find_notes(self, param: str, phonebook_list) -> list:
        value = input(f"Введите значение для поиска для параметра {param}: ")
        local_result_list = [note for note in phonebook_list if note[int(param)] == value]
        return local_result_list





one = Phonebook()


def print_page():
    # items_per_page = 10
    # current_page = 1

    # пример списка для вывода
    my_list = one.get_phonebook_from_file(one.FILE_NAME)

    # вычисляем количество страниц
    num_pages = len(my_list) // items_per_page + 1

    while True:
        # выводим элементы списка для текущей страницы
        start_index = (current_page - 1) * items_per_page
        end_index = start_index + items_per_page
        print(my_list[start_index:end_index])
        one.print_phonebook(my_list, start_index, end_index)

        # спрашиваем у пользователя, хочет ли он перейти на другую страницу
        user_input = input("\nEnter page number or 'q' to quit: ")
        if user_input == 'q':
            break

        # обрабатываем пользовательский ввод
        try:
            page_number = int(user_input)
            if page_number < 1 or page_number > num_pages:
                raise ValueError
            current_page = page_number
        except ValueError:
            print("\nInvalid input. Please enter a number between 1 and", num_pages)



def main_menu() -> None:
    # ПОПРОБОВАТЬ ИЗМЕНИТЬ РАЗМЕР ОКНА ТЕРМИНАЛА
    param = input(
    """
    [1] - Показать справочник
    [2] - Добавить новую запись в справочник
    [3] - Редактировать запись
    [4] - Поиск записей по одной или нескольким характеристикам
    [5] - Закрыть приложение
    [6] - test

    """)
    print("\033[H\033[J")

    
    if param == "1":
        one.print_phonebook(one.get_phonebook_from_file(one.FILE_NAME))
    elif param == "2":
        print("TWO")
        one.add_new_note(one.FILE_NAME)
        print("\nЗапись добавлена в справочник.")
    elif param == "3":
       print("THREE")
       tmp = one.get_edit_str()
       print(tmp)
       one.add_edited_note(tmp)
    #    one.add_edited_note(one.get_edit_str())
       print("\nЗапись отредактирована.")
    elif param == "4":  
        one.print_phonebook(one.get_param_for_find(one.get_phonebook_from_file(one.FILE_NAME)))
    elif param == "5":
        exit("Увидимся в следующий раз!\n")
    elif param == "6":
        print_page()
    else:
        print("\033[H\033[J")
        print("\nВы ввели неверный параметр. Попробуйте еще раз:")

    main_menu()




main_menu()
