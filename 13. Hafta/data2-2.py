import pandas as pd

df = pd.read_excel(
    r'C:\Users\Acer\OneDrive\Desktop\Veri Bilimi\13. Hafta\data2.xlsx',
    sheet_name='data2-2'
)

df_hasta = df[df["Hastalık"] == 1]
df_saglam = df[df["Hastalık"] == 0]

df_hasta = df_hasta.sample(frac=1).reset_index(drop=True)
df_saglam = df_saglam.sample(frac=1).reset_index(drop=True)

k = 5
folds = []

for i in range(k):
    hasta_dilim = df_hasta.iloc[i::k] 
    saglam_dilim = df_saglam.iloc[i::k]
    
    f = pd.concat([hasta_dilim, saglam_dilim])
    folds.append(f)

for i in range(k):
    test = folds[i]
    train = pd.concat([folds[j] for j in range(k) if j != i])

    print(f"\n--- {i+1}. DÖNGÜ ---")
    print(f"Train Satır Sayısı: {len(train)} | Test Satır Sayısı: {len(test)}")
    print("TEST Hastalık Oranı:")
    print(test["Hastalık"].value_counts(normalize=True))
    print(test.head())