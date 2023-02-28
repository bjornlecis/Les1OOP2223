"""diction = {"naam":"Ben","leeftijd":30}
print(diction)
"""

class persoon:

    aantalPersonen = 0
    aantalHobbies = 0
    def __init__(self,pnaam,pleeftijd,pinteresses):
        self.naam = pnaam
        self.leeftijd = pleeftijd
        self.email = self.naam+".student@syntrapxl.be"
        self.interesses = pinteresses
        persoon.aantalPersonen += 1
        for i in self.interesses:
            persoon.aantalHobbies += 1

    def info(self):
        print("hallo ik ben",self.naam,self.leeftijd)
        print(self.email)
        print("interesses")
        for inter in self.interesses:
            print(inter)
    def toon_aantal_personen(self):
        return self.aantalPersonen
    def toon_aantal_hobbies(self):
        return len(self.interesses)




p1 = persoon("Ben",30,["Voetbal","Wielrennen","Schaken"])
p2 = persoon("Jan",28,["Zwemmen","Lopen"])
p3 = persoon("Ann",35,["Wandelen","Schilderen"])
p4 = persoon("Bert",24,["Games","Programmeren","Dammen","Knikkeren"])
lijst_personen = [p1,p2,p3]

print(p3.toon_aantal_personen())
print(p3.toon_aantal_hobbies())
print(p3.aantalHobbies)

dict_p = p1.__dict__
print(dict_p)
