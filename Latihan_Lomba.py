harga_jual = 300000
pajak = 0

luas_tanah = int(input('Masukkan luas tanah (meter persegi): '))
total_harga_jual = harga_jual * luas_tanah


if total_harga_jual >= 50000000 and total_harga_jual < 100000000:
    pajak = total_harga_jual * (3 / 100)
    pendapatan = total_harga_jual - pajak
    print('Uang bersih = Rp. ',pendapatan)


elif total_harga_jual >= 100000000:
    pajak = total_harga_jual * (5 / 100)
    pendapatan = total_harga_jual - pajak
    print('Uang bersih = Rp. ',pendapatan)


else:
    pajak = total_harga_jual * (1 / 100)
    pendapatan = total_harga_jual - pajak
    print('Uang bersih = Rp. ',pendapatan)


# 149.000.000