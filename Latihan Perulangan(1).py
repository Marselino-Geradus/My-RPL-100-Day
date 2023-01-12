''' Program Bilangan Prima '''
">> Latihan 1"
# while True:
#     x = int(input('~ Masukkan bilangan: '))
#     if x / 1 == x and x / x == 1 and (x % 2 != 0 or x % 3 != 0):
#         print('>>> Termasuk bilangan prima.')
#     else:
#         print('>>> Tidak termasuk bilangan prima.')

# x = int(input('x = '))
# if (x % 2 == 0 or x % 3 == 0):
#     print('good')
# else:
#     print('noo')
    

">> Latihan 2"
def bil_prima(x):
    for i in range(2,x):
        if x  % i == 0:
            return False
    return True

def cari_bil_prima(awal,akhir):
    list_bilangan = []

    for a in range(awal, akhir+1):
        if bil_prima(a):
            list_bilangan.append(a)
    return list_bilangan


print("Bilangan prima antara 1 - 40: ", cari_bil_prima(1, 40))
print("Bilangan prima antara 100 - 500: ",cari_bil_prima(100, 150))
print("Bilangan prima antara 1050 - 1100: ", cari_bil_prima(1050, 1100))
