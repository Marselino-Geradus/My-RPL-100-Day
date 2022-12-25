print('+'*30)
print('-'*30)
print('>>> PROGRAM EDISI NATALAN <<<')
print('-'*30)
print('+'*30)

def kue(ini_kue ='KUE TAHUN BARU'):
    print()
    print('~'*30)
    print(f'>>> {ini_kue} <<<'.center(30))
    print('~'*30)

    jenis_kue = ini_kue

    if jenis_kue == 'KUE NATAL':
        print('''
    1. Nastar
    2. Kacang Goreng
    3. Deppatori' Lea''')

    elif jenis_kue == 'KUE TAHUN BARU':
        print('''
        1. Kue Bengbeng
        2. Kue Abon
        3. Deppatori' Busa''')
    

    pesan = input('Mau pesan apa? : ')
    if (pesan == '1','2','3'):
        print('''
        Permintaan Anda sedang kami proses. Mohon menunggu sejenak. 
        Terima kasih telah memesan produk kami. Semoga harimu menyenangkan:)
        
        Selamat Hari Natal dan Tahun Baru !!!''')
    else:
        print('Mohon maaf, pilihan Anda tidak tersedia! Silakan pilih ulang.')


while True:
    print()
    print('='*30)
    print('= TOKO KUE ='.center(30))
    print('='*30)

    print('''
    1. Kue Natal
    2. Kue Tahun Baru
    ''')


    pilih = input('Pilih menu: ')

    if pilih == '1':
        kue('KUE NATAL')
    elif pilih == '2':
        kue()
    else:
        print('Masukan Anda salah! ')
        break

