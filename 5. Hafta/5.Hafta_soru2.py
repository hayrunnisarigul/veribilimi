import math
sayi = int(input("Sayı giriniz:"))

def answer(sayi):
    #1
    low = 0
    high = sayi
    ans = 0

    #4
    while low <= high:
        #2
        mid = math.floor((low + high) / 2)
        #3
        if mid * mid == sayi:
            return mid
        elif mid * mid < sayi:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans

print(answer(sayi))

    
