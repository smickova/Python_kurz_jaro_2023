import re

uzivatelske_jmeno = input("Zadej uzivatelske jmeno:")
regularni_vyraz = re.compile(r"[a-zA-Z]{5,10}")
if regularni_vyraz:
    print("Uzivatelske jmeno je spravne.")
else:
    print("Uzivatelske jmeno je nespravne.")
    exit()

uzivatelske_heslo = input("Zadej uzivatelske heslo:")
regularni_vyraz_2 = re.compile(r"[a-zA-Z0-9\_|\-|\.|\+|\=]{12,30}")
#pro kontrolu:
# https://regex101.com/r/3MhNDL/1
vysledek = regularni_vyraz_2.fullmatch(uzivatelske_heslo)
if vysledek:
    print("Uzivatelske heslo je spravne.")
else:
    print("Uzivatelske heslo je nespravne.")
    exit()

uzivatelsky_email = input("Zadej email:")
regularni_vyraz_3 = re.compile(r"[\w\d\"\+\-\.]*[\w\"]+@[\d\w]+\.[\w\-]+(.jp)?")
vysledek_email = regularni_vyraz_3.fullmatch(uzivatelsky_email)
if vysledek_email:
    print("E-mail je v pořádku!")
else:
    print("Nesprávný e-mail!")
    exit()