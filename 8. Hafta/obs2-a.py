import pandas as pd
dosya_yolu = "C:\\Users\\Acer\\OneDrive\\Desktop\\Veri Bilimi\\8. Hafta\\obs.xlsx"

df = pd.read_excel(dosya_yolu, sheet_name='OBS2-A', usecols=['Ono', 'Ad', 'Soyad', 'Vize', 'ödev', 'Final', 'ort'])
#groupby, agg
hesapla = df.groupby(['Ono', 'Ad', 'Soyad']).agg({
	'Vize': ['mean', 'min', 'max'],
	'ödev': ['mean', 'min', 'max'],
	'Final': ['mean', 'min', 'max'],
	'ort': ['mean', 'min', 'max']
}).reset_index()

hesapla.columns = [
	'Ono', 'Ad', 'Soyad',
	'vize_ort', 'vize_min', 'vize_mak',
	'odev_ort', 'odev_min', 'odev_mak',
	'final_ort', 'final_min', 'final_mak',
	'ort_ort', 'ort_min', 'ort_mak'
]

num_cols = ['vize_ort','vize_min','vize_mak','odev_ort','odev_min','odev_mak',
            'final_ort','final_min','final_mak',
            'ort_ort','ort_min','ort_mak']
hesapla[num_cols] = hesapla[num_cols].round(2)

out_path = "obs2-a_odev.xlsx"
hesapla.to_excel(out_path, index=False)