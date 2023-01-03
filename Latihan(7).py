'''Ini adalah soal (3-Ronde 2) dalam lomba Coding War yang diselenggarakan oleh RPL Lab Unsulbar'''
bulan_komputer = 55000000 / 1500000

gaji_pokok = 5000000
bisa_menabung = 1500000
pengeluaran1_sewaKost = 750000
pengeluaran2_kebutuhan = 1000000


#persamaan 1
total_pengeluaran = pengeluaran1_sewaKost + pengeluaran2_kebutuhan
print('>>> Total pengeluaran Dilan sebulan (sewa kost & biaya hidup) = Rp. ',total_pengeluaran)
#persamaan 2
gaji_bersih = gaji_pokok - total_pengeluaran
print('>>> Gaji bersih Dilan sebulan (meski sudah dikurangi dengan pengeluarannya) masih ada sisanya untuk menabung, bahkan lebih, yaitu sebesar = Rp. ',gaji_bersih)
print('>>> Karena kita sudah tahu bahwa Dilan masih punya kas lebih, itu artinya kita tidak perlu khawatir masalah tabungan bulanan Dilan.')
print('''>>> Untuk dapat mengetahui jumlah minimal berapa bulan Dilan harus menabung agar bisa membeli Komputer Sultan itu, kita hanya perlu membagi harga komputer itu dengan tabungan_maksimalnya per bulan. Setelah itu, kita akan membalikkan rumusnya.

Jadi kita sekarang fokus pada tabungan_maksimalnya.
''')

#persamaan 3
bulan = 37
r = bisa_menabung * bulan
print('>> Jumlah bulan dimana Dilan harus menabung = ',bulan_komputer, ', namun kita akan membulatkannya ke atas agar menjadi bilangan bulat (integer).')
print('>> Waktunya membalik rumus (tabungan_maksimal * hasil_pembulatan) sehingga biaya yang dibutuhkan bisa mencapai target (55jt) = ',r)
print(f'Dari sini kita bisa mengetahui bahwa jumlah minimal bulan dimana ia harus menabung adalah = {bulan} bulan (3 tahun 1 bulan) :).')