'''Mencari Mean suatu Data'''
import statistics

while True:
    angka = input('Masukkan deret bilangan (pisahkan dengan tanda koma): ')
    data = []

    for a in angka.split(', '):
        data.append(int(a))

    rerata = statistics.mean(data)
    print(f'Data --> {data}')
    print(f'Mean --> {rerata}')