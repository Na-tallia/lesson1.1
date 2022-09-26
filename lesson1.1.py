a = input ("Введите сколько вам лет ")
if 0<=int(a)<100:
    if int(a)==0:
        print("Мне", a ,"лет")
    elif 2<=int(str(a))<5:
        print ("Мне" , a , "года")
    elif 5 <=int(a)<= 10:
        print("Мне", a, "лет")
    elif 2<=int(str(a)[0])<10 and int(str(a)[1])==1:
        print ("Мне" , a , "год")
    elif 2<=int(str(a)[0])<10 and 2<=int(str(a)[1])<=4:
        print("Мне" , a , "года")
    elif 1<=int(str(a)[0])<=9 and int(str(a)[1])==0:
        print("Мне", a , "лет")
    elif 95<=int(str(a))<=99:
        print("Мне", a , "лет")
    elif int(a)==1:
        print ("Мне" , a , "год")
else :
    print ("Неправильно введен возраст")
