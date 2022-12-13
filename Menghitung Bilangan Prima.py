def is_prima (x):
    for i in range (2,x):
        if x % i == 0:
            return False

    return True

while True:
    angka = int(input('~ Masukkan angka: '))
    tampil = is_prima(angka)
    if tampil == True:
        print('>> Angka tersebut termasuk bilangan prima.')
        print('-'*43)
    else:
        print('>> Angka tersebut tidak termasuk bilangan prima.')
        print('-'*43)
