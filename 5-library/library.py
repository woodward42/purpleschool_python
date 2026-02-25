# Сделай программу, которая работает с каталогом книг из словаря books и выполняет действие в зависимости от параметра запуска action. Используй модуль sys и получай action из sys.argv[1] (import sys)

# Если action == "filter" - С помощью filter выбери книги переданные в sys.argv[2]. С помощью map выведи список строк "Книга — Автор".

# Если action == "sort" - С помощью map подготовь список строк "Книга — Автор". Отсортируй список по алфавиту в зависимости от author или book.

# импортируем модуль sys
import sys

# словарь
books = [
    {"author": "Пратчетт", "book": "Стража! Стража!"},
    {"author": "Лукьяненко", "book": "Лабиринт отражений"},
    {"author": "Пратчетт", "book": "Шмяк"},
    {"author": "Кристи", "book": "Прилив"},
]

# читаем аргументы запуска скрипта
action = sys.argv[1]
val = sys.argv[2]

# смотрим шо делать
match action:
    case "filter":
        filtered_books = filter(lambda b: b["author"] == val, books)
        formatted_books = list(
            map(lambda b: f"{b['author']} - {b['book']}", filtered_books)
        )
        print("\n".join(formatted_books))

    case "sort":
        sorted_books: list[dict[str, str]] = sorted(books, key=lambda b: b[val])
        formatted_books = list(
            map(lambda b: f"{b['author']} - {b['book']}", sorted_books)
        )
        print("\n".join(formatted_books))
    case _:
        print("Что-то не то с параметрами, друг")
