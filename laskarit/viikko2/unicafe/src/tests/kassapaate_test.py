import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luotu_kassapaate_tiedot_oikeat(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_luotu_kassapaate_edulliset_oikeat(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_luotu_kassapaate_maukkaat_oikeat(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateinen_oikea_vaihtoraha_edullinen_raha_tasa(self):  
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(240), 0)

    def test_kateinen_oikea_vaihtoraha_edullinen_raha_liikaa(self):  
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)

    def test_kateinen_oikea_vaihtoraha_edullinen_raha_liianvahan(self):  
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(230), 230)

    def test_kateinen_oikea_maara_kassassa(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_kateinen_oikea_maara_kassassa_liian_vahan_rahaa(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullinen_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullinen_maara_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateinen_maukas_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(400), 0)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(460), 60)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(230), 230)

    def test_kateinen_maukas_oikea_maara_kassassa(self):
        self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_kateinen_maukas_oikea_maara_myytyja(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kortti_summa_veloitetaan_onnistunut_ostos(self):
        kortti = Maksukortti(1000)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), True)
        self.assertEqual(str(kortti), "saldo: 7.6")
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), True)
        self.assertEqual(str(kortti), "saldo: 3.6")
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kortti_summa_ei_veloitettu_ei_ostosta(self):
        kortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)
        self.assertEqual(str(kortti), "saldo: 2.0")
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)
        self.assertEqual(str(kortti), "saldo: 2.0")
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kortti_kassa_raha_ei_muutu(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortin_lataus(self):
        kortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti,100)
        self.assertEqual(str(kortti), "saldo: 11.0")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)
        self.kassapaate.lataa_rahaa_kortille(kortti,-100)
        self.assertEqual(str(kortti), "saldo: 11.0")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)



