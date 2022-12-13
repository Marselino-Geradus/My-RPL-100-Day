#Belajar tipe data List
'''Menghapus item dengan fungsi pop()'''

print('>>>Menghapus item dengan fungsi pop()<<<')
buah = ['Mangga', 'Pisang', 'Jeruk', 'Mangga', 'Naga', 'Nangka']
print(buah)
buah1 = buah.pop(3)
print('##Nama buah yang terhapus : ', buah1, ' di indeks 3.')
print(buah)
print()

print('>>>Menghapus item dengan fungsi remove()<<<')
angka = [2, 4, 6, 8, 7, 8]
print(angka)
print('##Angka yang terhapus (cara 1): ', angka[3], ' di indeks 3.')
a = angka.remove(8)
print(angka)
print('##Angka yang terhapus (cara 2): ', a,'  ==> kenapa hasilnya "none"?')
print()

print('>>>Menghapus item dengan fungsi del()<<<')
nama = ['Amir', 'Beto', 'Budi', 'Mars', 'Mage', 'Mury']
print(nama)
print('##Nama yang dihapus = ', nama[3], ' di indeks 3')
del nama[3]
print(nama)
print()
