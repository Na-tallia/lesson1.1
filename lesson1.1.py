a=input("Введите пятизначное число ")
if int(a[0])>int(a[1]) and int(a[0])>int(a[2]) and int(a[0])>int(a[3]) and int(a[0])>int(a[4]):
    print("Первая цифра больше всех")
elif int(a[1])>int(a[0]) and int(a[1])>int(a[2]) and int(a[1])>int(a[3]) and int(a[1])>int(a[4]):
    print("Вторая цифра больше всех")
elif int(a[3])>int(a[0]) and int(a[3])>int(a[1]) and int(a[3])>int(a[2]) and int(a[3])>int(a[4]):
    print("Четвертая цифра больше всех")
elif int(a[4])>int(a[0]) and int(a[4])>int(a[1]) and int(a[4])>int(a[2]) and int(a[4])>int(a[3]):
    print("Пятая цифра больше всех")
elif int(a[0])==int(a[1]) and int(a[0])> int(a[2]) and int(a[0])>int(a[3]) and int(a[0])>int(a[4]):
    print("Две первые цифры равны и больше всех")
elif int(a[1])==int(a[2]) and int(a[1])>int(a[3]) and int(a[1])>int(a[4]) and int(a[1])>int(a[0]):
    print("Вторая и третяя цифры равны и больше всех")
elif int(a[2])==int(a[3]) and int(a[2])>int(a[4]) and int(a[2])>int(a[0]) and int(a[2])>int(a[1]):
    print("Третяя и четвертая цифры равны и больше всех")
elif int(a[3])==int(a[4]) and int(a[3])>int(a[0]) and int(a[3])>int(a[2]) and int(a[3])>int(a[1]):
    print("Две последние цифры больше всех и равны между собой")
elif int(a[0])==int(a[1]) and int(a[1])==int(a[2]) and int(a[2])>int(a[3]) and int(a[2])>int(a[4]):
    print("Три первые цифры равны и больше всех")
elif int(a[1])==int(a[2]) and int(a[2])==int(a[3]) and int(a[3])>int(a[4]) and int(a[1])>int(a[0]):
    print("2,3 и 4 е цифры равны и больше всех")
elif int(a[2])==int(a[3]) and int(a[2])==int(a[4]) and int(a[4])==int(a[0]) and int(a[4])>int(a[1]):
    print("1,3,4,5 цифры равны и больше второй")
elif int(a[0])==int(a[1]) and int(a[1])==int(a[2]) and int(a[3])==int(a[2]) and int(a[2])>int(a[4]):
    print("Первые 4 цифры равны и больше 5й")
elif int(a[0])==int(a[1]) and int(a[1])==int(a[3]) and int(a[4])==int(a[3]) and int(a[3])>int(a[2]):
    print("1,2,3 и 5 цифры равны и больше 4й")
elif int(a[0])==int(a[1]) and int(a[1])==int(a[3]) and int(a[3])==int(a[4]) and int(a[4])>int(a[2]):
    print("1,2,4,5 цифры равны и больше 3й")
elif int(a[1])==int(a[2]) and int(a[2])==int(a[3]) and int(a[3])==int(a[4]) and int(a[4])>int(a[0]):
    print("Первая цифра меньше остальных четырех равных между собой")
elif int(a[0])==int(a[1])==int(a[2])==int(a[3])==int(a[4]):
    print("Все цифры равны между собой")
elif int(a[0])==int(a[4])>int(a[1]) and int(a[0])>int(a[2]) and int(a[0])>int(a[3]):
    print("Первая и последняя цифра равны и больше всех")
elif int(a[2])>int(a[0]) and int(a[2])>int(a[3]) and int(a[2])>int(a[4]) and int(a[2])>int(a[1]):
    print("Третяя цифра больше всех")
elif int(a[0])==int(a[2]) and int(a[2])>int(a[3]) and int(a[2])>int(a[1]) and int(a[2])>int(a[4]):
    print("Первая и третяя цифры равны и больше всех")
elif int(a[0])==int(a[3]) and int(a[3])>int(a[1]) and int(a[3])>int(a[2]) and int(a[3])>int(a[4]):
    print("Первая и четвертая цифры равны и больше всех")
elif int(a[0])==int(a[4]) and int(a[0])>int(a[1]) and int(a[0])>int(a[2]) and int(a[0])>int(a[3]):
    print("Первая и пятяая цифры равны и больше всех")
elif int(a[1])==int(a[0]) and int(a[0])>int(a[3]) and int(a[0])>int(a[4]) and int(a[0])>int(a[2]):
    print("Первая и вторая цифры равны и больше всех")
elif int(a[1])==int(a[3]) and int(a[1])>int(a[2]) and int(a[1])>int(a[4]) and int(a[1])>int(a[0]):
    print("Вторая и четвертая цифры больше всех")
elif int(a[1])==int(a[4]) and int(a[1])>int(a[0]) and int(a[1])>int(a[2]) and int(a[1])>int(a[3]):
    print("Вторая и пятая цифры больше всех")
elif int(a[2])==int(a[0]) and int(a[0])>int([1]) and int(a[0])>int(a[3]) and int(a[0])>int(a[4]):
    print("Первая и третяя цифры равны")
elif int(a[2])==int(a[1]) and int(a[1])>int(a[0]) and int(a[1])>int(a[3]) and int(a[1])>int(a[4]):
    print("Вторая и третяя цифры равны и больше остальных")
elif int(a[2])==int(a[4]) and int(a[2])>int(a[0]) and int(a[2])>int(a[1]) and int(a[2])>int(a[3]):
    print("Третяя и пятая цифры больше всех")
elif int(a[3])==int(a[0]) and int(a[0])>int(a[1]) and int(a[0])>int(a[2]) and int(a[0])>int(a[4]):
    print("Четвертая и первая цифры равны и больше остальных")
elif int(a[3])==int(a[1]) and int(a[3])>int(a[0]) and int(a[3])>int(a[2]) and int(a[3])>int(a[4]):
    print("Вторая и четвертая цифры равны и больше всех")
elif int(a[3])==int(a[4]) and int(a[3])>int(a[1]) and int(a[3])>int(a[0]) and int(a[3])>int(a[2]):
    print("Четвертая и пятая цифры равны и больше всех")





