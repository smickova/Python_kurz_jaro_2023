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

 
auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", "47534" )
auto2 = Auto("1P3 4747", "Škoda Octavia", "41253")

auto_uzivatele = input("Jakou znacku si prejete pujcit?")

if auto_uzivatele == "Octavia":
    auto_uzivatele = auto2
else:
    auto_uzivatele = auto1


auto_uzivatele.get_info()
auto_uzivatele.pujc_auto()

