#lanjutan
def nama(isi_nama,t4,tgl):
    print(f'Nama saya adalah {isi_nama}.')
    print(f'Saya lahir di {t4}, {tgl}.')
    print('~'*30)
    print('~'*30)


nama('Marselino Geradus','Makassar','30 Mei 2003')
nama('Titus Solon',"Pana'",'03 Maret 2004')
nama('Taufiq Wahyu Zahra',"Pana'",'12 Juni 2002')

def operator(a,b,c):
    i = a + b
    j = a*c
    k = j/c

    print(f'''
    Nilai a = {a}
    Nilai b = {b}
    Nilai c = {c}
    ''')

    print(f'''
    1). i = a + b
        >> Hasilnya = {i}
    2). j = a * c
        >> Hasilnya = {j}
    3). k = j/c
        >> Hasilnya = {k}

        ''')

operator(2,4,6)
