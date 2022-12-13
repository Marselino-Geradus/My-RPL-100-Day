nama = input('Masukkan nama: ')
tanggalBeli = input("Masukkan tanggal: ")

print()
print(">>>Daftar Pengunjung<<<")
print("Nama: ",nama)
print("Tanggal: ",tanggalBeli)


#Ini menggunakan operator percabangan (If Else)
print('''
==A. Produk Baju & Jaket==
1. Baju Kaos Polos
2. Baju Kaos Warna Gradien
3. Jaket Parka
4. Jaket Anti Air
''')

print('''
==B. Produk Celana==
1. Celana Jeans
2. Celana Kain Polos
3. Rok SMA
4. Celana Kain Batik
5. Celana Kain Mamasa
''')
print()

harga = 5e4                                 #untuk baju
harga2 = 7e4
harga3 = 2e5
harga4 = 5e5

harga11 = 2e5                                #untuk celana
harga22 = 1e5
harga33 = 8e4
harga44 = 18e4
harga55 = 15e4                   #150.000 = 15e4

def menu1():
    menu = input(">Pilih Produk (A/B): ")

menu = input(">Pilih Produk (A/B): ")

while True:  
    if menu == 'A' or menu == 'a':
        print('==========')
        
        minat = input("Pilih minat Anda (ketik 'back' untuk ke menu utama): ")
        if minat == "back":
            menu = input(">Pilih Produk (A/B): ")
        elif minat == '1':
            print(">>Harga baju kaos polos: Rp. ",int(harga))
            jumlah = int(input('>>Jumlah barang yang ingin dibeli: '))
            total = harga * jumlah
            print(">>Total pembelian: Rp. ",total)

            uang = int(input(">>Uang tunai yang disetor: "))
            sisa = uang - total
            print(f">>>Sisa kembalian: Rp.{sisa} <<<")
        elif minat == '2':
            print(">>Harga baju kaos warna gradien: Rp. ",harga2)
            jumlah = int(input('>>Jumlah barang yang ingin dibeli: '))
            total = harga2 * jumlah
            print(">>Total pembelian: Rp. ",total)

            uang = int(input(">>Uang tunai yang disetor: "))
            sisa = uang - total
            print(f">>>Sisa kembalian: Rp.{sisa} <<<")
        elif minat == '3':
            print(">>Harga jaket parka: Rp. ",harga3)
            jumlah = int(input('>>Jumlah barang yang ingin dibeli: '))
            total = harga3 * jumlah
            print(">>Total pembelian: Rp. ",total)

            uang = int(input(">>Uang tunai yang disetor: "))
            sisa = uang - total
            print(f">>>Sisa kembalian: Rp.{sisa} <<<")
        elif minat == '4':
            print(">>Harga jaket anti air: Rp. ",harga4)
            jumlah = int(input('>>Jumlah barang yang ingin dibeli: '))
            total = harga4 * jumlah
            print(">>Total pembelian: Rp. ",total)

            uang = int(input(">>Uang tunai yang disetor: "))
            sisa = uang - total
            print(f">>>Sisa kembalian: Rp.{sisa} <<<")
        else:
            print("Pilihan Anda tidak ! Mohon periksa kembali.")
            break

        print()


    elif menu == 'B' or menu == 'b':
        print('==========')

        minat = input("Pilih minat Anda (ketik 'back' untuk ke menu utama): ")
        if minat == '1':
            print(">>Harga celana Jeans: Rp. ",harga11)
            jumlah = int(input('>>Jumlah barang yang ingin dibeli: '))
            total = harga11 * jumlah
            print(">>Total pembelian: Rp. ",total)

            uang = int(input(">>Uang tunai yang disetor: "))
            sisa = uang - total
            print(f">>>Sisa kembalian: Rp.{sisa} <<<")
        elif minat == '2':
            print(">>Harga celana kain polos: Rp. ",harga22)
            jumlah = int(input('>>Jumlah barang yang ingin dibeli: '))
            total = harga22 * jumlah
            print(">>Total pembelian: Rp. ",total)

            uang = int(input(">>Uang tunai yang disetor: "))
            sisa = uang - total
            print(f">>>Sisa kembalian: Rp.{sisa} <<<")
        elif minat == '3':
            print(">>Harga rok SMA: Rp. ",harga33)
            jumlah = int(input('>>Jumlah barang yang ingin dibeli: '))
            total = harga33 * jumlah
            print(">>Total pembelian: Rp. ",total)

            uang = int(input(">>Uang tunai yang disetor: "))
            sisa = uang - total
            print(f">>>Sisa kembalian: Rp.{sisa} <<<")
        elif minat == '4':
            print(">>Harga celana kain batik: Rp. ",harga44)
            jumlah = int(input('>>Jumlah barang yang ingin dibeli: '))
            total = harga44 * jumlah
            print(">>Total pembelian: Rp. ",total)

            uang = int(input(">>Uang tunai yang disetor: "))
            sisa = uang - total
            print(f">>>Sisa kembalian: Rp.{sisa} <<<")
        elif minat == '5':
            print(">>Harga celana kain Mamasa: Rp. ",harga55)
            jumlah = int(input('>>Jumlah barang yang ingin dibeli: '))
            total = harga55 * jumlah
            print(">>Total pembelian: Rp. ",total)
            
            uang = int(input(">>Uang tunai yang disetor: "))
            sisa = uang - total
            print(f">>>Sisa kembalian: Rp.{sisa} <<<")
        else:
            print("Pilihan Anda tidak tersedia! Mohon periksa kembali.")
    else:
        print("Pilihan Anda tidak tersedia! Mohon periksa kembali.")
