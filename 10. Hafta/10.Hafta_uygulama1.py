import os
import pandas as pd

klasor = r"C:\Users\Acer\OneDrive\Desktop\Veri Bilimi\10. Hafta\gt"
sonuclar = []

for dosya in os.listdir(klasor):
    if dosya.endswith(".txt"):
        yol = os.path.join(klasor, dosya)
        df = pd.read_table(yol, delimiter=",", header=None)
        df.columns = ["frame", "nesne_id", "a", "b", "c", "d", "e", "f", "g"]

        file_tag = dosya.replace("_gt_whole.txt", "")

        gruplar = df.groupby("nesne_id")

        for nesne_id, grup in gruplar:
            grup["e"] = grup["e"].astype(int)

            grup = grup.sort_values("frame")
            f_first_i = grup["frame"].min()
            f_last_i = grup["frame"].max()

            x1 = ",".join(map(str, sorted(grup["e"].unique())))
            x2 = grup.iloc[0]["f"]
            x3 = grup.iloc[-1]["g"]

            sonuclar.append([
                file_tag,
                nesne_id,
                f_first_i,
                f_last_i,
                x1,
                x2,
                x3
            ])

df_sonuc = pd.DataFrame(
    sonuclar,
    columns=["file", "nesne_id", "f_first_i", "f_last_i", "x1", "x2", "x3"]
)

output_path = r"C:\Users\Acer\Downloads\kosul1_sonuc.xlsx"
df_sonuc.to_excel(output_path, index=False)
