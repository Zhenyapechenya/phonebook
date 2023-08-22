from sys import exit


class Phonebook:

    def get_phonebook_from_file(self, filename: str) -> list:
        try:
            with open(filename, "r+", encoding="utf-8") as file:
                result = [str.split("*") for str in file.readlines() if str != "\n"]
                return result
        except FileNotFoundError as e:
            print(e)

    def print_phonebook(self, phonebook_list: list) -> None:
        print(
            "\n№   | Имя              | Фамилия                 | Отчество                 | Название организации   | Рабочий телефон   | Личный телефон")
        for note in phonebook_list:
            number = note[0]
            name = note[1]
            surname = note[2]
            patronymic = note[3]
            print("{:-<150}".format("-"))
            print("{:<6}{:<19}{:<26}{:<26}".format(number, name, surname, patronymic))


one = Phonebook()
res = one.get_phonebook_from_file("source.txt")


def start_game():
    prev_param = 0
    param = input(
        """
    [1] - Показать справочник
    [2] - Добавить новую запись в справочник
    [3] - Редактировать запись
    [4] - Закрыть приложение
    """)

    if param == '1':
        print("\033[H\033[J")
        one.print_phonebook(res)
        start_game()
        prev_param = 1
    elif param == '4':
        exit('Увидимся в следующий раз.')
    else:
        print("\033[H\033[J")
        print('Вы ввели неверный параметр.')
        prev_param = -1
        start_game()


start_game()
