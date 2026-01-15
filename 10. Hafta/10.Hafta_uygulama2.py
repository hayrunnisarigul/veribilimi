import os
import pandas as pd

klasor = r"C:\Users\Acer\OneDrive\Desktop\Veri Bilimi\10. Hafta\test"
sonuclar = []

for dosya in os.listdir(klasor):
    if dosya.endswith("_attr.txt"):
        yol = os.path.join(klasor, dosya)

        kolon_isimleri = [
        "daylight", "night", "fog",
        "low-alt", "medium-alt", "high-alt",
        "front-view", "side-view", "bird-view", "long-term"
        ]

        df = pd.read_table(
            yol,
            delimiter=",",
            header=None,
            names=kolon_isimleri
        )

        kosullar = df.iloc[0].tolist()

        file_tag = dosya.replace("_attr.txt", "")

        sonuclar.append([file_tag] + kosullar)

df_sonuc = pd.DataFrame(
    sonuclar,
    columns=["train"] + kolon_isimleri
)

output_path = r"C:\Users\Acer\Downloads\kosul2_sonuc.xlsx"
df_sonuc.to_excel(output_path, index=False)
