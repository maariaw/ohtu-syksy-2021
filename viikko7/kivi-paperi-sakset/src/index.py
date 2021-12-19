from pelitehdas import Pelitehdas
from kps_io import PeliIO


def main():
    io = PeliIO()
    tehdas = Pelitehdas()

    while True:
        vastaus = io.lue("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan\n"
              )

        if vastaus.endswith("a"):
            io.kirjoita(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

            kaksinpeli = tehdas.luo_kaksinpeli(io)
            kaksinpeli.pelaa()
        elif vastaus.endswith("b"):
            io.kirjoita(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

            yksinpeli = tehdas.luo_yksinpeli(io)
            yksinpeli.pelaa()
        elif vastaus.endswith("c"):
            io.kirjoita(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

            haastava_yksinpeli = tehdas.luo_haastava_yksinpeli(io)
            haastava_yksinpeli.pelaa()
        else:
            break


if __name__ == "__main__":
    main()
