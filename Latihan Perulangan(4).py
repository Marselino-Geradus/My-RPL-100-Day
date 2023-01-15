'''Mencari Modus suatu Data'''
import statistics

while True:
    angka = input('Masukkan deret bilangan (pisahkan dengan tanda koma dan spasi): ')
    data = []

    for a in angka.split(', '):
        data.append(int(a))

    data.sort()
    mod = statistics.mode(data)
    print(f'Modus --> {mod}')
    print('=================')