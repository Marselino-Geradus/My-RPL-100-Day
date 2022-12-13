while True:
    kalimat = input('''Masukkan kalimat: ''').lower()
    t4 = {
        'a' : 0,
        'i' : 0,
        'u' : 0,
        'e' : 0,
        'o' : 0,
        ' ' : 0,
        }
    total_huruf = 0

    for karakter in kalimat:
        if karakter in ['a', 'i', 'u', 'e', 'o', ' ']:
            t4[karakter] += 1
            total_huruf += 1
            
    print('======================')
    print('======Hasil Identifikasi======')
    print(f"> Total karakter (termasuk spasi): {len(kalimat)}")
    print(f"> Total huruf vokal: {total_huruf}")
    print(f"""Rincian: 
    a - {t4['a']}
    i - {t4['i']}
    u - {t4['u']}
    e - {t4['e']}
    o - {t4['o']}
    <spasi> - {t4[' ']}

    """)
    


    print('''Untuk mengetahui jumlah total karakter(huruf) dalam suatu kalimat inputan (tanpa spasi), cukup gunakan rumus ini: 
## total = total karakter - spasi ##<<''')
    print('----------------------------------------')
    a = int(input("> Total karakter (termasuk spasi) yang diketahui: "))
    b = int(input('> Jumlah spasi yang diketahui: '))
    print('Total karakter(huruf) tanpa spasi = ', a-b)
    print('==================================')
    print('==================================')
    print('==================================')
    


#Sebuah catatan penting tentang materi Operator Keanggotaan
"""
print(">>> Berikut ini sebuah catatan penting tentang materi Operator Keanggotaan")
usaha = "Mikro"
print(
    '''apakah 'a' ada di variabel usaha?
Jawaban = ''', 'a' not in usaha
)
"""
