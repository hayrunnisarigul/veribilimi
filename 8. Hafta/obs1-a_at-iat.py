import pandas as pd
df = pd.read_excel("C:\\Users\\Acer\\OneDrive\\Desktop\\Veri Bilimi\\8. Hafta\\obs.xlsx", sheet_name='OBS1-A',
                   usecols=['Ono','Ad','Soyad','Vize','ödev','Final','ort'])
#loc, at, iat, query
unique_students = df[['Ono','Ad','Soyad']].drop_duplicates().reset_index(drop=True)
result = pd.DataFrame(columns=['Ono','Ad','Soyad','ders_sayisi',
                               'vize_ort','vize_min','vize_mak',
                               'odev_ort','odev_min','odev_mak',
                               'final_ort','final_min','final_mak',
                               'ort_ort','ort_min','ort_mak'])

for idx in range(len(unique_students)):
    ono = unique_students.iat[idx, 0]
    ad = unique_students.iat[idx, 1]
    soyad = unique_students.iat[idx, 2]

    group = df.query('Ono == @ono & Ad == @ad & Soyad == @soyad')
    ders_sayisi = len(group)

    vize = group.loc[:, 'Vize']
    odev = group.loc[:, 'ödev']
    final = group.loc[:, 'Final']
    ort = group.loc[:, 'ort']

    result.at[idx, 'Ono'] = ono
    result.at[idx, 'Ad'] = ad
    result.at[idx, 'Soyad'] = soyad

    result.at[idx, 'vize_ort'] = vize.mean()
    result.at[idx, 'vize_min'] = vize.min()
    result.at[idx, 'vize_mak'] = vize.max()

    result.at[idx, 'odev_ort'] = odev.mean()
    result.at[idx, 'odev_min'] = odev.min()
    result.at[idx, 'odev_mak'] = odev.max()

    result.at[idx, 'final_ort'] = final.mean()
    result.at[idx, 'final_min'] = final.min()
    result.at[idx, 'final_mak'] = final.max()

    result.at[idx, 'ort_ort'] = ort.mean()
    result.at[idx, 'ort_min'] = ort.min()
    result.at[idx, 'ort_mak'] = ort.max()

num_cols = ['vize_ort','vize_min','vize_mak',
            'odev_ort','odev_min','odev_mak',
            'final_ort','final_min','final_mak',
            'ort_ort','ort_min','ort_mak']
result[num_cols] = result[num_cols].astype(float).round(2)

result.to_excel("C:\\Users\\Acer\\Downloads\\obs1-a_at-iat.xlsx", index=False)