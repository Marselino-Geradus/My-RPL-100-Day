'''
- Soal 3/Final Test
- Coding War
- RPL Lab Unsulbar

~ Soal ~
Buatlah program yang dapat memprediksi keuntungan setiap tahun
yang akan didapatkan investor jika ketentuan investasi sebagai berikut:
1. Keuntungan tiap tahun = 5% dari total lama_investasi
2. Setiap keuntungan per tahun, dimasukkan menjadi tambahan modal investasi pada tahun berikutnya.
3. Modal awal dan lama investasi diinput
''' 

#Proses Cari Jawaban II
#PREDIKSI KEUNTUNGAN INVESTASI
#Ini masih dalam proses mencari metode yang benar

modalAwal = 5000000
bulan = 12
lama_investasi = 2

total_penghasilan = modalAwal * lama_investasi
ROI = (total_penghasilan - modalAwal) / modalAwal
print("Keuntungan investasi dalam setahun = ",ROI,"(100%).")
