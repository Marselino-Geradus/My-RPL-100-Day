# "==============================="
# "CARA 1"
# "MENGGUNAKAN LIST"
# "==============================="

# panjang1 = int(input('Masukkan panjang deret: '))
# fibo = [0,1]    #list yang di dalamnya tersimpan 2 angka pertama dari deret fibonacci

# "Ini adalah logika output yang kita inginkan dalam bentuk teksnya."
# # for i in range(2, panjang):
# #     index1 = i - 2
# #     index2 = i -1

# #     print(f'Deret ke-{i + 1} adalah indeks {index1} + indeks {index2}.')


# for i in range (2, panjang1):     #kita mulai dari angka dua karena kita hanya akan menampilkan hasil deret dimulai dari deret ke-3 dst saja
#     angka1 = fibo[i - 2]    #mengambil angka dalam [fibo] dan menyimpannya dalam dua variabel angka ini
#     angka2 = fibo[i - 1]    
#     angkaSelanjutnya = angka1 + angka2  #variabel hasil penjumlahan 2 variabel angka di atasnya

#     fibo.append(angkaSelanjutnya)   #hasil penjumlahan ditambahkan dalam list agar bisa digunakan pada penentuan selanjutnya

# print(fibo)



"==============================="
"CARA 2"
"MENGGUNAKAN 2 VARIABEL BANTUAN"
"==============================="

panjang2 = int(input('Masukkan panjang deret: '))
angka3, angka4 = 0, 1   #tanpa list, hanya 2 variabel

#ini hanya akan menampilkan perulangan biasa (sesuai panjang deret yang diinput), dijadikan percobaan saja
"""for i in range(panjang2):
    print(f'Perulangan ke-{i}')
"""

#pemanasan ke-2 (menjabarkan logika output yang diharapkan)
#kita hanya akan mengedit kode "else" karena di sanalah 'fibonacci'nya
for i in range(panjang2):
    if (i < 2):     #jika i = 0 atau 1 ==> program lansung jalan
        print(i,end=' ')    #kita menambahkan parameter 'end' agar hasilnya tidak vertikal

    # else:           #jika i > 1 ==> lakukan penjumlahan
    #     index3 = i - 2
    #     index4 = i - 1
    #     print(f'Penjumlahan dari indeks {index3} dan indeks {index4}')

    else:
        angka1Sekarang = angka3 + angka4
        print(angka1Sekarang, end=' ')

        #update 2 variabel bantuan untuk menghitung angka berikutnya 
        angka3 = angka4
        angka4 = angka1Sekarang
