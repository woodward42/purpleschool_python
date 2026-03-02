# получаем ввод
price = int(input("Введите цену: "))
discount = int(input("Введите размер скидки (пример: для 15% введите 15): "))

# считаем
discount_amount = price * (discount / 100)
final_price = price - discount_amount

print(final_price)