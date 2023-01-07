'''
- Soal 3/Final Test
- Coding War
- RPL Lab Unsulbar
'''


#Proses Cari Jawaban I

#PREDIKSI KEUNTUNGAN INVESTASI
modalAwal = int(input('Modal awal: '))
lama_investasi = int(input('Lama investasi (tahun): '))

keuntungan_tahun = 5/100 * modalAwal * lama_investasi
modal2 = modalAwal + keuntungan_tahun

tingkat_pertumbuhan_keuntungan_tiap_tahun = keuntungan_tahun * modal2
print("Keuntungan yang diterima dalam setahun = ",keuntungan_tahun)
print('Prediksi peningkatan keuntungan tiap tahun = ',tingkat_pertumbuhan_keuntungan_tiap_tahun)

