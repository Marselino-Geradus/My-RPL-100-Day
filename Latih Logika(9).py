#Mengidentifikasi jumlah huruf vokal suatu teks
while True:
    teks = input('Masukkan teks: ').lower()
    hvokal = {
        'a' : 0,
        'i' : 0,
        'u' : 0,
        'e' : 0,
        'o' : 0
    }

    total = 0


    for karakter in teks:
        if karakter in ['a', 'i', 'u', 'e', 'o']:
            hvokal[karakter] += 1
            total += 1

    print(f'Total karakter : {len(teks)}')
    print(f'Total huruf vokal : {total}')

    print(f'''\
        a -> {hvokal ['a']}
        i -> {hvokal ['i']}
        u -> {hvokal ['u']}
        e -> {hvokal ['e']}
        o -> {hvokal ['o']}\
    ''')
            
