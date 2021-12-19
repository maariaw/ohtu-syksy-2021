from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu
from kps import KPS


class KPSParempiTekoaly(KPS):
    def __init__(self, io):
        super().__init__(io)
        self.tekoaly = TekoalyParannettu(10)

    def _toisen_siirto(self, ensimmaisen_siirto):
        siirto = self.tekoaly.anna_siirto()
        self.io.kirjoita(f"Tietokone valitsi: {siirto}")
        self.tekoaly.aseta_siirto(ensimmaisen_siirto)
        return siirto
