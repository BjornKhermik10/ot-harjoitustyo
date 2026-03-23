import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_rahan_lataaminen_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(2500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 35.00 euroa")
    
    def test_rahan_ottaminen_toimii(self):
        self.maksukortti.ota_rahaa(240)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.60 euroa")
    
    def test_rahan_ottaminen_ei_onnistu(self):
        self.maksukortti.ota_rahaa(1200)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_saldo_euroina_palauttaa_saldon_euroina(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)