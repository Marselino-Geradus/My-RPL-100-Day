#Menghitung Luas Persegi Dengan Function

def luas_persegi():
    a = int(input('> Sisi: '))
    sisi = a * a
    print(f'>>> Luas persegi tersebut = {sisi} cm.')


def luas_persegi_panjang():
    b = int(input('> Panjang: '))
    c = int(input('> Lebar: '))

    luas = b*c
    print(f'>>> Luas persegi panjang tersebut = {luas} cm.')

print('='*25)
luas_persegi()

print('-'*25)
luas_persegi_panjang()