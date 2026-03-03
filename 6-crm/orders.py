from typing import TypedDict, Optional
# from typing import TypedDict

from datetime import datetime
import storage

# возможные статусы заказа
ORDER_STATES = {"new", "in_progress", "done", "cancelled"}


class Order(TypedDict):
    id: int
    title: str
    amount: float
    email: str
    status: str
    tags: Optional[set[str]]
    created_at: str
    due: Optional[str]
    closed_at: Optional[str]


# переменная для хранения заказов
orders: list[Order] = storage.load()


def create_order(
    title: str,
    amount: float,
    email: str,
    status: str = "new",
    tags: Optional[set[str]] = None,
    due: Optional[str] = None,
):
    new_order: Order = {
        "id": len(orders) + 1,
        "title": title,
        "amount": amount,
        "email": email,
        "status": status,
        "tags": tags,
        "created_at": str(datetime.now()),
        "due": due,
        "closed_at": None,
    }
    orders.append(new_order)
    storage.save(orders)
    return new_order


def list_orders():
    print(f"Список заказов:\n {orders}")


def edit_order(order_id: int, title: str):
    for order in orders:
        if order["id"] == order_id:
            order["title"] = title


def remove_order(order_id: int):
    for i, order in enumerate(orders):
        if order["id"] == order_id:
            orders.pop(i)
            return True
    return False
