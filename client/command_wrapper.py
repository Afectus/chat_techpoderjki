# author Sergey Romanchuk

# В файле представленна функция обработки входящих строк от пользователя,
# определения является ли строка командой и возвращает коретж
# где 0 элемент команда, 1 элемент -  текст команды.
# если текст не является командой возвращается кортеж: (text, текст введеный пользователем)
# так можно реализовать быстрое выполнение иструкций,
# например #<login user name pass позволит проводить авторизацию пользователя без доп запросов
# Но на сервере надо будет обработать этот кортеж
# команды определяются по наличию вначале символов #< и до ближайшего пробела
import re


def comandProcessing(user_text):
    pattern = r'\#\<[\w]+'
    exit_command = tuple()
    find_comand = re.match(pattern, user_text)
    if find_comand:
        exit_command = (str(find_comand.group())[2:], user_text[find_comand.end():])
        pass
    else:
        exit_command = ('text', user_text)
    return exit_command


if __name__ == '__main__':

    print(comandProcessing("#<user текст который будет передаваться"))


