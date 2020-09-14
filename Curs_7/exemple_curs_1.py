class Angajat:
    "Clasa de baza pentru angajati"
    nr_angajati = 0
    _buget_salarial = 10000
    __secrete_de_firma = ["Cod sursa", "Strategie de marketing", "Hardware"]
    __do_not_print = ["_Angajat__cnp", "_Angajat_serie_buletin"]
    
    def __init__(self, nume, salariu):
        self.nume = nume
        self.salariu = salariu
        self.__cnp = "1580408451589"
        Angajat.nr_angajati += 1
        
    def modifica_salariu(self, suma_modificare):
        self.salariu += suma_modificare
        self.__salariu_modificat = True
        
    def print_angajat(self):
        print("nume: {}\nsalariu: {}\n".format(self.nume, self.salariu))
        
    def print_angajat_dinamic(self):
        att = vars(self)
        for key in att.keys():
            #if key not in Angajat.__do_not_print:
            if not key.startswith("_"):
                print("{}: {}".format(key, att[key]))
        
if __name__ == "__main__":
    print("Numar angajati: {}".format(Angajat.nr_angajati))
    ang1 = Angajat("Stefan", 3000)
    print("Numar angajati: {}".format(Angajat.nr_angajati))
    ang1 = Angajat("Mihai", 5000)
    print("Numar angajati: {}".format(Angajat.nr_angajati))
    ang1.print_angajat()
    ang1.modifica_salariu(1000)
    ang1.print_angajat()
    ang1.modifica_salariu(-500)
    ang1.print_angajat()
    
    print(Angajat._buget_salarial)
    print(Angajat._Angajat__secrete_de_firma)
    print(ang1.nume)
    print(ang1.salariu)
    print(ang1._Angajat__cnp)
    
    print(hasattr(ang1, "nume"))
    print(hasattr(ang1, "prenume"))
    print(hasattr(ang1, "__cnp"))
    print(hasattr(ang1, "_Angajat__cnp"))
    
    setattr(ang1, "prenume", "cel Mare")
    print(getattr(ang1, "prenume"))
    setattr(ang1, "nume", "Iuga")
    print(getattr(ang1, "nume"))
    
    print("-"*100)
    
    ang1_attr = vars(ang1)
    print(ang1_attr)
    print("-"*100)
    ang1.print_angajat_dinamic()
    
    print("-"*100)
    delattr(ang1, "prenume")
    ang1.print_angajat_dinamic()