#Belajar Logika Aritmetika
print('''Soal: Menurut penelitian, seseorang sudah bisa dikatakan ahli dalam bidang tertentu jika dia telah belajar selama 10.000 jam. Jika Mage bisa belajar selama 6 jam dalam sehari, tentukan berapa bulan Mage bisa menjadi programmer ahli!''')
print()
print('JAWAB: ')

print()
jam_tahun = 6*30*12
print(f'>Satu tahun bisa dapat {jam_tahun} jam.')
selisih = 1e4 / jam_tahun 
print('>Jumlah tahun: ',selisih)
bulan = selisih * 12
print('Jadi, jika Mage belajar 6 jam/hari maka dia sudah bisa dikatakan seorang programmer ahli dalam waktu ',bulan, ' bulan.')

print()
print('''Saya bulatkan tahunnya menjadi 5, sehingga hasilnya akan seperti berikut: ''')
bulan = 5 * 12
print('Jadi, jika Mage belajar 6 jam/hari maka dia sudah bisa dikatakan seorang programmer ahli dalam waktu ',bulan, ' bulan.')
