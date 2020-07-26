sentence = input("Karakterlerin sayılacağı cümleyi giriniz: ")

karakterler = {}

for i in sentence:
    keys = karakterler.keys()
    if i in keys:
        karakterler[i] += 1
    else:
        karakterler[i] = 1

print(karakterler)