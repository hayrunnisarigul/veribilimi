import pandas as pd

df = pd.read_excel("C:\\Users\\Acer\\OneDrive\\Desktop\\Veri Bilimi\\8. Hafta\\obs.xlsx",
                   sheet_name='OBS1-A',
                   usecols=['Ono','Ad','Soyad','Vize','ödev','Final','ort'])
#iloc
unique_students = []
for i in range(len(df)):
    ono  = df.iloc[i]['Ono']
    ad   = df.iloc[i]['Ad']
    soyad  = df.iloc[i]['Soyad']
    tup  = (ono, ad, soyad)
    if tup not in unique_students:
        unique_students.append(tup)

result = []

for (ono, ad, soyad) in unique_students:

    vize_list  = []
    odev_list  = []
    final_list = []
    ort_list   = []

    for i in range(len(df)):
        if df.iloc[i]['Ono'] == ono and df.iloc[i]['Ad'] == ad and df.iloc[i]['Soyad'] == soyad:
            vize_list.append(df.iloc[i]['Vize'])
            odev_list.append(df.iloc[i]['ödev'])
            final_list.append(df.iloc[i]['Final'])
            ort_list.append(df.iloc[i]['ort'])

    row = {
        'Ono': ono,
        'Ad': ad,
        'Soyad': soyad,
        'vize_ort':  round(sum(vize_list)/len(vize_list), 2),
        'vize_min':  min(vize_list),
        'vize_mak':  max(vize_list),

        'odev_ort':  round(sum(odev_list)/len(odev_list), 2),
        'odev_min':  min(odev_list),
        'odev_mak':  max(odev_list),

        'final_ort': round(sum(final_list)/len(final_list), 2),
        'final_min': min(final_list),
        'final_mak': max(final_list),

        'ort_ort':   round(sum(ort_list)/len(ort_list), 2),
        'ort_min':   min(ort_list),
        'ort_mak':   max(ort_list)
    }

    result.append(row)

df_son = pd.DataFrame(result)
df_son.to_excel("obs1-a_manual.xlsx", index=False)
