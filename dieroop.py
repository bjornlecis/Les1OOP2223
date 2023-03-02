class Dier:

    def __init__(self,naam,soort,geslacht,geluid):
        self.naam = naam
        self.soort = soort
        self.geslacht = geslacht
        self.geluid = geluid

    def toon_naam(self):
        return str(self.naam).upper()
    def dier_info(self):
        return "Dier met naam {} is een {}".format(self.naam,self.soort)
    def maak_geluid(self):
        print(self.geluid)

d1 = Dier("Samson", "Hond", "Man", "Mow Zeg Gertje")
d1.maak_geluid()
d2 = Dier("a", "a", "man", "hallo 1")
d3 = Dier("b", "b", "man", "hallo 2")
d4 = Dier("c", "c", "vrouw", "hallo 3")
d5 = Dier("d", "d", "man", "hallo 4")

lijst_dieren = [d1,d2,d3,d4,d5]
for dier in lijst_dieren:
    print(Dier.dier_info(dier))

