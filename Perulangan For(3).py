#contoh soal perulangan For
'''Soal: buatlah program inputan yang ketika ditampilkan akan menghasilkan simbol bintang berurut seperti berikut
(dengan inputan sebagai batas maksimumnya):
    *
    **
    ***
    dst
'''

'''
simbol = int(input("Masukkan angka: "))
for i in range(1,simbol+1):
    print("*"*i)

 '''

angka1 = int(input("Masukkan angka: "))
for a in range(1,angka1+1):
    print(a,"I love you:)")

angka = 5
for a in range(1,angka+1):
    for b in range(1,a):
        print("-"*b)
    
    
