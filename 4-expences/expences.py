# получаем ввод
sum_input = input("Введите сумму в формате <руб> руб <коп> коп: ")

# форматируем
sum_input_formatted = sum_input.strip().lower()

# проверим ввод
sum_input_formatted_list = sum_input_formatted.split(" ")

if len(sum_input_formatted_list) == 2 and not sum_input_formatted_list[0].isnumeric():
    print("Неверный формат суммы в рублях")
    exit()

if len(sum_input_formatted_list) == 4 and (
    not sum_input_formatted_list[0].isnumeric()
    or not sum_input_formatted_list[3].isnumeric()
):
    print("Неверный формат суммы в рублях ИЛИ копейках")
    exit()


rub_splitted_list = sum_input_formatted.split("руб")
rub_amount = rub_splitted_list[0].strip()

if bool(rub_splitted_list[1].strip()):
    kop_splitted_list = rub_splitted_list[1].strip().split("коп")
    kop_amount = int(kop_splitted_list[0].strip())
else:
    kop_amount = 0

print(f"{(int(rub_amount) * 100 + int(kop_amount)) / 100:.2f}")