'''Ini adalah soal UTS PBO Java, tapi aku modifikasi sedikit jadi Python'''




while True:
    jumlah_karung_beras = int(input('Masukkan banyak karung beras yang ingin dibeli: '))

    beras_per_karung = 200000
    diskon1 = (10/100)
    diskon2 = (20/100)

    jumlah = (beras_per_karung * jumlah_karung_beras)
    harga_setelah_diskon1 = diskon1 * jumlah
    harga_setelah_diskon2 = diskon2 * jumlah

    if jumlah_karung_beras >= 5 and jumlah_karung_beras <= 10:
        
        harga_bersih = jumlah - harga_setelah_diskon1
        print(f'Anda mendapatkan diskon 10%. Harga yang harus Anda bayar adalah {harga_bersih}.')
        print('='*20)
        print()

    elif jumlah_karung_beras >= 11:

        harga_bersih = jumlah - harga_setelah_diskon2
        print(f'Anda mendapatkan diskon 15%. Harga yang harus Anda bayar adalah {harga_bersih}.')
        print()

    else:
        print('Anda tidak mendapatkan diskon. Harga yang harus Anda bayar adalah ',jumlah)
        print()