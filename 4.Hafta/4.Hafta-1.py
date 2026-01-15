sayi = int(input("Bir sayı giriniz: "))

def sqrt_root(sayi):    
    low = 0
    high = sayi
    ans = 0

    while low <= high:

        mid = (low + high) // 2
        mid_sqrt = mid * mid

        if mid_sqrt == sayi:
            return mid
        
        elif mid_sqrt < sayi:
            ans = mid
            low = mid + 1

        else:
            high = mid - 1

    return ans

print(sqrt_root(sayi))