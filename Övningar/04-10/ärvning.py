class Djur:
    def __init__(self, namn):
        self.namn = namn
    def at():
        print("Djuret åt ett annat djur.")
    def sov():
        print("Djuret somnade")
    
class Fagel(Djur):
    def __init__(self, namn, vinsgpann):
        super().__init__(namn)
        self.vinsgpann = vinsgpann

class Fisk(Djur):
    def __init__(self, namn, maxdjup):
        super().__init__(namn)
        self.maxdjup = maxdjup
    def simma():
        print("Fisken simmar!")

class Haj(Fisk):
    def __init__(self, namn, maxdjup, antalTänder):
        super().__init__(namn, maxdjup)
        self.antalTänder = antalTänder
    def at(djur):
        print(f"Hajen åt {djur.namn}.")

class Torsk(Fisk):
    def __init__(self, namn, maxdjup, hastighet):
        super().__init__(namn, maxdjup)
        self.hastighet = hastighet

torsk1 = Torsk("Felix", 100, 45)
torsk2 = Torsk("Hjalmar", 100, 25)
haj1 = Haj("Betty", 200, 250)

def fånga(haj: Haj, torsk: Torsk):
    return True if haj.maxdjup >= torsk.maxdjup and torsk.hastighet < 30 else False 

print(fånga(haj1, torsk2))
Haj.at(torsk2)
Fisk.simma()
Djur.sov()