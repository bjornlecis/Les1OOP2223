class programeurs:

    def __init__(self,naam,loon,talen):
        self.naam = naam
        self.loon = loon
        self.talen = talen

    def toon_info(self):
        return print("deze persoon {}  en heeft dit bedrag {} ".format(self.naam,self.loon))

    def toon_taal(self):
        print("***************************************")
        print("programmeur beheerst volgende talen")
        print("***************************************")
        for taal in self.talen:
            print(taal)



p1 = programeurs("Dario",3200,["python","java","C++"])
p2 = programeurs("ma",3200,["pyt","java","C++"])
p3 = programeurs("yo",3200,["python","java.script","C++"])
lijst_IT = [p1,p2,p3]

for progr in lijst_IT:
    progr.toon_info()
    progr.toon_taal()

