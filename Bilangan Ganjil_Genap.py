angka = int(input('Masukkan angka: '))
def genap():
    for i in range (0,angka+2):
        if i % 2 == 0:
            print(i,end=' ')
            
def ganjil():
    for i in range (0,angka):
        if i % 2 != 0:
            print(i, end=' ')

print('>>> Angka genap di range 0 sampai ',angka)
genap()

print()

print('\n>>> Angka ganjil di range 0 sampai ',angka)
ganjil()