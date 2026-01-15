# 1'den 100'e kadar dolaplar hepsi başta kapalı
dolaplar = {i: False for i in range(1, 101)}

for tur in range(1,51):
    if tur == 25 or tur == 50:
        # 25. ve 50. turda: Tüm dolapların durumu ters çevrilir
        for numara in range(1, 101):
            dolaplar[numara] = not dolaplar[numara]
    else:
        if tur <= 24:
            if tur == 1:
                # 1. tur: 1'in katları açılır
                for numara in range(1, 101):
                    if numara % tur == 0:
                        dolaplar[numara] = True
            elif tur == 2:
                # 2. tur: 2'nin katları kapatılır
                for numara in range(1, 101):
                    if numara % tur == 0:
                        dolaplar[numara] = False
            else:
                # 3-24. turlar
                for numara in range(1, 101):
                    if numara % tur == 0:
                        dolaplar[numara] = not dolaplar[numara]
        else:  # tur 26-49
            n = tur - 24
            if n == 2:
                # 26. tur: 2'nin katları açılır
                for numara in range(1, 101):
                    if numara % n == 0:
                        dolaplar[numara] = True
            elif n == 3:
                # 27. tur: 3'ün katları kapatılır
                for numara in range(1, 101):
                    if numara % n == 0:
                        dolaplar[numara] = False
            else:
                for numara in range(1, 101):
                    if numara % n == 0:
                        dolaplar[numara] = not dolaplar[numara]

print("Açık olan dolaplar:")
for numara, durum in dolaplar.items():
    if durum:
        print(numara)

print("Kapalı olan dolaplar:")
for numara, durum in dolaplar.items():
    if not durum:
        print(numara)