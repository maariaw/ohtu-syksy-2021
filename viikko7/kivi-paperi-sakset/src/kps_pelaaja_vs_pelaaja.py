from tuomari import Tuomari
from kps import KPS

class KPSPelaajaVsPelaaja(KPS):
    def _toisen_siirto(self, _):
        return self.io.lue("Toisen pelaajan siirto: ")
