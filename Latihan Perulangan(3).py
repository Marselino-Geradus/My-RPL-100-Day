'''Mencari Mean suatu Data'''
import statistics

while True:
    angka = input('Masukkan deret bilangan (pisahkan dengan tanda koma dan spasi): ')
    data = []

    for a in angka.split(', ' or ','):
        data.append(int(a))

    data.sort()
    print(f'Data     --> {data}')
    med = statistics.median(data)
    print(f'Median   --> {med}')
