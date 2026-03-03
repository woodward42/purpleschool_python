# __main__.py - ТОЧКА ВХОДА программы
import orders
# возможные статусы заказа
ORDER_STATES = {"new", "in_progress", "done", "cancelled"}

def print_menu():
    """Выводит меню программы"""
    print("\n" + "=" * 40)
    print("📋 СИСТЕМА УПРАВЛЕНИЯ ЗАКАЗАМИ")
    print("=" * 40)
    print("1. Показать все заказы")
    print("2. Создать заказ")
    print("3. Изменить заказ")
    print("4. Удалить заказ")
    print("0. Выход")
    print("-" * 40)


def main():
    """Основная функция программы"""
    print("🚀 Запуск системы заказов...")

    # Загрузка уже произошла автоматически в orders.py

    while True:
        print_menu()

        choice = input("Выберите действие (0-4): ").strip()

        if choice == "1":
            orders.list_orders()

        elif choice == "2":
            print("\n➕ Создание заказа")
            title = input("📝 Название: ").strip()
            try:
                amount = float(input("💰 Сумма (₽): "))
                email = input("📧 Email: ").strip()
                print("Статус:", ", ".join(ORDER_STATES))
                status = input("🏷️  Статус (по умолчанию 'new'): ").strip() or "new"
                tags_input = input("🏷️  Теги (через запятую): ").strip()
                tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]
                due = input("📅 Срок (YYYY-MM-DD, Enter-пропустить): ").strip() or None

                result = orders.create_order(title, amount, email, status, tags, due)
                if result:
                    print("✅ Заказ создан!")
                else:
                    print("❌ Ошибка создания заказа")
            except ValueError:
                print("❌ Некорректная сумма")

        elif choice == "3":
            orders.list_orders()
            try:
                order_id = int(input("ID заказа для изменения: "))
                new_title = input("Новое название: ").strip()
                if new_title:
                    if orders.edit_order(order_id, new_title):
                        print("✅ Заказ обновлён")
                    else:
                        print("❌ Заказ не найден")
                else:
                    print("❌ Название не может быть пустым")
            except ValueError:
                print("❌ Введите корректный номер")

        elif choice == "4":
            orders.list_orders()
            try:
                order_id = int(input("ID заказа для удаления: "))
                if orders.remove_order(order_id):
                    print("✅ Заказ удалён")
                else:
                    print("❌ Заказ не найден")
            except ValueError:
                print("❌ Введите корректный номер")

        elif choice == "0":
            print("👋 До свидания! Данные сохранены.")
            break

        else:
            print("❌ Неверный выбор")

        input("\nНажмите Enter для продолжения...")


# ✅ ТОЧКА ВХОДА - выполняется только при прямом запуске
if __name__ == "__main__":
    main()
