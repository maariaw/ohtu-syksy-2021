from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostokset = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        lukumaarat = map(lambda o: o.lukumaara(), self._ostokset)
        return sum(lukumaarat)
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        hinnat = map(lambda o: o.hinta(), self._ostokset)
        return sum(hinnat)
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        nimi = lisattava.nimi()

        for ostos in self._ostokset:
            if ostos.tuotteen_nimi() == nimi:
                ostos.muuta_lukumaaraa(1)
                return

        self._ostokset.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        nimi = poistettava.nimi()
        poistettava_ostos = list(
            filter(lambda o: o.tuotteen_nimi() == nimi, self._ostokset)
        )[0]

        poistettava_ostos.muuta_lukumaaraa(-1)

        if poistettava_ostos.lukumaara() == 0:
            self._ostokset.remove(poistettava_ostos)

    def tyhjenna(self):
        self._ostokset.clear()

    def ostokset(self):
        return self._ostokset
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
