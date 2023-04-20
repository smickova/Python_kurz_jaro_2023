import json

with open ("body.json", encoding='utf-8') as file:
    data = json.load(file)

with open ("bonusy.json", encoding='utf-8') as file:
    data_02 = json.load(file)

hodnoceni = {}

#nejsem si jista, jestli tyto 3 radky jsou spravne
for jmeno in data:  
    if data.keys == data_02.keys:
        data = data[jmeno] + data_02[jmeno]

for jmeno in data:
    if data[jmeno] < 29:
        hodnoceni[jmeno] = ("5")
    if data[jmeno] < 49:
        hodnoceni[jmeno] = ("4")
    if data[jmeno] < 69:
        hodnoceni[jmeno] = ("3")  
    if data[jmeno] < 89:
        hodnoceni[jmeno] = ("2") 
    else:
        hodnoceni[jmeno] = ("1")

with open("znamkovani.json", "w", encoding = 'utf-8') as file:
    json.dump(hodnoceni, file, ensure_ascii=False, indent="")