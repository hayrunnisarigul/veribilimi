import pandas as pd

def analiz(df, **indeksli_filtreler):
    veri = df.copy()
    for anahtar, deger in indeksli_filtreler.items():
        idx = int(''.join(filter(str.isdigit, anahtar)))

        if isinstance(deger, str):
            maske = veri.iloc[:, idx].astype(str).str.contains(deger, case=False, na=False)
            veri = veri.loc[maske]
        else:
            maske = (veri.iloc[:, idx] == deger)
            veri = veri.loc[maske]

    if len(veri) < 10:
        print(veri.iloc[:, [12, 13, 10, 15]].to_string(index=False))
        if veri.shape[1] > 15:
            print(f" Ort: {veri.iloc[:, 15].mean():.2f}")
            
def kesisim(df, d1, d2):
    k1 = set(df.loc[df.iloc[:, 10].str.contains(d1, case=False, na=False)].iloc[:, 11])
    k2 = set(df.loc[df.iloc[:, 10].str.contains(d2, case=False, na=False)].iloc[:, 11])
    
    ortak = k1.intersection(k2)
    print(f"\n'{d1}' & '{d2}': {len(ortak)} ortak öğrenci.")
    
    if ortak:
        print(df.loc[df.iloc[:, 11].isin(ortak)].iloc[:, [12, 13]].drop_duplicates().to_string(index=False))

df = pd.read_excel(r"C:\Users\Acer\OneDrive\Desktop\Veri Bilimi\11. Hafta\ogrenci.xlsx")

analiz(df, col5="Bilgisayar")

analiz(df, col3="Müh", col6="BAHAR")

analiz(df, col12="Ayşe")

kesisim(df, "Algoritma", "Matematik")