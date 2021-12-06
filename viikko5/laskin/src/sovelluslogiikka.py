class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edellinen_arvo = tulos

    def miinus(self, arvo):
        self.edellinen_arvo = self.tulos
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.edellinen_arvo = self.tulos
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos = arvo
