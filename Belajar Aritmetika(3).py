print()
print('----------------------------------------')
print('=====Kalkulator Sederhana=====')
print('----------------------------------------')

print('''
===========================
                            TOKO KUE
===========================

===========================
                        >Menu Makanan<
===========================
------------------------------------------
|Kode|   Nama Kue    |          Harga       |
------------------------------------------
|   1   |   Deppatori'   | Rp. 7000/mika |
|   2   |   Onde-onde  | Rp. 5000/mika |
|   3   |        Baje'        | Rp. 5000/mika |


===========================
                        >Menu Minuman<
===========================
----------------------------------------------
|Kode| Nama Minuman |         Harga        |
----------------------------------------------
|   1   |       Jus Jambu      | Rp. 7000/gelas |
|   2   |       Jus Jeruk        | Rp. 7000/gelas |
|   3   |      Jus Mangga    | Rp. 7000/gelas |

===========================
                        >Selamat Menikmati:)<
===========================

''')

print('Anda mau pesan apa? \nTekan 1 jika ingin memilih menu makanan.\nTekan 2 jika ingin memilih menu minuman.')

opsi = int(input('1 or 2: '))
if opsi == 1:
    kode = input('Masukkan kode: ')
    n = int(input('Jumlah pesan: '))
    if kode == '1':
        print()
        harga = 7000
        total = harga*n
        print('---')
        print(f"Pesanan Anda: \nKode: {kode} \nNama Makanan: Deppatori'  \nHarga: Rp. {harga}/mika \nJumlah Pesan: {n} \nJumlah yang harus dibayar: Rp. {total}")
        print('---')
        print('------Terima Kasih-----')
    
    elif kode == '2':
        print()
        harga = 5000
        total = harga*n
        print('---')
        print(f'Pesanan Anda: \nKode: {kode} \nNama Makanan: Onde-onde \nHarga: Rp. {harga}/mika \nJumlah Pesan: {n} \nJumlah yang harus dibayar: Rp. {total}')
        print('---')
        print('------Terima Kasih-----')

    elif kode == '3':
        print()
        harga = 5000
        total = harga*n
        print('---')
        print(f"Pesanan Anda: \nKode: {kode} \nNama Makanan: Baje' \nHarga: Rp. {harga}/mika \nJumlah Pesan: {n} \nJumlah yang harus dibayar: Rp. {total}")
        print('---')
        print('------Terima Kasih-----')
    else:
        print('Mohon maaf, pilihan Anda tidak tersedia! Mohon periksa kembali.')

elif opsi == 2:
    kode = input('Masukkan kode: ')
    n = int(input('Jumlah pesan: '))
    if kode == '1':
        print()
        harga = 7000
        total = harga*n
        print('---')
        print(f"Pesanan Anda: \nKode: {kode} \nNama Minuman:  Jus Jambu \nHarga: Rp. {harga}/gelas \nJumlah Pesan: {n} \nJumlah yang harus dibayar: Rp. {total}")
        print('---')
        print('------Terima Kasih-----')
    elif kode == '2':
        print()
        harga = 7000
        total = harga*n
        print('---')
        print(f"Pesanan Anda: \nKode: {kode} \nNama Minuman:  Jus Jeruk \nHarga: Rp. {harga}/gelas \nJumlah Pesan: {n} \nJumlah yang harus dibayar: Rp. {total}")
        print('---')
        print('------Terima Kasih-----')
    elif kode == '3':
        print()
        harga = 7000
        total = harga*n
        print('---')
        print(f"Pesanan Anda: \nKode: {kode} \nNama Minuman:  Jus Jeruk \nHarga: Rp. {harga}/gelas \nJumlah Pesan: {n} \nJumlah yang harus dibayar: Rp. {total}")
        print('---')
        print('------Terima Kasih-----')
    else:
        print('Mohon maaf, pilihan Anda tidak tersedia! Mohon periksa kembali.')















