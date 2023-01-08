'''
- Soal 4/Final Test
- Coding War
- RPL Lab Unsulbar
'''

a = int(input('a = '))
b = int(input('b = '))
hasil = a+b
print('>> Hasil penjumlahan = ',hasil)

if hasil % 2 == 0:
    hasil_genap = hasil + 1
    print('>>> Karena menghasilkan bilangan genap, maka hasil penjumlahan ditambah 1 = ',hasil_genap)
else:
    hasil_ganjil = hasil + 2
    print('>>> Karena menghasilkan bilangan ganjil, maka hasil penjumlahan ditambah 2 = ',hasil_ganjil)