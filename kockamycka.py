class Zak:
    def __init__(self, jmeno, prijmeni, rodne_cislo):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.rodne_cislo = rodne_cislo

    def __eq__(self, other):
        return self.jmeno == other.jmeno and self.prijmeni == other.prijmeni

z1 = Zak("Karel", "Teub", "12345")
