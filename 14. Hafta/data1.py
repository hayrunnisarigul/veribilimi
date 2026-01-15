import pandas as pd
df = pd.read_excel(r"C:\Users\Acer\OneDrive\Desktop\Veri Bilimi\14. Hafta\data1.xlsx")

urun_ozet = (
    df.groupby("Ürün", as_index=False)
      .agg(Satildigi_Gun_Sayisi=("Tarih", "nunique"), Top_Adet=("Satış adet", "sum")
      ))

gun_ozet = (
    df.groupby("Tarih", as_index=False)
      .agg(Urun_Sayisi=("Ürün", "nunique"), Top_Adet=("Satış adet", "sum")
      ))

#gun_ozet["Tarih"] = gun_ozet["Tarih"].dt.strftime('%d.%m.%Y')

with pd.ExcelWriter("ozet_tablolar.xlsx", engine="openpyxl") as writer:
    urun_ozet.to_excel(writer, sheet_name="Urun_Ozet", index=False)
    gun_ozet.to_excel(writer, sheet_name="Gun_Ozet", index=False)
