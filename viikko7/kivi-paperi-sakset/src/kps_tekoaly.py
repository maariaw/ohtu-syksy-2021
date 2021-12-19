from tuomari import Tuomari
from tekoaly import Tekoaly
from kps import KPS


class KPSTekoaly(KPS):
    def __init__(self, io):
        super().__init__(io)
        self.tekoaly = Tekoaly()

    def _toisen_siirto(self, _):
        siirto = self.tekoaly.anna_siirto()
        self.io.kirjoita(f"Tietokone valitsi: {siirto}")
        return siirto
