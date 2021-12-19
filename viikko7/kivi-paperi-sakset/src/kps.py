from tuomari import Tuomari

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
            tokan_siirto = self.io.lue("Toisen pelaajan siirto: ")

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