try:
    100/0
except ZeroDivisionError:
    print("НА НОЛЬ ДЕЛИТЬ НЕЛЬЗЯ")
except TypeError:
    print("ОШИБКА ТИПА")
else:
    print("ОШИБОК НЕТ")
finally:
    print("ПРОГРАММА РАБОТАЕТ")