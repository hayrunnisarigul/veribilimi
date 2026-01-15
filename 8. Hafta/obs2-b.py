import pandas as pd
dosya_yolu = "C:\\Users\\Acer\\OneDrive\\Desktop\\Veri Bilimi\\8. Hafta\\obs.xlsx"

df = pd.read_excel(dosya_yolu, sheet_name='OBS2-B', usecols=['Ono', 'Ad', 'Soyad', 'Vize', 'ödev', 'Final', 'ort'])
#groupby, agg
hesapla = df.groupby(['Ono', 'Ad', 'Soyad']).agg(
	ders_sayisi = ('Vize','count'),
	vize_ort = ('Vize','mean'),
	vize_min = ('Vize','min'),
	vize_mak = ('Vize','max'),
	odev_ort = ('ödev','mean'),
	odev_min = ('ödev','min'),
	odev_mak = ('ödev','max'),
	final_ort = ('Final','mean'),
	final_min = ('Final','min'),
	final_mak = ('Final','max'),
	ort_ort = ('ort','mean'),
	ort_min = ('ort','min'),
	ort_mak = ('ort','max')
).reset_index()

hesapla['ders_sayisi'] = hesapla['ders_sayisi'].astype(int)
num_cols = ['vize_ort','vize_min','vize_mak',
            'odev_ort','odev_min','odev_mak',
            'final_ort','final_min','final_mak',
            'ort_ort','ort_min','ort_mak']
hesapla[num_cols] = hesapla[num_cols].round(2)

cols_order = ['Ono','Ad','Soyad','ders_sayisi'] + num_cols
hesapla = hesapla[cols_order]

out_path = "obs2-b_odev.xlsx"
hesapla.to_excel(out_path, index=False)