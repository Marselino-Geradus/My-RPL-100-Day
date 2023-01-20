"Belajar Perpangkatan Python"

#inputan
bilangan = int(input('> Bilangan = '))
pangkat = int(input('> Pangkat = '))


#Dengan operator
hasil = bilangan ** pangkat
print('#Dengan operator')
print('>>> Hasil = ',hasil)

#Dengan Fungsi Bawaan 'pow'
hasil = pow(bilangan,pangkat)
print("#Dengan Fungsi Bawaan 'pow'")
print('>>> Hasil = ',hasil)

#Dengan Perulangan For
hasil = bilangan
for i in range(pangkat - 1):
    hasil *= bilangan

print('#Dengan Perulangan For')
print('>>> Hasil = ',hasil)

#Dengan Perulangan Rekrusif
def hitung_pangkat(bilangan,pangkat):
    if pangkat > 1:
        return bilangan * hitung_pangkat(bilangan,pangkat - 1)
    return bilangan

hasil = hitung_pangkat(bilangan,pangkat)

print('#Dengan Perulangan Rekrusif')
print('>>> Hasil = ',hasil)
