'''
Tampilkan deretan bilangan ganjil dengan In Range di rentang angka 100 - 360
'''

b = int(input('''
Ganjil (1) / Genap (2)?
> Tekan 1 atau 2 : '''))


if b in [1,2]:
    for a in range(100, 360+1):
        if b == 1 and a % 2 == 1:
            print(a)
        elif b == 2 and a % 2 == 0:
            print(a)
        else:
            print()
else:
    print('Pilihan salah!')
