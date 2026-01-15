import pandas as pd
import math

df = pd.read_excel("C:\\Users\\Acer\\Downloads\\hafta3\\hafta3\\soru.xlsx")[['öğrenci', 'not']]

sinif_sayisi = int(input("Kaç sınıf oluşturmak istiyorsunuz? (örnek: 5, 7, 10): "))

alt_deger = 0
ust_deger = 100

aralik_genisligi = math.ceil((ust_deger - alt_deger) / sinif_sayisi)

alt_sinir = alt_deger
ust_sinir = alt_sinir + aralik_genisligi

siniflar = []
araliklar = []
frekanslar = []
ortalama_notlar = []

notlar = []
for i in range(len(df)):
    notlar.append(df.iloc[i, 1])

for i in range(len(notlar)):
    for j in range(0, len(notlar) - i - 1):
        if notlar[j] > notlar[j + 1]:
            notlar[j], notlar[j + 1] = notlar[j + 1], notlar[j]

def leq_count(a, x):
    low = 0
    high = len(a) - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] <= x:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans + 1  # eleman sayısı

prefix = [0]
for n in notlar:
    prefix.append(prefix[-1] + n)

def aralik_frekans_toplam(alt, ust):
    sag = leq_count(notlar, ust)
    sol = leq_count(notlar, alt)
    adet = sag - sol
    toplam = prefix[sag] - prefix[sol]
    return adet, toplam

for i in range(1, sinif_sayisi + 1):

    frekans, toplam = aralik_frekans_toplam(alt_sinir, ust_sinir)

    if frekans > 0:
        ortalama = toplam / frekans
    else:
        ortalama = 0  # hiç öğrenci yoksa ortalama 0 olsun
    
    siniflar.append(i)
    araliklar.append(f"({int(alt_sinir)} - {int(ust_sinir)})")
    frekanslar.append(frekans)
    ortalama_notlar.append(round(ortalama, 1))

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
