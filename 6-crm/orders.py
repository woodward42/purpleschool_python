from typing import TypedDict

# возможные статусы заказа
ORDER_STATES = {"new", "in_progress", "done", "cancelled"}


class Order(TypedDict):
    id: int
    title: str
    amount: float
    email: str
    status: str
    tags: set[str]
    created_at: str
    due: str | None
    closed_at: str

def create_order():
    pass


def list_orders():
    pass


def edit_order():
    pass


def remove_order():
    pass
