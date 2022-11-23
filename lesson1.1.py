txt = int(input("Введите количество строк "))
b=""
c=[]
dict={}
for i in range(txt):
    a=input("Введите строку текста ")
    b+=" " + a
c=b.split()
for j in c:
    if dict.get(j.lower()) == None:
        dict[j.lower()]=1
    else:
        dict[j.lower()]+=1
key1=None
value1=0
dict1={}
for key,value in dict.items():
    if key!=key1 and value>=value1:
        key1=key
        value1=value
        dict1[key1]=value1
print(sorted(dict1.items())[0])



















