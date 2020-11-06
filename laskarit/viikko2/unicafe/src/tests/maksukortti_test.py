import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(100)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_luotu_kortti_oikea_saldo(self):
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")

    def test_rahan_lataus_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(str(self.maksukortti), "saldo: 2.0")

    def test_saldo_vahenee(self):
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(str(self.maksukortti), "saldo: 0.0")

    def test_saldo_ei_negativinen(self):
        self.maksukortti.ota_rahaa(200)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")

    def test_oikea_palautus_rahat_riittaa(self):
        self.assertEqual(str(self.maksukortti.ota_rahaa(100)), "True")

    def test_oikea_palautus_rahat_ei_riita(self):
        self.assertEqual(str(self.maksukortti.ota_rahaa(200)), "False")        
