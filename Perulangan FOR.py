#Perulangan
#Perulangan For
#1. For dengan List
print(">1. For dengan List<")

listKota = ['Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo', 'Mamasa', 'Semarang', 'Makassar']
for kota in listKota:
    print(kota)

#mengetahui iterasi for dengan list
print()
print()
print("a). Mengetahui iterasi For dengan List")
for i, kota in enumerate(listKota):
    print(i,kota)

#2. For dengan Fungsi Range()
print()
print()
print(">2. For dengan Fungsi Range()<")
print('>>Contoh 1: menampilkan perulangan biasa (dimulai dari angka nol)<<')
for i in range (5):
    print('Perulangan ke - ',i)

print()
print('>>Contoh 2: dimulai  dari angka yang didefinisikan sendiri<<')
for j in range (10,16):
    print('j = ',j)


print()
print('>>Contoh 3: Mendefinisikan kelipatan suatu angka<<')
for k in range (3,31,3):
    print('k = ',k)


print()
print('>>Contoh 3: Mengulangi suatu pernyataan_(cara1)<<')
for k in range (1,11):
    print('I love you for a 1k years',k)


print()
print('>>Contoh 3: Mengulangi suatu pernyataan_(cara1)<<')
for k in range (0,10):
    print('I love you for a 1k years',k+1)

