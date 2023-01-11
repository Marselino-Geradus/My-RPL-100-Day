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

#Proses Cari Jawaban IV
#Hampir sama ji Latihan(13), cuman lebih sederhana:)
#PREDIKSI KEUNTUNGAN INVESTASI

modal = int(input('Modal awal: '))
tahun = int(input('Lama investasi (tahun): '))
for i in range(1, tahun+1):
    keuntungan = modal * (5/100)
    print(f'Keuntungan tahun ke-{i} adalah Rp. {keuntungan}')
    modal += keuntungan