'''Ini adalah soal (1) dalam lomba Coding War yang diselenggarakan oleh RPL Lab Unsulbar'''

#definisikan pernyataan yang ada
lembur_jam = 55000

#nilai dimasukkan dengan fungsi Input
gaji_pokok = int(input('Masukkan gaji pokok: Rp.'))
lama_lembur = int(input('Lama lembur (jam): '))

#logika bermain di sini
gaji_lembur = (lembur_jam * lama_lembur)
gaji_bersih = gaji_pokok + gaji_lembur
print('Gaji bersih yang diterima oleh karyawan tersebut setiap bulan = Rp.',gaji_bersih)