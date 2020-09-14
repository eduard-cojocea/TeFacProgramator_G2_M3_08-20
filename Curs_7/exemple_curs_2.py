class Parinte_1:
    atribut_parinte = 78
    
    def __init__(self):
        print("Constructor parinte 1")
        
    def metodaParinte1(self):
        print("Metoda parinte 1")
        
    def Sulla_Felix_epitaph(self):
        print("No better friend, no worse enemy")
        
class Parinte_2:
    atribut_parinte = 42
    
    def __init__(self):
        print("Constructor parinte 2")
        
    def metodaParinte2(self):
        print("Metoda parinte 2")
        
    def Sulla_Felix_epitaph(self):
        print("No friend ever served me, and no enemy ever wrong me, whom I have not repaid in full.")

class Copil_1(Parinte_1):
    def __init__(self):
        print("Constructor copil 1")
        
    def metodaCopil1(self):
        print("Metoda copil 1")
    
class Copil_2(Parinte_2, Parinte_1):
    def __init__(self):
        print("Constructor copil 2")
        
    def metodaCopil2(self):
        print("Metoda copil 2")    
        
class Copil_3(Parinte_2, Parinte_1):
    def __init__(self):
        print("Constructor copil 3")
        
    def metodaCopil3(self):
        print("Metoda copil 3") 
        
    def Sulla_Felix_epitaph(self):
        print("Patria ingrata, no habes mi ossas")
    

if __name__ == "__main__":
    c1 = Copil_1()
    c2 = Copil_2()
    p1 = Parinte_1()
    c1.metodaCopil1()
    c1.metodaParinte1()
    #c1.metodaParinte2()
    
    c2.metodaCopil2()
    c2.metodaParinte1()
    c2.metodaParinte2()
    c2.Sulla_Felix_epitaph()
    
    c3 = Copil_3()
    c3.Sulla_Felix_epitaph()