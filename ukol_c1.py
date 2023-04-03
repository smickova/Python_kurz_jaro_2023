# 1. ukol
jmeno = "Radka"

print(jmeno + "@czechitas.cz")

#bonus
jmeno_a_prijmeni = input("Zadej své jméno a příjmení: ")

#všechna písmena velká
print(jmeno_a_prijmeni.upper())

# všechna písmena malá 
print(jmeno_a_prijmeni.lower())

#standardní varianta - první písmeno velké, další malá
str.split(jmeno_a_prijmeni)

jmeno_a_prijmeni = str.split(jmeno_a_prijmeni)
jmeno = jmeno_a_prijmeni[0]
jmeno = str.split(jmeno)

prijmeni = jmeno_a_prijmeni[1]
prijmeni = str.split(prijmeni)

jmeno = (jmeno[0][0].upper() + jmeno[0][1:])
prijmeni = (prijmeni[0][0].upper() + prijmeni[0][1:])
print(jmeno + " " + prijmeni)

#inicialy
iniciala_jmeno = jmeno[0][0].upper()
iniciala_prijmeni = prijmeni[0][0].upper()
print(iniciala_jmeno + "." + iniciala_prijmeni + ".")

# křestní jméno zkrácené na první písmeno a příjmení, pokud je křestní jméno delší než 5 znaků
pocet_pismen = int(len(jmeno))
if pocet_pismen > 5:
    print(iniciala_jmeno + ". " + prijmeni)
else:
    print(jmeno + " " + prijmeni)