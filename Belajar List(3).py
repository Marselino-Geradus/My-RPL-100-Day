#Memanggil nilai list dengan slicing tanpa batas.
print('>>>Memanggil nilai list dengan slicing tanpa batas<<<')
sepatu = ['Vans', 'Bintang', 'Nike', 'ProATT']
print(sepatu[0:])
print(sepatu[1:])
print(sepatu[2:])
print(sepatu[3:])
print(sepatu[:0])
print(sepatu[:1])
print(sepatu[:2])
print(sepatu[:3])
print(sepatu[:4])
print()

#Mengubah data dalam list
print('>>>Mengubah data dalam list<<<')
print('1. Mengubah data pertama dalam list')
sepatu[0] = 'Dallas'
print(sepatu)
print()

print('2. Mengubah data terakhir dalam list')
sepatu[3] = 'Adidas'
print(sepatu)
print()

print('3. Mengubah data dalam range list')
sepatu[0:2] = ['Ardiles','Puma']
print(sepatu)
print()
print()


#Menambahkan data ke dalam list
print('>>>Menambahkan data ke dalam list<<<')
buah = ['Mangga', 'Pisang', 'Jambu']

print('1. Menambahkan data di bagian tertentu dalam list (menggunakan insert)')
buah.insert(2, 'Durian')
print(buah)
print()

print('2. Menambahkan data di bagian belakang list (menggunakan append)')
buah.append('Strawberry')
print(buah)
print()
































