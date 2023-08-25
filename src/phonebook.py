from sys import exit


class Phonebook:

    FILE_NAME = "source.txt"


    def get_phonebook_from_file(self, filename: str) -> list:
        try:
            with open(filename, "r+", encoding="utf-8") as file:
                result = [str.strip("\n").split("*") for str in file.readlines() if str != "\n"]
                return result
        except FileNotFoundError as e:
            print(e)


    def print_phonebook(self) -> None:
        phonebook_list = self.get_phonebook_from_file(self.FILE_NAME)
        print("\n№   | Имя              | Фамилия                 | Отчество                 "
              "| Название организации        | Рабочий телефон   | Личный телефон")
        for note in phonebook_list:
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
            one.print_phonebook()
            main_menu()
        # ДОБАВИТЬ ВАЛИДАЦИЮ ВХОДНЫХ ДАННЫХ
        else:
            phonebook_list = self.get_phonebook_from_file(self.FILE_NAME)
            str_for_edit = ""
            for note in phonebook_list:
                if note[0] == number:
                    line_for_edit = note
            return line_for_edit


    def add_edited_note(self, line_for_edit: list) -> None:
        str_number_in_file = int(line_for_edit[0]) + 1

        param = input("""
        Какой параметр хотите изменить? Введите соответствующую цифру:
        [1] - Имя
        [2] - Фамилия
        [3] - Отчество
        [4] - Название организации
        [5] - Рабочий телефон
        [6] - Личный телефон
        [7] - Закончить редактирование и сохранить запись
        """)

        if param == "7":
            try:
                with open(self.FILE_NAME, "r+", encoding="utf-8") as file:
                    lines = file.readlines()
                    lines.pop(str_number_in_file)
                    lines[str_number_in_file] = "*".join(line_for_edit) + "\n"
                    file.seek(0)
                    file.writelines(lines)
            except FileNotFoundError as e:
                print(e)

        else:
            line_for_edit[int(param)] = input("Введите новое значение: ")
            self.add_edited_note(line_for_edit)

    

one = Phonebook()




def main_menu() -> None:
    # ПОПРОБОВАТЬ ИЗМЕНИТЬ РАЗМЕР ОКНА ТЕРМИНАЛА
    param = input(
    """
    [1] - Показать справочник
    [2] - Добавить новую запись в справочник
    [3] - Редактировать запись
    [4] - Поиск записей по одной или нескольким характеристикам
    [5] - Закрыть приложение
    """)
    print("\033[H\033[J")

    if param == "1":
        one.print_phonebook()
    elif param == "2":
        one.add_new_note(one.FILE_NAME)
        print("Запись добавлена в справочник.")
    elif param == "3":
       one.add_edited_note(one.get_edit_str())
       print("Запись отредактирована.")
    elif param == "4":
        print("тут будет функция поиска записи")
    elif param == "5":
        exit("Увидимся в следующий раз.")
    else:
        print("\033[H\033[J")
        print("Вы ввели неверный параметр. Попробуйте еще раз:")

    main_menu()




main_menu()
