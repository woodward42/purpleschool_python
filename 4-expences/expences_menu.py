# Сделать функции:

# add_expense(expenses, value) — добавляет расход
# delete_expence(expenses, index) — удалить расход
# get_total(expenses) — возвращает сумму
# get_average(expenses) — возвращает средний расход
# print_report(expenses) — печатает красивый отчёт


# пункты меню
menu_items = [
    "Добавить расход",
    "Показать все расходы",
    "Показать сумму и средний расход",
    "Удалить расход по номеру",
    "Выход",
]

# список трат
expences_list: list[int] = []


# функция добавления расхода
def add_expense(expences: list[int], value: int):
    expences.append(value)


# функция показа всех расходов
def print_report(expences: list[int]):
    print(f"Список ваших расходов: {expences}")


# функция подсчета суммы всех расходов
def get_total(expences: list[int]):
    return sum(expences)


# функция подсчета среднего расходов
def get_average(expences: list[int]):
    return sum(expences) / len(expences)


# функция удаления расхода по индексу
def delete_expence(expences: list[int], index: int):
    del expences[index]


def main():
    # выбранный пункт меню
    menu_item_selected_code = ""

    while True:
        menu_item_selected_code = input(
            "Выбери пункт меню:\n 1) Добавить расход\n 2) Показать все расходы\n 3) Показать сумму и средний расход\n 4) Удалить расход по номеру\n 99) Выход\n"
        )
        
        # Проверяем выход ПЕРЕД match
        if menu_item_selected_code == "99":
            print("До свидания!")
            break

        match menu_item_selected_code:
            # добавить расход
            case "1":
                expence = int(input("Введите сумму расхода: "))
                add_expense(expences_list, expence)

            # показать все расходы
            case "2":
                print_report(expences_list)

            # показать сумму и средний
            case "3":
                print(
                    f"Сумма расходов: {get_total(expences_list)}\nСредний расход: {get_average(expences_list)}"
                )

            # удалить расход по индексу
            case "4":
                selected_index = int(input("Введите номер расхода: ")) - 1
                delete_expence(expences_list, selected_index)

            case _:
                print("Неизвестный пункт меню")


# запуск программы
main()
