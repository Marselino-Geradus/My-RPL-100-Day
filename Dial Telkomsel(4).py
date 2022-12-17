saldo = []
saldo1 = int(input('> Saldo pulsa: '))
paket = int(input('> Paket aktif (GB): '))
print('-'*50)
print()

while True:
    print('='*50)
    print('= SELAMAT DATANG DI GRAPARI TELKOMSEL KW ='.center(50))
    print('''
    1. Transfer Pulsa
    2. Isi Pulsa
    3. Cek Pulsa  ---> Isi pulsa terlebih dahulu untuk melihat saldo.
    4. Cek Kuota
    5. Info Paket
    '''.center(50))

    menu = input('> Pilih menu: ')
    print('~'*50)
    print()
    
    if menu == '1':
        print('>>> Transfer Pulsa <<<'.center(50))
        trans = input('> Masukkan nomor tujuan pengiriman: ')
        nominal = input('> Nominal pulsa yang ingin ditransfer: ')
        
        if trans == False:
            print('~ Nomor yang Anda masukkan tidak lengkap! Mohon input ulang.')
            print(('-'*50))
            print(('-'*50))
        else:
            print('-'*50)
            print('~ Transfer pulsa berhasil! Terima kasih telah memakai Telkomsel. Semoga harimu menyenangkan:)')
            print(('-'*50))
            print(('-'*50))
            
    elif menu == '2':
        print('>>> Isi Pulsa <<<'.center(50))
        isi = input('> Nomor Anda: ')
        nominal = input('> Nominal pulsa yang ingin diisi: ')
        if isi == False:
            print('-'*50)
            print('~ Nomor yang Anda masukkan tidak lengkap! Mohon input ulang.')
            print(('-'*50))
            print(('-'*50))            
        else:
            print('-'*50)
            print('''~ Permintaan Anda sedang diproses!
    Mohon cek pesan SMS untuk konfirmasi lebih lanjut.''')
            print(('-'*50))
            print(('-'*50))

    elif menu == '3':
        saldo2 = int(nominal) + saldo1
        print('>>> Sisa Pulsa <<<'.center(50))
        print(f'''~ Sisa pulsa yang Anda miliki adalah {saldo1}.
                ''')
        print(('-'*50))
        print(('-'*50))

    elif menu == '4':
        print('>>> Info Kuota <<<'.center(50))
        print(f'''~ Paket Aktif:
              1. Kuota Internet Anda = {paket} GB.

              Cek beragam paket internetan murah meriah di menu Info Paket!
              ''')
   
    elif menu == '5':
        print('>>> Info Paket <<<'.center(50))
        print('''
    1. Internet 15 GB/30 hari = 50k
    2. Internet 10 GB/30 hari = 30k
    3. Internet 5 GB/30 hari   = 15k
    4. Internet 3 GB/7 hari   = 7k
    5. Internet 1 GB/3 hari   = 4k
    ''')
        pilih = input('> Pilih: ')
        if (pilih == '1'):
            yakin = input('>> Apakah Anda yakin ingin membeli paket Internet 15 GB/30 hari seharga 50k? (y/n): ')
            if yakin == 'y' or yakin == 'Y':
                print('''
        ~ Selamat! Paket Internet 15 GB/30 hari Anda berhasil diaktifkan.
            Terima kasih telah berlangganan dengan Telkomsel:).''')
            else:
                print()
        
        elif (pilih == '2'):
            yakin2 = input('>> Apakah Anda yakin ingin membeli paket Internet 10 GB/30 hari seharga 30k? (y/n): ')
            if yakin2 == 'y' or yakin2 == 'Y':
                print('''
        ~ Selamat! Paket Internet 10 GB/30 hari Anda berhasil diaktifkan.
            Terima kasih telah berlangganan dengan Telkomsel:).''')
            else:
                print('')
            
        elif (pilih == '3'):
            yakin3 = input('>> Apakah Anda yakin ingin membeli paket Internet 5 GB/30 hari seharga 15k? (y/n): ')
            if yakin3 == 'y' or yakin3 == 'Y':
                print('''
        ~ Selamat! Paket Internet 5 GB/30 hari Anda berhasil diaktifkan.
            Terima kasih telah berlangganan dengan Telkomsel:).''')
            else:
                print()
            
        elif (pilih == '4'):
            yakin4 = input('>> Apakah Anda yakin ingin membeli paket Internet 3 GB/7 hari seharga 7k? (y/n): ')
            if yakin4 == 'y' or yakin4 == 'Y':
                print('''
        ~ Selamat! Paket Internet 3 GB/7 hari Anda berhasil diaktifkan.
            Terima kasih telah berlangganan dengan Telkomsel:).''')
            else:
                print()
            
        elif (pilih == '5'):
            yakin5 = input('>> Apakah Anda yakin ingin membeli paket Internet 1 GB/3 hari seharga 4k? (y/n): ')
            if yakin5 == 'y' or yakin5 == 'Y':
                print('''
        ~ Selamat! Paket Internet 1 GB/3 hari Anda berhasil diaktifkan.
            Terima kasih telah berlangganan dengan Telkomsel:).''')
            else:
                print()

        else:
            print('>> Maaf, masukan Anda salah! Silakan pilih ulang.')
            ulang = input('~~ Pilih ulang? (y/n): ')
            if ulang == 'y' or ulang == 'Y':
                print()
            else:
                print()
    else:
            print('>> Maaf, inputan Anda salah! Silakan pilih ulang.')
