import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(10)
        

    def test_konstruktori_asettaa_saldon_oikein(self):
        vastaus = str(self.kortti)
        self.assertEqual(vastaus, "Kortilla on rahaa 10 euroa")

    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_edullisesti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.5 euroa")

    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_maukkaasti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 6 euroa")

    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
        self.kortti.syo_maukkaasti()
        self.kortti.syo_maukkaasti()
        # nyt kortin saldo on 2
        self.kortti.syo_edullisesti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 2 euroa")

    def test_kortille_voi_ladata_rahaa(self):
        self.kortti.lataa_rahaa(25)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 35 euroa")

    def test_kortin_saldo_ei_ylita_maksimiarvoa(self):
        self.kortti.lataa_rahaa(200)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 150 euroa")

    def test_syo_maukas_ei_vie_saldoa_negatiiviseksi(self):
        self.kortti.syo_maukkaasti()
        self.kortti.syo_maukkaasti()
        self.kortti.syo_maukkaasti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 2 euroa")

    def test_neagatiivinen_summa_ei_muuta_saldoa(self):
        self.kortti.lataa_rahaa(-3)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10 euroa")

    def test_kortilla_edullisen_ostaminen_viimeisilla_rahoilla(self):
        self.koyha = Maksukortti(2.5)
        self.koyha.syo_edullisesti()
        self.assertEqual(str(self.koyha), "Kortilla on rahaa 0.0 euroa")
    
    def test_kortilla_maukkaan_ostaminen_viimeisilla_rahoilla(self):
        self.koyha2 = Maksukortti(4)
        self.koyha2.syo_maukkaasti()
        self.assertEqual(str(self.koyha2), "Kortilla on rahaa 0 euroa")
