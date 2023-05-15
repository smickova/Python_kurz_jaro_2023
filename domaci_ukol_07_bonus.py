class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka 
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True
    
    def pujc_auto(self):
        if self.dostupne:
            print("Potvrzuji zapůjčení vozidla")
            self.dostupne = False
        else:
            print("Vozidlo není k dispozici")
    
    def get_info(self):
        print(f"Auto {self.typ_vozidla} s registracni znackou {self.registracni_znacka}.")

    def vrat_auto(self, pocet_dni):
        #self.stav_tachometru = stav_tachometru
        if pocet_dni<7:
            cena = pocet_dni * 400
        else:
            cena = pocet_dni * 400
        print(f"Cena pujcovneho cini:{cena} Kc ")        
        self.dostupne = True

 
auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", "47534" )
auto2 = Auto("1P3 4747", "Škoda Octavia", "41253")

auto_uzivatele = input("Jakou znacku si prejete pujcit?")

if auto_uzivatele == "Octavia":
    auto_uzivatele = auto2
elif auto_uzivatele == "Peugeot":
    auto_uzivatele = auto1
else:
    exit()


auto_uzivatele.get_info()
auto_uzivatele.pujc_auto()

pocet_pujcenych_dni = int(input("Kolid dni jste mel auto pujcene?"))

auto_uzivatele.vrat_auto(pocet_pujcenych_dni)
auto_uzivatele.pujc_auto()


