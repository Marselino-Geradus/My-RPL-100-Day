saldo = int(input('> Saldo pulsa: '))
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
        if trans == False:
            print('~ Nomor yang Anda masukkan tidak lengkap! Mohon input ulang.')
            print(('-'*50))
            print(('-'*50))
        else:
            print('~ Transfer pulsa berhasil! Terima kasih telah memakai Telkomsel. Semoga harimu menyenangkan:)')
            print(('-'*50))
            print(('-'*50))
            
    elif menu == '2':
        print('>>> Isi Pulsa <<<'.center(50))
        isi = input('> Nomor Anda: ')
        nominal = input('> Nominal pulsa yang ingin diisi: ')
        if isi == False:
            print('~ Nomor yang Anda masukkan tidak lengkap! Mohon input ulang.')
            print(('-'*50))
            print(('-'*50))            
        else:
            print('''~ Permintaan Anda sedang diproses!
    Mohon menunggu konfirmasi lebih lanjut.''')
            print(('-'*50))
            print(('-'*50))

    elif menu == '3':
        saldo1 = int(nominal) + saldo
        print('>>> Sisa Pulsa <<<'.center(50))
        print(f'''~ Sisa pulsa yang Anda miliki adalah {saldo1}.
                ''')
        print(('-'*50))
        print(('-'*50))

    elif menu == '4':
        print('>>> Info Kuota <<<'.center(50))
        print('''~ Paket Aktif:
              1. Kuota Internet Anda = {paket} GB.

              Cek beragam paket internetan murah meriah di menu Info Paket!
              ''')
        
