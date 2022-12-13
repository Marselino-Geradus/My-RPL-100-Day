'''
Program Penentu Bilangan Ganjil/Genap
'''

#Bentuk Dasar
print("# Bentuk Dasar")
a = int(input("Masukkan nilai A: "))
print(">> A adalah bilangan", "genap" if (a % 2 == 0) else "ganjil")
print()


#Bentuk 2 (Menampilkan List Bilangan Genap/Ganjil dari Range Tertentu)
print("#Bentuk 2: Tampilkan Bilangan dengan Range")

while True:
    i = int(input("> Nilai awal: "))
    j = int(input("> Nilai akhir: "))

    print('''
=== Bilangan ===
        1. Ganjil
        2. Genap
''')
    b = int(input("> Tampilkan bilangan (1/2) : "))

    if b not in [1,2]:
        print('Pilihan salah!')
        print('\n==' *2)
        print()
    else:
        for x in range(i,j +1):
            if b == 1 and x % 2 == 1:
                print(x, end=' ')
            elif b == 2 and x % 2 == 0:
                print(x, end=' ')
            else:
                #ganti baris perulangan
                print()
