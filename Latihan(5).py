'''Ini adalah soal (1-Ronde 2) dalam lomba Coding War yang diselenggarakan oleh RPL Lab Unsulbar'''
while True:
    jenis_bilangan = int(input('Masukkan angka: '))
    if jenis_bilangan % 2 == 0:
        print('Bilangan Genap.')

    elif jenis_bilangan % 2 == 1:
        print('You and I, end!')
        break
    else:
        break