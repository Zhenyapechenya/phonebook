from sys import exit


class Phonebook:

    def get_phonebook_from_file(self, filename: str) -> list:
        # ТУТ ДОЛЖЕН БЫТЬ СПИСОК СПИСКОВ
        try:
            with open(filename, "r+", encoding="utf-8") as file:
                result = [str.strip("\n").split("*") for str in file.readlines() if str != "\n"]
                return result
        except FileNotFoundError as e:
            print(e)

    def print_phonebook(self, phonebook_list: list) -> None:
        # НЕ ЗАБУДЬ ПЕРЕНЕСТИ ДЛИННУЮ СТРОКУ
        print("\n№   | Имя              | Фамилия                 | Отчество                 | Название организации   | Рабочий телефон   | Личный телефон")
        # print("\033[H\033[J")
        for note in phonebook_list:
            number = note[0]
            name = note[1]
            surname = note[2]
            patronymic = note[3]
            print("{:-<150}".format("-"))
            print("{:<6}{:<19}{:<26}{:<26}".format(number, name, surname, patronymic))


one = Phonebook()
res = one.get_phonebook_from_file("source.txt")


def add_new_note(filename: str) -> None:
    try:
        with open(filename, "a", encoding="utf-8") as file:
            # тут полученные данные должны сохраняться в список,
            # соединяются звездочкой и записываются в файл
            file.write("check"+"\n")
    except FileNotFoundError as e:
        print(e)

#     НУЖНА ФУНКЦИЯ ОБНОВЛЕНИЯ СПИСКА, ПОЛУЧЕННОГО ИЗ ФАЙЛА

def main_menu(prev_param: int = 0) -> None:
    param = input(
        """
    [1] - Показать справочник
    [2] - Добавить новую запись в справочник
    [3] - Редактировать запись
    [4] - Закрыть приложение
    """)

    if param == "1":
        one.print_phonebook(res)
    elif param == "2":
        add_new_note("source.txt")
        print("Запись добавлена в справочник.")
    elif param == "3":
        print("тут будет функция редактирования записи")
    elif param == "4":
        exit("Увидимся в следующий раз.")
    else:
        print("\033[H\033[J")
        print("Вы ввели неверный параметр.")
        prev_param = -1

    main_menu()




main_menu()
