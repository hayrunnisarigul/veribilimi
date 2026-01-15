import pandas as pd
import math

df = pd.read_excel("C:\\Users\\Acer\\Downloads\\hafta3\\hafta3\\soru.xlsx")[['öğrenci', 'not']]

sinif_sayisi = int(input("Kaç sınıf oluşturmak istiyorsunuz? (örnek: 5, 7, 10): "))

alt_deger = 0
ust_deger = 100

aralik_genisligi = math.ceil((ust_deger - alt_deger) / sinif_sayisi)

# Başlangıç sınırları
alt_sinir = alt_deger
ust_sinir = alt_sinir + aralik_genisligi

# Sonuçları tutmak için boş listeler
siniflar = []
araliklar = []
frekanslar = []
ortalama_notlar = []

for i in range(1, sinif_sayisi + 1):
    
    # O sınıfa düşen öğrencileri filtrele
    sinif_dilim = df[(df['not'] > alt_sinir) & (df['not'] <= ust_sinir)]

    # Öğrenci sayısı (frekans)
    frekans = len(sinif_dilim)
    
    # Not ortalaması
    if frekans > 0:
        ortalama = sinif_dilim['not'].mean()
    else:
        ortalama = 0  # hiç öğrenci yoksa ortalama 0 olsun
    
    # Listelere ekle
    siniflar.append(i)
    araliklar.append(f"({int(alt_sinir)} - {int(ust_sinir)})")
    frekanslar.append(frekans)
    ortalama_notlar.append(round(ortalama, 1))
    
    # Sınırları bir sonraki aralığa kaydır
    alt_sinir = ust_sinir
    ust_sinir += aralik_genisligi

toplam_ogrenci = len(df)
frekans_yuzde = [round((f / toplam_ogrenci) * 100, 2) for f in frekanslar]

sonuc_df = pd.DataFrame({
    "Sınıf": siniflar,
    "Sınıf/Not Aralığı": araliklar,
    "Frekans (Öğrenci Sayısı)": frekanslar,
    "Sınıf Ortalaması": ortalama_notlar,
    "Frekans %": frekans_yuzde
})

print(sonuc_df)
