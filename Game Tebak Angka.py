"Game Tebak Angka"

#VERSI 1

print('='*60)
print('>>> Kami punya sebuah angka. Coba tebak angka tersebut! <<<'.upper())
print('='*60)

while True:
    print()
    print('~'*15)
    tebak = int(input('> Tebakanku: '))
    print('~'*15)
    print()

    if tebak > 15:
        print('>>> Tebakan Anda masih terlalu jauh! Cobalah dengan angka yang lebih kecil.')
    elif tebak < 5:
        print('>>> Tebakan Anda masih terlalu jauh! Cobalah dengan angka yang lebih besar.')
    elif (tebak >= 5 and tebak <10) or (tebak >10 and tebak <= 15):
        print('>>> Tebakan Anda sudah mendekati jawabannya! Coba dengan angka yang lebih dekat.')
    elif tebak == 10:
        print('>>> Yey, tebakan Anda benar! Selamat ya! :)')
        break
    else:
        print('=> Masukan Anda bukan angka! Mohon ulangi.')