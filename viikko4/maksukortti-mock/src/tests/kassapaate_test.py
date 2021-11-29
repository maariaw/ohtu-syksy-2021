import unittest
from unittest.mock import Mock, ANY
from kassapaate import Kassapaate, HINTA
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()

    def test_kortilta_velotetaan_hinta_jos_rahaa_on(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo = 10
        
        self.kassa.osta_lounas(maksukortti_mock)

        maksukortti_mock.osta.assert_called_with(HINTA)

    def test_kortilta_ei_veloteta_jos_raha_ei_riita(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo = 4
        
        self.kassa.osta_lounas(maksukortti_mock)

        maksukortti_mock.osta.assert_not_called()

    def test_korttia_ladataan_jos_lataussumma_positiivinen(self):
        maksukortti_mock = Mock()

        self.kassa.lataa(maksukortti_mock, 12)

        maksukortti_mock.lataa.assert_called_with(12)

    def test_korttia_ei_ladata_jos_lataussumma_negatiivinen(self):
        maksukortti_mock = Mock()

        self.kassa.lataa(maksukortti_mock, -20)

        maksukortti_mock.lataa.assert_not_called()
