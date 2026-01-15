import pandas as pd
df = pd.read_excel(r"C:\Users\Acer\OneDrive\Desktop\Veri Bilimi\11. Hafta\hamveri.xlsx")

ws_col = "hiz"
target_col = "TOPRAK_SICAKLIGI_5_°C"

for i in range(1, 6):
    df[f"WS_t-{i}"] = df[ws_col].shift(i)

df_out = df.dropna().copy()

df_out = df_out[[
    "Year", "Month", "Day", "Hour",
    "WS_t-5", "WS_t-4", "WS_t-3", "WS_t-2", "WS_t-1",
    ws_col,
    target_col
]]

output_path = r"C:\Users\Acer\OneDrive\Desktop\Veri Bilimi\11. Hafta\hamveri_sonuc.xlsx"
df_out.to_excel(output_path, index=False)
