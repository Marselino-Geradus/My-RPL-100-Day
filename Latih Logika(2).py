#Mencari mean dari suatu data
'Programnya belum sempurna dan masih ada beberapa yang belum ku pahami'

import statistics
while True:
    '1. Buat Inputan'
    angka = input('Masukkan deret bilangan (pisahkan dengan koma): ')
    data = []

    '~ Konversi inputan ke dalam list yang berisi integer ~'
    for bil in angka.split(', '):
        data.append(int(bil))

    
    rerata = statistics.mean(data)
    print(f'Data --> {data}')
    print(f'Mean --> {rerata}')

    data.sort()
    med = statistics.median(data)
    print(f'Median --> {med}')

    data.sort()
    mod = statistics.mode(data)
    print(f'Modus --> {mod}')
    print('=================')

