import argparse
import orders


def cmd_list(args):
    """Обработчик команды list"""
    orders.list_orders(
        overdue=args.overdue,
        tag=args.tag,
        limit=args.limit,
    )


def cmd_add(args):
    """Обработчик команды add"""
    tags = [t.strip() for t in args.tags.split(",") if t.strip()] if args.tags else []
    result = orders.create_order(
        title=args.title,
        amount=args.amount,
        email=args.email,
        tags=tags,
        due=args.due,
    )
    print(f"Заказ создан: {result['id']}")


def cmd_remove(args):
    """Обработчик команды remove"""
    if orders.remove_order(args.id):
        print("Заказ удалён.")
    else:
        print("Заказ не найден.")


def cmd_edit(args):
    """Обработчик команды edit"""
    fields = {}
    if args.title is not None:
        fields["title"] = args.title
    if args.amount is not None:
        fields["amount"] = args.amount
    if args.email is not None:
        fields["email"] = args.email
    if args.due is not None:
        fields["due"] = args.due

    if not fields:
        print("Не указано ни одного поля для редактирования.")
        return

    if orders.edit_order(args.id, **fields):
        print("Заказ обновлён.")
    else:
        print("Заказ не найден.")


def cmd_tags(args):
    """Обработчик команды tags"""
    add_tags = [t.strip() for t in args.add.split(",") if t.strip()] if args.add else None
    rm_tags = [t.strip() for t in args.remove.split(",") if t.strip()] if args.remove else None

    if not add_tags and not rm_tags:
        print("Укажите --add или --remove.")
        return

    if orders.manage_tags(args.id, add=add_tags, remove=rm_tags):
        print("Теги обновлены.")
    else:
        print("Заказ не найден.")


def cmd_status(args):
    """Обработчик команды status"""
    if orders.change_status(args.id, args.new_status):
        print("Статус обновлён.")
    else:
        print("Заказ не найден или недопустимый статус.")


def main():
    parser = argparse.ArgumentParser(description="CRM — управление заказами")
    sub = parser.add_subparsers(dest="command")

    # list
    p_list = sub.add_parser("list", help="Показать заказы")
    p_list.add_argument("--overdue", action="store_true", help="Только просроченные")
    p_list.add_argument("--tag", help="Фильтр по тегу")
    p_list.add_argument("--limit", type=int, help="Ограничить количество")

    # add
    p_add = sub.add_parser("add", help="Добавить заказ")
    p_add.add_argument("--title", required=True, help="Название заказа")
    p_add.add_argument("--amount", type=float, required=True, help="Сумма заказа")
    p_add.add_argument("--email", required=True, help="Email клиента")
    p_add.add_argument("--due", default=None, help="Срок (YYYY-MM-DD)")
    p_add.add_argument("--tags", default=None, help="Теги через запятую")

    # remove
    p_rm = sub.add_parser("remove", help="Удалить заказ")
    p_rm.add_argument("--id", required=True, help="UUID заказа")

    # edit
    p_edit = sub.add_parser("edit", help="Редактировать заказ")
    p_edit.add_argument("--id", required=True, help="UUID заказа")
    p_edit.add_argument("--title", default=None, help="Новое название")
    p_edit.add_argument("--amount", type=float, default=None, help="Новая сумма")
    p_edit.add_argument("--email", default=None, help="Новый email")
    p_edit.add_argument("--due", default=None, help="Новый срок (YYYY-MM-DD)")

    # tags
    p_tags = sub.add_parser("tags", help="Управление тегами")
    p_tags.add_argument("--id", required=True, help="UUID заказа")
    p_tags.add_argument("--add", default=None, help="Добавить теги (через запятую)")
    p_tags.add_argument("--remove", default=None, help="Удалить теги (через запятую)")

    # status
    p_status = sub.add_parser("status", help="Изменить статус")
    p_status.add_argument("--id", required=True, help="UUID заказа")
    p_status.add_argument(
        "new_status",
        metavar="status",
        choices=sorted(orders.ORDER_STATES),
        help=f"Новый статус: {', '.join(sorted(orders.ORDER_STATES))}",
    )

    args = parser.parse_args()

    handlers = {
        "list": cmd_list,
        "add": cmd_add,
        "remove": cmd_remove,
        "edit": cmd_edit,
        "tags": cmd_tags,
        "status": cmd_status,
    }

    handler = handlers.get(args.command)
    if handler:
        handler(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
