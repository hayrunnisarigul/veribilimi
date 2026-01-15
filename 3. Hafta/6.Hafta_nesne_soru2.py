class Universite:
    universite_adi = "KSBU Üniversitesi"

    def __init__(self, ad):
        self.ad = ad
        self.ogretim_uyeleri = []
        self.ogrenciler = []
    
    def ogretim_uyesi_ekle(self, ogretim_uyesi):
        self.ogretim_uyeleri.append(ogretim_uyesi)

    def ogrenci_ekle(self, ogrenci):
        self.ogrenciler.append(ogrenci)
    
    def universite_bilgisi(self):
        print(f"Toplam öğretim üyesi sayısı: {len(self.ogretim_uyeleri)}\nToplam öğrenci sayısı: {len(self.ogrenciler)}")

    def en_basarili_ogrenci(self):
        en_basarili = self.ogrenciler[0]
        en_yuksek_ort = en_basarili.genel_ortalama()

        for ogr in self.ogrenciler[1:]:
            ort = ogr.genel_ortalama()
            if ort > en_yuksek_ort:
                en_yuksek_ort = ort
                en_basarili = ogr

        print(f"\nEn başarılı öğrenci:\n{en_basarili.ad} ({en_basarili.bolum}) - Ortalama: {en_yuksek_ort:.2f}")

    def sorgula(self, tip, ad_veya_bolum):
        if tip == "ogrenci":
            for ogrenci in self.ogrenciler:
                if (ad_veya_bolum.lower() in ogrenci.ad.lower()) or (ad_veya_bolum.lower() in ogrenci.bolum.lower()):
                    ogrenci.listele()
                else:
                    print("Böyle bir öğrenci bulunamadı.")
        elif tip == "ogretim_uyesi":
            for ogretim_uyesi in self.ogretim_uyeleri:
                if (ad_veya_bolum.lower() in ogretim_uyesi.ad.lower()) or (ad_veya_bolum.lower() in ogretim_uyesi.bolum.lower()):
                    ogretim_uyesi.dersleri_goster()
                else:
                    print("Böyle bir öğretim üyesi bulunamadı.")

class OgretimUyesi:
    def __init__(self, ad, unvan, bolum, dersler):
        self.ad = ad
        self.unvan = unvan
        self.bolum = bolum
        self.dersler = dersler
    
    def dersleri_goster(self):
        print(f"{self.unvan} {self.ad} ({self.bolum}) -> {', '.join(self.dersler)}")

class Ogrenci:
    def __init__(self, ad, bolum):
        self.ad = ad
        self.bolum = bolum
        self.dersler = {}

    def ders_ekle(self, ders, vize, final):
        self.dersler[ders] = {'vize': vize, 'final': final}
    
    def ortalama(self, ders):
        if ders in self.dersler:
            vize = self.dersler[ders]['vize']
            final = self.dersler[ders]['final']
            return (vize * 0.4) + (final * 0.6)
    
    def harf_notu(self, ortalama):
        if ortalama <= 100 and ortalama > 90:
            return "AA"
        elif ortalama <= 90 and ortalama > 70:
            return "BB"
        elif ortalama <= 70 and ortalama > 60:
            return "CC"
        else:
            return "FF"
    
    def hesapla(self):
        for ders in self.dersler:
            ort = self.ortalama(ders)
            harf = self.harf_notu(ort)
            self.dersler[ders]['ort'] = ort
            self.dersler[ders]['harf'] = harf
    
    def genel_ortalama(self):
        toplam = 0
        for ders in self.dersler:
            toplam += self.ortalama(ders)
        return toplam / len(self.dersler)
    
    def listele(self):
        print(f"\nÖğrenci: {self.ad}, Bölüm: {self.bolum}, Üniversite: {Universite.universite_adi}")
        for ders, bilgi in self.dersler.items():
            print(f"{ders} -> Vize: {bilgi['vize']}, Final: {bilgi['final']}, "
                  f"Ortalama: {bilgi['ort']:.2f}, Harf Notu: {bilgi['harf']}")

#Üniversite Oluştur
KSBU_uni = Universite("KSBU Universitesi")

#Öğretim Üyeleri
hoc1 = OgretimUyesi("Mehmet", "Prof.Dr.", "Bilgisayar Mühendisliği", ["Algoritmalar", "Matematik"])
hoc2 = OgretimUyesi("Kadir", "Doç.Dr.", "Fizik", ["Fizik 1"])

KSBU_uni.ogretim_uyesi_ekle(hoc1)
KSBU_uni.ogretim_uyesi_ekle(hoc2)

#Öğrenciler
ogr1 = Ogrenci("Ayşe", "Bilgisayar Mühendisliği")
ogr2 = Ogrenci("Ahmet", "Bilgisayar Mühendisliği")
ogr3 = Ogrenci("Elif", "Fizik")

KSBU_uni.ogrenci_ekle(ogr1)
KSBU_uni.ogrenci_ekle(ogr2)
KSBU_uni.ogrenci_ekle(ogr3)

#Ders ve Not Ekleme
ogr1.ders_ekle("Algoritmalar", 60, 80)
ogr1.ders_ekle("Matematik", 40, 50)

ogr2.ders_ekle("Algoritmalar", 70, 90)
ogr2.ders_ekle("Matematik", 50, 70)

ogr3.ders_ekle("Kuantum Mekaniği", 85, 95)

#Hesaplamalar
ogr1.hesapla()
ogr2.hesapla()
ogr3.hesapla()

#Bilgileri yazdır
KSBU_uni.universite_bilgisi()
print("\nÖğretim Üyeleri:")
for hoca in KSBU_uni.ogretim_uyeleri:
    hoca.dersleri_goster()

print("\nÖğrenciler:")
for ogrenci in KSBU_uni.ogrenciler:
    ogrenci.listele()

#En başarılı öğrenciyi bul
KSBU_uni.en_basarili_ogrenci()

#Öğrenci arama
KSBU_uni.sorgula("ogrenci", "ayşe")
KSBU_uni.sorgula("ogrenci", "bilgisayar")

#Öğretim üyesi arama
KSBU_uni.sorgula("ogretim_uyesi", "mehmet")
KSBU_uni.sorgula("ogretim_uyesi", "fizik")

KSBU_uni.sorgula("ogrenci", "mehmet")