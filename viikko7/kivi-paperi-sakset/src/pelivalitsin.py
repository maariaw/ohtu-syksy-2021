from pelitehdas import Pelitehdas

class Pelivalitsin:
    def __init__(self, io):
        self.io = io

    def suorita(self):
        tehdas = Pelitehdas()
        while True:
            vastaus = self.io.lue("Valitse pelataanko"
                "\n (a) Ihmistä vastaan"
                "\n (b) Tekoälyä vastaan"
                "\n (c) Parannettua tekoälyä vastaan"
                "\nMuilla valinnoilla lopetetaan\n"
                )
            peliohje = "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"

            if vastaus.endswith("a"):
                self.io.kirjoita(peliohje)

                kaksinpeli = tehdas.luo_kaksinpeli(self.io)
                kaksinpeli.pelaa()
            elif vastaus.endswith("b"):
                self.io.kirjoita(peliohje)

                yksinpeli = tehdas.luo_yksinpeli(self.io)
                yksinpeli.pelaa()
            elif vastaus.endswith("c"):
                self.io.kirjoita(peliohje)

                haastava_yksinpeli = tehdas.luo_haastava_yksinpeli(self.io)
                haastava_yksinpeli.pelaa()
            else:
                break