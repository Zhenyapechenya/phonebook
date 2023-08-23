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
        # НЕ ЗАБУДЬ ПЕРЕНЕСТИ ДЛИННУЮ СТРОКУ
        print("\n№   | Имя              | Фамилия                 | Отчество                 | Название организации        | Рабочий телефон   | Личный телефон")
        # print("\033[H\033[J")
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

    def add_new_note(self, filename: str) -> None:
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
                # тут полученные данные должны сохраняться в список,
                # соединяются звездочкой и записываются в файл
                file.write(new_note + "\n")
        except FileNotFoundError as e:
            print(e)

    #     НУЖНА ФУНКЦИЯ ОБНОВЛЕНИЯ СПИСКА, ПОЛУЧЕННОГО ИЗ ФАЙЛА


one = Phonebook()
res = one.get_phonebook_from_file(one.FILE_NAME)




def main_menu(prev_param: int = 0) -> None:
    param = input(
        """
    [1] - Показать справочник
    [2] - Добавить новую запись в справочник
    [3] - Редактировать запись
    [4] - Закрыть приложение
    """)

    if param == "1":
        one.print_phonebook()
    elif param == "2":
        one.add_new_note(one.FILE_NAME)
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
