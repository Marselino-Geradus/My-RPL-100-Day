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

#Proses Cari Jawaban III
#PREDIKSI KEUNTUNGAN INVESTASI

def prediksi(modal_awal,waktu):
    modal = modal_awal
    for i in range(waktu):
        keuntungan = modal * 0.05
        modal += keuntungan

        print(f'Tahun {i+1}: keuntungan = {keuntungan}, total modal = {modal}')

#mengambil input modal awal dan lama investasi dari user
modal_awal = float(input('Modal awal: '))
lama_investasi = int(input('Lama investasi (dalam tahun): '))

# Menjalankan fungsi tadi
prediksi(modal_awal,lama_investasi)
