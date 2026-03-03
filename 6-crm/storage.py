# Реализовать хранение данных заказов.
# В storage.load():
#     если файла нет — вернуть [],
#     при повреждённом JSON — вывести понятное сообщение и вернуть [] (не падать).

# В storage.save(items):
#     Сохранять заказы в файл json

from __future__ import annotations

import json
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from orders import Order

filename = "orders.json"


def load() -> List[Order]:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            file_data = json.load(file)
            return list(file_data)

    except FileNotFoundError:
        print(f"Файл {filename} не найден")
        return []

    except json.JSONDecodeError:
        print(f"Файл {filename} внутри некорректынй JSON")

        return []

    except Exception as e:
        print(f"Неизвестная ошибка при чтении файла: {e}")
        return []


def save(items: List[Order]) -> None:

    try:
        # Открываем файл в режиме записи
        with open(filename, "w", encoding="utf-8") as file:
            # Сохраняем с отступами
            json.dump(items, file, ensure_ascii=False, indent=2)
        print(f"Сохранено {len(items)} заказов в файл {filename}")

    except Exception as e:
        print(f"Ошибка сохранения в файл {filename}: {e}")
