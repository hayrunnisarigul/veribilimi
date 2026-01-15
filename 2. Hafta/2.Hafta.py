#Soru 1:
class Kitap:
    def __init__(self,isim, yazar):
        self.isim = isim
        self.yazar = yazar

kitap1 = Kitap("Küçük Prens","Sefiller")
kitap2 = Kitap("Suç ve Ceza", "Dostoyevski")

print(kitap1.isim, "-", kitap1.yazar)
print(kitap2.isim, "-", kitap2.yazar)

#Soru 2:
class HesapMakinesi:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def topla(self):
        return self.a + self.b

    def cikar(self):
        return self.a - self.b

h = HesapMakinesi(10,4)
print("Toplam", h.topla())
print("Fark:",h.cikar())

#Soru 3
class Sinif:      
    def __init__(self,ad=""):
        self.ad = ad
        self.ogrenciler = []
    
    def listele(self):
        print("Sınıftaki Öğrenciler:")
        for ogrenci in self.ogrenciler:
            print("-",ogrenci)

    def ogrenci_ekle(self, ogrenci):
        self.ogrenciler.append(ogrenci)

s = Sinif()
s.ogrenci_ekle("Ayşe")
s.ogrenci_ekle("Mehmet")
s.ogrenci_ekle("Ali")
s.listele()

#Soru 4
class Ogrenci:
    def __init__(self, adsoyad, no, vize, final):
        self.adsoyad = adsoyad
        self.no = no
        self.vize = vize
        self.final = final

    def ortalama(self):
        return ((self.vize * 0.4) + (self.final * 0.6))
    
    def harf_notu(self):
        ort = self.ortalama()
        if ort <= 100 and ort >=80:
            return "AA"
        elif ort < 80 and ort >= 60:
            return "BB"
        elif ort < 60 and ort >= 50:
            return "CC"
        else:
            return "FF"
    
    def yazdir(self):
        print(self.adsoyad, "| No: ", self.no, "| Vize: ", self.vize, "| Final: ", self.final, "| Ortalama: ", self.ortalama(), "| Harf Notu: ", self.harf_notu())
    
ogr1 = Ogrenci("Ali Yılmaz", 101, 40, 50)
ogr2 = Ogrenci("Ayşe Demir", 102, 70, 80)
ogr3 = Ogrenci("Mehmet Kaya", 103, 90, 95)
ogr1.yazdir()
ogr2.yazdir()
ogr3.yazdir()

#KÜTÜPHANE
import pandas as pd
#Soru 5

# Dosyadan sadece gerekli kolonları oku tümü gereksiz
#tail()'de kullanılabilirdi
df = pd.read_excel("C:\\Users\\Acer\\Downloads\\hafta2\\hafta2\\ogrenci.xlsx")[['Ono', 'Ad', 'Soyad', 'Vize', 'Final']]

# Ad ve Soyad'ı birleştirip yeni bir sütun ekle
df['AdSoyad'] = df['Ad'] + " " + df['Soyad']

class Ogrenci:
    def __init__(self, no, adsoyad, vize, final):
        self.no = no
        self.adsoyad = adsoyad
        self.vize = vize
        self.final = final
        self.ort = None
        self.harf = None
        self.durumlar = None

    def ortalama(self):
        return ((self.vize * 0.4) + (self.final * 0.6))
    
    def harf_notu(self):
        ort = self.ortalama()
        if ort <= 100 and ort >=80:
            return "AA"
        elif ort < 80 and ort >= 60:
            return "BB"
        elif ort < 60 and ort >= 50:
            return "CC"
        else:
            return "FF"
    
    def durum(self):
        if self.ortalama() >= 50:
            return "G"
        else:
            return "K"
    
    def hesapla(self):
        self.ort = self.ortalama()
        self.harf = self.harf_notu()
        self.durumlar = self.durum()

    def yazdir(self):
        print(self.no, self.adsoyad, self.vize, self.final, self.ort, self.harf, self.durumlar)

tum_bilgiler = []

for i in range(len(df)):
    ogr = Ogrenci(df['Ono'][i], df['AdSoyad'][i], df['Vize'][i], df['Final'][i])
    ogr.hesapla()
    tum_bilgiler.append([ogr.no, ogr.adsoyad, ogr.vize, ogr.final, ogr.ort, ogr.harf, ogr.durumlar])

print("No | Ad Soyad | Vize | Final | Ortalama | Harf Notu | Durum")
for ogrenci in tum_bilgiler:
    print(f"{ogrenci[0]} | {ogrenci[1]} | {ogrenci[2]} | {ogrenci[3]} | {ogrenci[4]} | {ogrenci[5]} | {ogrenci[6]}")

# Sonuçları CSV'ye kaydet
df_sonuc = pd.DataFrame(tum_bilgiler, columns=["No", "Ad Soyad", "Vize", "Final", "Ortalama", "Harf Notu", "Durum"])
df_sonuc.to_csv("C:\\Users\\Acer\\Downloads\\hafta2\\hafta2\\ogrenciler_odev_sonuc.csv", index=False)
