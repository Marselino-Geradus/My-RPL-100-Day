#Latih Logika (1)
bil = int(input('Masukkan nilai: '))
if bil < 7:
    print('Alfa')
    print('Omega')
else:
    print('Bravo')

#Latih Logika (2)
while True:
    print()
    a = int(input('>> Masukkan nilai: '))
    if a < 0:
        b = -1
        print(b)
    else:
        if a == 0:
            b = 0
            print(b)
        else:
            b = 1
            print(b)
        break
#Latih Logika (3)
'Mengubah kode berikut dengan If Else'

lulus = False
nilai = int(input('Input: '))
if nilai >= 60:
    lulus1 = True
    print(lulus1)
else:
    print(lulus)
