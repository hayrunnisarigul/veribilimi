import pandas as pd
df = pd.read_excel(r"C:\Users\Acer\OneDrive\Desktop\Veri Bilimi\14. Hafta\data1.xlsx")

urun_verileri = []
for urun in df["Ürün"].unique():
    urun_verileri.append({
        "Ürün": urun,
        "Satildigi_Gun_Sayisi": df.query("Ürün == @urun")["Tarih"].nunique(),
        "Top_Adet": df.query("Ürün == @urun")["Satış adet"].sum()
    })
urun_ozet = pd.DataFrame(urun_verileri)

gun_verileri = []
for tarih in df["Tarih"].unique():
    gun_verileri.append({
        "Tarih": tarih,
        "Urun_Sayisi": df.query("Tarih == @tarih")["Ürün"].nunique(),
        "Top_Adet": df.query("Tarih == @tarih")["Satış adet"].sum()
    })
gun_ozet = pd.DataFrame(gun_verileri)

with pd.ExcelWriter("ozet_tablolar.xlsx", engine="openpyxl") as writer:
    urun_ozet.to_excel(writer, sheet_name="Urun_Ozet", index=False)
    gun_ozet.to_excel(writer, sheet_name="Gun_Ozet", index=False)