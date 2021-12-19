from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
from kps_io import PeliIO


def main():
    io = PeliIO()

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

            kaksinpeli = KPSPelaajaVsPelaaja(io)
            kaksinpeli.pelaa()
        elif vastaus.endswith("b"):
            io.kirjoita(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

            yksinpeli = KPSTekoaly(io)
            yksinpeli.pelaa()
        elif vastaus.endswith("c"):
            io.kirjoita(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

            haastava_yksinpeli = KPSParempiTekoaly(io)
            haastava_yksinpeli.pelaa()
        else:
            break


if __name__ == "__main__":
    main()
