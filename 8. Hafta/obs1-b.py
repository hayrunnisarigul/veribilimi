import pandas as pd

dosya_yolu = "C:\\Users\\Acer\\OneDrive\\Desktop\\Veri Bilimi\\8. Hafta\\obs.xlsx"
#groupby, agg
df = pd.read_excel(dosya_yolu, sheet_name='OBS1-B',
                   usecols=['Ono', 'Ad', 'Soyad', 'Vize', 'ödev', 'Final', 'ort'])

df = df.reset_index(drop=True)
df['blok_id'] = (df['Ono'] != df['Ono'].shift()).cumsum()

agg = df.groupby(['Ono','Ad','Soyad']).agg(
    ders_sayisi=('Vize','count'),
    vize_ort=('Vize','mean'), vize_min=('Vize','min'), vize_mak=('Vize','max'),
    odev_ort=('ödev','mean'), odev_min=('ödev','min'), odev_mak=('ödev','max'),
    final_ort=('Final','mean'), final_min=('Final','min'), final_mak=('Final','max'),
    ort_ort=('ort','mean'), ort_min=('ort','min'), ort_mak=('ort','max')
).reset_index()

num_cols = ['vize_ort','vize_min','vize_mak',
            'odev_ort','odev_min','odev_mak',
            'final_ort','final_min','final_mak',
            'ort_ort','ort_min','ort_mak']

agg['ders_sayisi'] = agg['ders_sayisi'].astype(int)
agg[num_cols] = agg[num_cols].round(2)

out_path = "obs1-b_odev.xlsx"
agg.to_excel(out_path, index=False)