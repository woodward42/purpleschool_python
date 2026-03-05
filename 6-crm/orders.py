from typing import TypedDict, Optional
from datetime import datetime, date
import uuid
import storage


ORDER_STATES = {"new", "in_progress", "done", "cancelled"}


class Order(TypedDict):
    id: str
    title: str
    amount: float
    email: str
    status: str
    tags: list[str]
    created_at: str
    due: Optional[str]
    closed_at: Optional[str]


orders: list[Order] = storage.load()


def _find_order(order_id: str) -> Order | None:
    """Поиск заказа по UUID"""
    for order in orders:
        if order["id"] == order_id:
            return order
    return None


def create_order(
    title: str,
    amount: float,
    email: str,
    status: str = "new",
    tags: Optional[list[str]] = None,
    due: Optional[str] = None,
) -> Order:
    """Создание нового заказа с UUID"""
    new_order: Order = {
        "id": str(uuid.uuid4()),
        "title": title,
        "amount": amount,
        "email": email,
        "status": status,
        "tags": tags or [],
        "created_at": str(datetime.now()),
        "due": due,
        "closed_at": None,
    }
    orders.append(new_order)
    storage.save(orders)
    return new_order


def list_orders(
    overdue: bool = False,
    tag: Optional[str] = None,
    limit: Optional[int] = None,
) -> None:
    """Вывод таблицы заказов с фильтрацией"""
    filtered = list(orders)

    if overdue:
        today = date.today()
        filtered = [
            o for o in filtered
            if o.get("due")
            and datetime.strptime(o["due"], "%Y-%m-%d").date() < today
            and o["status"] not in ("done", "cancelled")
        ]

    if tag:
        filtered = [
            o for o in filtered
            if tag in (o.get("tags") or [])
        ]

    if limit is not None:
        filtered = filtered[:limit]

    if not filtered:
        print("Заказов не найдено.")
        return

    header = f"{'ID':<36}  {'Title':<20}  {'Amount':>10}  {'Status':<12}  {'Due':<12}"
    print(header)
    print("-" * len(header))
    for o in filtered:
        due_str = o.get("due") or "—"
        print(
            f"{o['id']:<36}  "
            f"{o['title']:<20}  "
            f"{o['amount']:>10.2f}  "
            f"{o['status']:<12}  "
            f"{due_str:<12}"
        )


def edit_order(order_id: str, **fields) -> bool:
    """Редактирование только переданных полей заказа"""
    order = _find_order(order_id)
    if not order:
        return False

    allowed = {"title", "amount", "email", "due"}
    for key, value in fields.items():
        if key in allowed and value is not None:
            order[key] = value

    storage.save(orders)
    return True


def remove_order(order_id: str) -> bool:
    """Удаление заказа по UUID"""
    for i, order in enumerate(orders):
        if order["id"] == order_id:
            orders.pop(i)
            storage.save(orders)
            return True
    return False


def manage_tags(
    order_id: str,
    add: Optional[list[str]] = None,
    remove: Optional[list[str]] = None,
) -> bool:
    """Управление тегами заказа (множество)"""
    order = _find_order(order_id)
    if not order:
        return False

    current = set(order.get("tags") or [])
    if add:
        current.update(add)
    if remove:
        current -= set(remove)

    order["tags"] = sorted(current)
    storage.save(orders)
    return True


def change_status(order_id: str, new_status: str) -> bool:
    """Изменение статуса заказа с валидацией"""
    if new_status not in ORDER_STATES:
        print(f"Недопустимый статус '{new_status}'. Допустимые: {', '.join(sorted(ORDER_STATES))}")
        return False

    order = _find_order(order_id)
    if not order:
        return False

    order["status"] = new_status
    if new_status in ("done", "cancelled"):
        order["closed_at"] = str(datetime.now())

    storage.save(orders)
    return True
