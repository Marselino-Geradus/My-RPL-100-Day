"Game Tebak Angka"

#VERSI 2

import random       #modul untuk memanggil angka acak

angka_rahasia = random.randint(1,15)   #randint = fungsi untuk mengacak angka bil bul sesuai argumen yang kita berikan
print('='*60)
print('>>> Kami punya sebuah angka. Coba tebak angka tersebut! <<<'.upper())
print('='*60)

#Jika kita ingin meminta user memasukkan inputan tanpa ada batasnya, gunakan "while True"
"""while True:
    print('bla bla bla')""" #kode program yang ingin dieksekusi


#Namun, kali ini kita akan membatasi berapa kali user bisa menebak. Untuk itu, kita memakai perulangan "for-else"
batas_menebak = 3

for menebak in range(batas_menebak):
    print()
    print('~'*15)
    tebak = int(input(f'[Percobaan {menebak+1}] >> Tebakanku: '))
    print('~'*15)
    print()

    if tebak == angka_rahasia:
        print('>>> Yey, tebakan Anda benar! Selamat ya! :)')
        break
    else:
        print(
            '>>> Tebakan Anda masih jauh! Cobalah dengan angka yang lebih', 
            'kecil.' if tebak > angka_rahasia else 'besar.'
        )
else:
    print()
    print('-'*73)
    print(f'Mohon maaf, kesempatan Anda telah habis. Anda telah menebak sebanyak {batas_menebak}x!')
    








"=================================================================="
"Alternatif lain menggunakan if else"
# while True:
#     angka = 12
#     jawab = int(input('tebak: '))
#     if jawab == angka:
#         print('Selamat!')
#     else:
#         print(
#             'Tebakanmu masih jauh. Cobalah angka yang lebih',
#             'kecil' if jawab > angka else 'besar'
#         )
"=================================================================="