import pandas as pd
df = pd.read_excel(r'C:\Users\Acer\OneDrive\Desktop\Veri Bilimi\13. Hafta\data2.xlsx',)

df_hasta = df[df["Hastalık"] == 1]
df_saglam = df[df["Hastalık"] == 0]

df_hasta = df_hasta.sample(frac=1).reset_index(drop=True)
df_saglam = df_saglam.sample(frac=1).reset_index(drop=True)

n_hasta_train = int(len(df_hasta) * 0.7)
n_saglam_train = int(len(df_saglam) * 0.7)

train = pd.concat([
    df_hasta.iloc[:n_hasta_train],
    df_saglam.iloc[:n_saglam_train]
])

test = pd.concat([
    df_hasta.iloc[n_hasta_train:],
    df_saglam.iloc[n_saglam_train:]
])

train = train.sample(frac=1,).reset_index(drop=True)
test  = test.sample(frac=1).reset_index(drop=True)

print(f"Train Veri Sayısı: {len(train)} (%70)")
print(f"Test Veri Sayısı:  {len(test)} (%30)")
print(train.head())
print(test.head())