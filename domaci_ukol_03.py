import json

with open ("body.json", encoding='utf-8') as file:
    data = json.load(file)
    
    for jmena in data:
       if data[jmena] < 60:
            print(jmena + " - Fail")
       else:
           print(jmena + " - Pass")

#Výsledný slovník ulož jako JSON do souboru prospech.json
#       json.dump(jmena, data)

