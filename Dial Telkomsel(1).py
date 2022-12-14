while True:
    print('= SELAMAT DATANG DI GRAPARI TELKOMSEL KW ='.center(50))
    print('''
1. Transfer Pulsa
2. Minta Pulsa
3. Cek Pulsa
4. Cek Kuota
5. Info Paket
'''.center(50))

    #minta = int(input('> Masukkan nominal pulsa yang ingin ditransfer: '))
    menu = input('> Pilih menu: ')
    print('~'*50)
    print()
    
    if menu == '1':
        print('>>> Transfer Pulsa <<<'.center(50))
        trans = input('> Masukkan nomor tujuan pengiriman: ')
        if False:
            print('~ Nomor yang Anda masukkan tidak lengkap! Mohon input ulang.')
            print(('-'*50))
            print(('-'*50))
        else:
            print('>> Transfer pulsa berhasil! Terima kasih telah memakai Telkomsel. Semoga harimu menyenangkan:)')
            print(('-'*50))
            print(('-'*50))
