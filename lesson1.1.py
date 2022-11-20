txt = input("Введите текст, разделяя предложения точками. Другие знаки в предложениях не используйте ").split()
dict={}
for i in txt:
    if dict.get(i.lower()) == None:
        dict[i.lower()] = 1
    else:
        dict[i.lower()]+=1
for k,v in dict.items():
    print("Слово", k, "-", v, "раз")















