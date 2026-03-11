# Нужно обработать все возможные ошибки в помощью ошибок:

# Не передан текст фильтра
# Передана кривая команда
# Передан кривой параметр сортировки
# Сделать базовый класс ошибки и расширить нужными ошибками. Обработать их всех и вывести в консоль ошибки.

# импортируем модуль sys
import sys

# словарь
books = [
    {"author": "Пратчетт", "book": "Стража! Стража!"},
    {"author": "Лукьяненко", "book": "Лабиринт отражений"},
    {"author": "Пратчетт", "book": "Шмяк"},
    {"author": "Кристи", "book": "Прилив"},
]


# создаем классы ошибок
class LibraryBaseError(Exception):
    pass


class EmptyFilterError(LibraryBaseError):
    pass


class BadActionError(LibraryBaseError):
    pass


class BadSortParamError(LibraryBaseError):
    pass


try:
    if len(sys.argv) != 3:
        raise BadActionError(
            "Требуется 2 аргумента: action и value (пример: python script.py filter Пратчетт)"
        )

    # читаем аргументы запуска скрипта
    action = sys.argv[1]
    val = sys.argv[2]

    # смотрим шо делать
    match action:
        case "filter":
            if str(val) == "":
                raise EmptyFilterError("Передан пустой фильтр!")

            filtered_books = filter(lambda b: b["author"] == val, books)
            formatted_books = list(
                map(lambda b: f"{b['author']} - {b['book']}", filtered_books)
            )
            print("\n".join(formatted_books))

        case "sort":
            if val not in list(books[0].keys()):
                raise BadSortParamError("Нет такого ключа для сортировки")

            sorted_books: list[dict[str, str]] = sorted(books, key=lambda b: b[val])
            formatted_books = list(
                map(lambda b: f"{b['author']} - {b['book']}", sorted_books)
            )
            print("\n".join(formatted_books))
        case _:
            raise BadActionError("Введен некорректный параметр действия")

except EmptyFilterError as err:
    print(f"[Ошибка]: {err}")

except BadActionError as err:
    print(f"[Ошибка]: {err}")

except BadSortParamError as err:
    print(f"[Ошибка]: {err}")
