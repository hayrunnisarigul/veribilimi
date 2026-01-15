import pandas as pd

df = pd.read_excel(r'C:\Users\Acer\OneDrive\Desktop\Veri Bilimi\13. Hafta\data1.xlsx')

hafiza = {}

for col in df.columns:
    if df[col].dtype != "object":
        continue

    if col not in hafiza:
        hafiza[col] = {}

    for val in df[col]:
        if val not in hafiza[col]:
            hafiza[col][val] = len(hafiza[col]) + 1

    df[col] = df[col].map(hafiza[col])
df.to_excel("veri_sayisallastirilmis.xlsx", index=False)