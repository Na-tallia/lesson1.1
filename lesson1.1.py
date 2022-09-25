a=input("Введите дату рождения 1го человека в формате дд.мм.гггг ")
b=input("Введите дату рождения 2го человека дд.мм.гггг ")
if 0<=int(a[0])<=3 and 0<=int(a[1])<=9 and 0<=int(a[3])<=1 and 0<=int(a[4])<=9 and 0<=int(b[0])<=3 and 0<=int(b[1])<=9 and 0<=int(b[3])<=1 and 0<=int(b[4])<=9 and a[2]!="." and a[5]!=".":
    if int(a[6:10])>int(b[6:10]):
        print("Старше второй человек")
    if int(a[6:10])<int(b[6:10]):
        print("Старше первый человек")
    if int(a[6:10]) == int(b[6:10]):
        if int(a[3])>int(b[3]) and int(a[4])>int(b[4]):
            print("Старше второй человек")
        if int(a[3])<int(b[3]):
            print("Старше первый человек")
        if int(a[3])==int(b[3]) and int(a[4])>int(b[4]):
            print("Старше второй человек")
        if int(a[3])==int(b[3]) and int(a[4])<int(b[4]):
            print("Старше первый человек")
        if int(a[3])==int(b[3]) and int(a[4])==int(b[4]):
            print("Возраст одинаковый")
else:
    print("Неправильно введены даты")







