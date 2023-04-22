
tel_cislo = input("Zadej telefonni cislo:")

def overeni_tel_cisla(cislo):
    if len(cislo) == 9:
        hodnota = True
    elif len(cislo) == 13:
        if cislo[0:4] == "+420":
            hodnota = True
        else:
            hodnota = False
    else:
        hodnota = False
    return hodnota


spravnoste_tel_cisla = overeni_tel_cisla(tel_cislo)
if spravnoste_tel_cisla == False:
    print(f"Zadali jste nespravny format telefonniho cisla.")
else:
    zadana_zprava = input("Zadej zpravu, kterou chcete poslat:")

def vypocet_ceny(zprava):
    zakladni_cena = 3
    delka = len(zprava)//180
    cena = zakladni_cena + (delka * 3)
    return cena

vysledna_cena = vypocet_ceny(zadana_zprava)
print(f"Za vasi zpravu zaplatite: {vysledna_cena} Kc.")
    


