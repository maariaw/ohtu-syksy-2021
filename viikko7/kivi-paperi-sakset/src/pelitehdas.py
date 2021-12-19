from kps import (
    KPSPelaajaVsPelaaja,
    KPSTekoaly,
    KPSParempiTekoaly
)

class Pelitehdas():
    @staticmethod
    def luo_kaksinpeli(io):
        return KPSPelaajaVsPelaaja(io)

    @staticmethod
    def luo_yksinpeli(io):
        return KPSTekoaly(io)

    @staticmethod
    def luo_haastava_yksinpeli(io):
        return KPSParempiTekoaly(io)
