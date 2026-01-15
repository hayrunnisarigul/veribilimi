class Universite:
    universite_adi = "KSBU Üniversitesi"

class OgretimUyesi:
    def __init__(self, ad, unvan, bolum, dersler):
        self.ad = ad
        self.unvan = unvan
        self.bolum = bolum
        self.dersler = dersler
    
    def dersleri_goster(self):
        print(f"{self.unvan} {self.ad} ({self.bolum}) -> Dersler: {', '.join(self.dersler)}")
    
    @classmethod
    def universite_bilgisi(cls):
        print(f"\nTüm öğretim üyeleri {Universite.universite_adi} bünyesinde görev yapmaktadır.")

class Ogrenci:
    def __init__(self, ad, bolum):
        self.ad = ad
        self.bolum = bolum
        self.dersler = {}
        self.ders_adi = None
        self.vize = None
        self.final = None
    
    def ders_ekle(self, ders_adi, vize, final):
        self.dersler[ders_adi] = {'vize': vize, 'final': final}

    def ortalama(self, ders_adi):
        vize = self.dersler[ders_adi]['vize']
        final = self.dersler[ders_adi]['final']
        return (vize * 0.4) + (final * 0.6)

    def harf_notu(self, ortalama):
        if ortalama <= 100 and ortalama > 90:
            return "AA"
        elif ortalama <= 90 and ortalama > 70:
            return "BB"
        elif ortalama <= 70 and ortalama > 50:
            return "CC"
        else:
            return "FF"

    def hesapla(self):
        for ders_adi in self.dersler:
            ortalama = self.ortalama(ders_adi)
            harf_notu = self.harf_notu(ortalama)
            self.dersler[ders_adi]['ortalama'] = ortalama
            self.dersler[ders_adi]['harf_notu'] = harf_notu

    def listele(self):
        #print(f"{self.ad}, {self.bolum}, {self.dersler}, {self.vize}, {self.final}, {self.ortalama}, {self.harf_notu}")
        print(f"\nÖğrenci: {self.ad}, Bölüm: {self.bolum}")
        print("Ders Notları ve Hesaplanan Ortalama/Harf Notları:")
        for ders, bilgi in self.dersler.items():
            print(f"Ders: {ders} -> Vize: {bilgi['vize']}, Final: {bilgi['final']}, "
                  f"Ortalama: {bilgi['ortalama']:.2f}, Harf Notu: {bilgi['harf_notu']}")


#Öğretim Üyeleri ekle
hoc1 = OgretimUyesi("Mehmet", "Prof. Dr.", "Bilgisayar Mühendisliği", ["Algoritmalar", "Matematik"])
hoc2 = OgretimUyesi("Kadir", "Doç. Dr.", "Fizik", ["Kuantum Mekaniği"])

#Hocaların derslerini göster
hoc1.dersleri_goster()
hoc2.dersleri_goster()

#Üniversite bilgisi (class method)
OgretimUyesi.universite_bilgisi()

#Öğrenciler ekle
ogr1 = Ogrenci("Ayşe", "Bilgisayar Mühendisliği")
ogr2 = Ogrenci("Ahmet", "Bilgisayar Mühendisliği")
ogr3 = Ogrenci("Elif", "Fizik")

#Ders ve not ekleme
ogr1.ders_ekle("Algoritmalar", 60, 80)
ogr1.ders_ekle("Matematik", 40, 50)

ogr2.ders_ekle("Algoritmalar", 70, 90)
ogr2.ders_ekle("Matematik", 50, 70)

ogr3.ders_ekle("Kuantum Mekaniği", 85, 95)

#Hesaplamaları önceden çalıştır
ogr1.hesapla()
ogr2.hesapla()
ogr3.hesapla()

#Öğrencilerin notlarını yazdır
ogr1.listele()
ogr2.listele()
ogr3.listele()