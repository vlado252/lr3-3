# Запрашиваем у пользователя ввод дня и сохраняем его в переменную day
day = int(input("Введи день:"))
# Запрашиваем у пользователя ввод номера месяца и сохраняем его в переменную month
month = int(input("Введи номер месяца:"))
# Проверяем, относится ли дата к зимнему сезону
if (day >= 1 and day <= 31 and month == 12) or (day >= 1 and day <= 31 and month == 1) or (day >= 1 and day <= 28 and month == 2):
    print("Сезон зима")
# Проверяем, относится ли дата к весеннему сезону
elif (day >= 1 and day <= 31 and month == 3) or (day >= 1 and day <= 30 and month == 4) or (day >= 1 and day <= 31 and month == 5):
    print("Сезон весна")
# Проверяем, относится ли дата к летнему сезону
elif (day >= 1 and day <= 30 and month == 6) or (day >= 1 and day <= 31 and month == 7) or (day >= 1 and day <= 31 and month == 8):
    print("Сезон лето")
# Проверяем, относится ли дата к осеннему сезону
elif (day >= 1 and day <= 30 and month == 9) or (day >= 1 and day <= 31 and month == 10) or (day >= 1 and day <= 30 and month == 11):
    print("Сезон осень")
# Если дата не соответствует ни одному из сезонов, выводим сообщение о неправильной дате
else:
    print("Неправильная дата")

