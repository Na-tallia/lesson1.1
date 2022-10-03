a=input("Введите пятизначное число ")
max=0
for i in range(0,5):
    if int(a[i])>max:
        max=int(a[i])
print(max)
