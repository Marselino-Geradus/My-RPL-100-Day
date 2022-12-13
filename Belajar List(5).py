#Mengurutkan data list
"1. Mengurutkan secara ascending"
print('"1. Mengurutkan secara ascending"')
print('a. Contoh 1')
angka = [1, 4, 5, 2, 6, 9]
print("Bentuk awal: ",angka)
angka.sort()
print('Urutan list: ', angka)
print()

print('b. Contoh 2')
buah = ['nanas', 'apel', 'jeruk', 'sirsak', 'jambu']
print("Bentuk awal: ", buah)
buah.sort()
print('Urutan list: ', buah)
print()

"2. membalikkan posisi item list (tidak harus berurut)"
print('2. Membalikkan posisi item list (tidak harus berurut)')
warna = ['Biru', 'Merah', 'Hijau', 'Kuning']
print("Bentuk awal: ", warna)
warna.reverse()
print('Urutan list: ', warna)
print()

"Menggabungkan dua metode di atas"
print('>>>Menggabungkan dua metode di atas<<<')
warna = ['Biru', 'Merah', 'Hijau', 'Kuning', "Coklat"]
print("Bentuk awal: ", warna)
warna.sort() #datanya diurutkan 
warna.reverse() #baru dibalik
print('Urutan list: ', warna)
print()

