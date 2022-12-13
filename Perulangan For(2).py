#ini contoh soal yang masih membingungkan saya
'''Buatlah program yang outputnya itu menampilkan kalimat berikut ini:
> Pertemuan ke - 1 telah selesai
> Pertemuan ke - 2 telah selesai
> Pertemuan ke - 3 telah selesai
> Pertemuan ke - 4 telah selesai
> Pertemuan ke - 5 diadakan kuis
> Pertemuan ke - 6 diadakan final
> Pertemuan ke - 7 belum selesai
> Pertemuan ke - 8 belum selesai
> Pertemuan ke - 9 belum selesai
> Pertemuan ke - 10 belum selesai
> Pertemuan ke - 11 diadakan kuis
> Pertemuan ke - 12 diadakan final
'''

#Bagaimana logika pemrogramannya yang tepat agar hasilnya itu bisa sama seperti di atas?
for c in range(1,13):
    if c == 5 and c == 11:
        print("Pertemuan ke-",c," diadakan kuis.")
    elif c == 6 and c == 12:
        print("Pertemuan ke-",c," diadakan final.")
    elif c >= 7 and c <= 12:
        print("Pertemuan ke-" ,c," belum selesai.")
    else:
        print("Pertemuan ke-" ,c," telah selesai.")

