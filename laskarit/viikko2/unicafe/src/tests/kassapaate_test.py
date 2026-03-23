import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    ALKUKASSA = 100000
    EDULLINEN_HINTA = 240
    MAUKAS_HINTA = 400

    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_kassapaate_luodaan_onnistuneesti_myynteja0_rahaa1000(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, self.ALKUKASSA)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_toimii_edullinen(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(vaihtoraha, 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa, self.ALKUKASSA + self.EDULLINEN_HINTA)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_toimii_maukas(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, self.ALKUKASSA + self.MAUKAS_HINTA)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisosto_ei_onnistu_edullinen(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, self.ALKUKASSA)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_ei_onnistu_maukas(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(300)

        self.assertEqual(vaihtoraha, 300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, self.ALKUKASSA)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_toimii_edullinen(self):
        kortti = Maksukortti(1000)
        onnistui = self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(str(kortti), "Kortilla on rahaa 7.60 euroa")
        self.assertTrue(onnistui)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, self.ALKUKASSA)

    def test_korttiosto_toimii_maukas(self):
        kortti = Maksukortti(1000)
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(str(kortti), "Kortilla on rahaa 6.00 euroa")
        self.assertTrue(onnistui)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, self.ALKUKASSA)

    def test_korttiosto_ei_onnistu_edullinen(self):
        kortti = Maksukortti(200)
        onnistui = self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")
        self.assertFalse(onnistui)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, self.ALKUKASSA)

    def test_korttiosto_ei_onnistu_maukas(self):
        kortti = Maksukortti(300)
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(str(kortti), "Kortilla on rahaa 3.00 euroa")
        self.assertFalse(onnistui)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, self.ALKUKASSA)

    def test_rahan_lataaminen_kortille_toimii(self):
        kortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti, 2500)

        self.assertEqual(str(kortti), "Kortilla on rahaa 35.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, self.ALKUKASSA + 2500)

    def test_rahan_lataaminen_kortille_negatiivisella_summalla_ei_muuta_tilaa(self):
        kortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti, -100)

        self.assertEqual(str(kortti), "Kortilla on rahaa 10.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, self.ALKUKASSA)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kassassa_rahaa_euroina_palauttaa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)