class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edellinen_arvo = tulos
        self.edellinen_komento = None

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

    def muista_komento(self, komento_olio):
        self.edellinen_komento = komento_olio
