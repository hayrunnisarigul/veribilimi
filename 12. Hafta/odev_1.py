import pandas as pd
df = pd.read_excel(r'C:\Users\Acer\OneDrive\Desktop\Veri Bilimi\12. Hafta\ogrenci.xlsx')

df['DonemNotu'] = (df['vize'] * 0.4) + (df['final'] * 0.6)

P_YIL = 2324            
P_DONEM = 'GUZ'         
P_AD = 'Ali'
P_SOYAD = 'Kaya'
P_DERS_1 = 'Algoritma 1'
P_DERS_2 = 'Matematik 1'

print(f"\n[1] Bölüm Bazlı Öğrenci ve Dersleri ({P_YIL} {P_DONEM}):")
s1 = df.query("Yilid == @P_YIL and donem == @P_DONEM")
print(s1.filter(items=['Bolum', 'ogrno', 'ad', 'soyad', 'ders']).to_string(index=False))

print(f"\n[2] Fakülte Bazlı Öğrenciler ({P_YIL} {P_DONEM}):")
s2 = df.query("Yilid == @P_YIL and donem == @P_DONEM")
print(s2.groupby(['Fak', 'Bolum', 'ogrno', 'ad', 'soyad']).size().to_string(name='DersSayisi'))

print("\n[3] Bölüm Bazlı Tüm Öğrenciler:")
s3 = df.groupby(['Bolum', 'ogrno', 'ad', 'soyad']).size()
print(s3.to_string(name='KayitSayisi'))

print("\n[4] Fakülte Bazlı Tüm Öğrenciler:")
s4 = df.groupby(['Fak', 'Bolum', 'ogrno', 'ad', 'soyad']).size()
print(s4.to_string(name='KayitSayisi'))

print(f"\n[5] Fakülte Bazlı Ders Sayısı ({P_YIL} {P_DONEM}):")
s5 = df.query("Yilid == @P_YIL and donem == @P_DONEM")
print(s5.groupby('Fak')['ders'].nunique().to_string(dtype=False))

print(f"\n[6] Bölüm Bazlı Ders Sayısı ({P_YIL} {P_DONEM}):")
s6 = df.query("Yilid == @P_YIL and donem == @P_DONEM")
print(s6.groupby('Bolum')['ders'].nunique().to_string(dtype=False))

print(f"\n[7] Fakülte Bazlı Öğrenci Sayısı ({P_YIL} {P_DONEM}):")
s7 = df.query("Yilid == @P_YIL and donem == @P_DONEM")
print(s7.groupby('Fak')['ogrno'].nunique().to_string(dtype=False))

print(f"\n[8] Bölüm Bazlı Öğrenci Sayısı ({P_YIL} {P_DONEM}):")
s8 = df.query("Yilid == @P_YIL and donem == @P_DONEM")
print(s8.groupby('Bolum')['ogrno'].nunique().to_string(dtype=False))

print(f"\n[9] {P_AD} {P_SOYAD} - Tüm Dönemler Dersleri:")
s9 = df.query("ad == @P_AD and soyad == @P_SOYAD")
print(s9.filter(items=['Yilid', 'donem', 'ders', 'DonemNotu']).to_string(index=False))

print(f"\n[10] {P_AD} {P_SOYAD} - {P_YIL} {P_DONEM} Dersleri:")
s10 = df.query("Yilid == @P_YIL and donem == @P_DONEM and ad == @P_AD and soyad == @P_SOYAD")
print(s10.filter(items=['ders', 'DonemNotu']).to_string(index=False))

print(f"\n[11] {P_AD} {P_SOYAD} - Genel Not Ortalaması:")
s11 = df.query("ad == @P_AD and soyad == @P_SOYAD")
print(f"{s11['DonemNotu'].mean():.2f}")

print(f"\n[12] {P_AD} {P_SOYAD} - {P_YIL} {P_DONEM} Not Ortalaması:")
s12 = df.query("Yilid == @P_YIL and donem == @P_DONEM and ad == @P_AD and soyad == @P_SOYAD")
print(f"{s12['DonemNotu'].mean():.2f}")

print(f"\n[13] {P_DERS_1} Dersini Alan Öğrenciler:")
s13 = df[df['ders'].isin([P_DERS_1])]
print(s13.groupby(['ogrno', 'ad', 'soyad', 'Bolum']).size().to_string(name='Adet'))

print(f"\n[14] Hem {P_DERS_1} hem {P_DERS_2} Alan Öğrenciler:")

ders1_alanlar = df.query("ders == @P_DERS_1")['ogrno']

kesisim = df[ (df['ders'] == P_DERS_2) & (df['ogrno'].isin(ders1_alanlar)) ]
print(kesisim.groupby(['ogrno', 'ad', 'soyad']).size().to_string(name='Kesisim'))

ogrt_sayi = df.filter(items=['ogretim']).nunique().values[0]
print(f"Öğretim Elemanı Sayısı : {ogrt_sayi}")

fak_sayi = df.filter(items=['Fak']).nunique().values[0]
print(f"Fakülte Sayısı         : {fak_sayi}")

bol_sayi = df.filter(items=['Bolum']).nunique().values[0]
print(f"Bölüm Sayısı           : {bol_sayi}")

ders_sayi = df.filter(items=['ders']).nunique().values[0]
print(f"Ders Sayısı            : {ders_sayi}")