'''Ini adalah soal (2-Ronde 2) dalam lomba Coding War yang diselenggarakan oleh RPL Lab Unsulbar'''

angka = int(input('Masukkan angka: '))
if angka % 3 == 0:
    print('Pride of 3')
elif angka % 5 == 0:
    print('Pride of 5')
elif angka % 3 == 0 and angka % 5 == 0:
    print('Master Class')
else:
    print('Bilangan tidak habis dibagi 3 atau 5')
