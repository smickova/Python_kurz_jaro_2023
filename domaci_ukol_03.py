import json

with open ("body.json", encoding='utf-8') as file:
    data = json.load(file)

hodnoceni = {}
#klic je jmeno

for jmeno in data:
    if data[jmeno] < 60:
            hodnoceni[jmeno] = ("Fail")
        
    else:
            hodnoceni[jmeno] = ("Pass")


with open("prospech.json", "w", encoding = 'utf-8') as file:
    json.dump(hodnoceni, file, ensure_ascii=False, indent="")



