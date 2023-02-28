class dier:

    def __init__(self,naam,soort,geslacht,geluid):
        self.naam = naam
        self.soort = soort
        self.geslacht = geslacht
        self.geluid = geluid

    def toon_naam(self):
        print(self.naam)
    def dier_info(self):
        return "Dier met naam {} is een {}".format(self.naam,self.soort)
    def maak_geluid(self):
        print(self.geluid)

d1 = dier("Samson","Hond","Man","Mow Zeg Gertje")
d1.maak_geluid()


