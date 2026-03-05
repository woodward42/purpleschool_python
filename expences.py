# получаем ввод
eda = int(input("Введите траты на еду: "))
transport = int(input("Введите траты на транспорт: "))
razvlecheniya = int(input("Введите траты на развлечения: "))

# считаем
sum = eda + transport + razvlecheniya
avg = sum / 3

print(sum, avg)
