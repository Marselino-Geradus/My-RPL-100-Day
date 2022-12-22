'''Fungsi dengan percabangan'''
def percabangan():
    print('~'*20)
    isi_nama = int(input('Masukkan nilai: '))
    if (isi_nama >= 60 and isi_nama <= 75):
        print('Nilai Anda = C')
    elif (isi_nama > 76 and isi_nama <= 85):
        print('Nilai Anda = B')
    elif (isi_nama > 86 and isi_nama <= 100):
        print('Nilai Anda = A')
    elif isi_nama > 100:
        print('Mohon maaf, nilai tidak terdefinisi.')
    else:
        print('Mohon maaf, Anda harus remedial!')

percabangan()


'''= Fungsi dengan Perulangan ='''
def ulang(nama='Putri'):
    #perulangan For
    for a in range (1,10+1):
        print(a,f'| I love you for a thousand year, {nama}.')

ulang()
print('~'*20)

ulang('Putra')
print('~'*20)