import pandas as pd

df = pd.read_excel(r"C:\Users\Acer\OneDrive\Desktop\Veri Bilimi\11. Hafta\hamveri.xlsx")
N = len(df)
print(len(df))

cikti_listesi = [df.iloc[5:, 1:5].reset_index(drop=True)]

for col_indis in [5, 6, 7, 8]:
    for i in range(6):
        dilim = df.iloc[i : N-5+i, col_indis].reset_index(drop=True)
        cikti_listesi.append(dilim)

final_df = pd.concat(cikti_listesi, axis=1)

final_df.to_excel("hamverisonuc.xlsx", index=False)