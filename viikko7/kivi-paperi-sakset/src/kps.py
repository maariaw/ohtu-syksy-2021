from tuomari import Tuomari
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu

class KPS:
    def __init__(self, io):
        self.io = io

    def pelaa(self):
        tuomari = Tuomari()

        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            self.io.kirjoita(tuomari)

            ekan_siirto = self.io.lue("Ensimmäisen pelaajan siirto: ")
            tokan_siirto = self._toisen_siirto(ekan_siirto)

        self.io.kirjoita("Kiitos!")
        self.io.kirjoita(tuomari)

    def _ensimmaisen_siirto(self):
      return self.io.lue("Ensimmäisen pelaajan siirto: ")

    # tämän metodin toteutus vaihtelee eri pelityypeissä
    def _toisen_siirto(self, ensimmaisen_siirto):
        # metodin oletustoteutus
        return "k"

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"

class KPSPelaajaVsPelaaja(KPS):
    def _toisen_siirto(self, _):
        return self.io.lue("Toisen pelaajan siirto: ")

class KPSTekoaly(KPS):
    def __init__(self, io):
        super().__init__(io)
        self.tekoaly = Tekoaly()

    def _toisen_siirto(self, _):
        siirto = self.tekoaly.anna_siirto()
        self.io.kirjoita(f"Tietokone valitsi: {siirto}")
        return siirto

class KPSParempiTekoaly(KPS):
    def __init__(self, io):
        super().__init__(io)
        self.tekoaly = TekoalyParannettu(10)

    def _toisen_siirto(self, ensimmaisen_siirto):
        siirto = self.tekoaly.anna_siirto()
        self.io.kirjoita(f"Tietokone valitsi: {siirto}")
        self.tekoaly.aseta_siirto(ensimmaisen_siirto)
        return siirto
