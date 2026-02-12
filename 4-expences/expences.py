# захардкодим траты (в дз говорилось, что это допустимо)
payments = [11, 22, 33, 44, 55, 66, 77]

# сумма трат
payments_sum_value = sum(payments)

# минимальная трата
payments_min_value = min(payments)

# максимальная трата
payments_max_value = max(payments)

# среднее значение траты
payments_avg_value = payments_sum_value / len(payments)

# итоговый кортеж для вывода
payments_info_values = (payments_min_value, payments_max_value, payments_sum_value)

print(payments_info_values)
