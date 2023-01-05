'''Ini adalah soal (1-FINAL) dalam lomba Coding War yang diselenggarakan oleh RPL Lab Unsulbar'''

while True:
    print('='*45)
    print('='*45)
    pekerjaan = input('~ Pekerjaan: ').lower()
    print('-'*30)
    if pekerjaan == 'pns' or pekerjaan == 'polisi' or pekerjaan == 'tentara' or pekerjaan == 'pegawai' or pekerjaan == 'pegawai negeri':
        pajak = 5/100
        print(f'>> Karena Anda PNS maka Anda dikenakan pajak sebesar 5%.')

        print('~'*30)
        penghasilan = int(input('~ Penghasilan/bulan: Rp.'))
        if penghasilan >= 3000000 and penghasilan < 5000000:
            pajak1 = (5/100 + pajak) * (penghasilan)
            gaji_bersih = penghasilan - pajak1

            print('>> Gaji >= 3jt & < 5jt dipotong pajak sebesar 5%.')
            print(f'>>> Gaji bersih Anda per bulan = Rp.{gaji_bersih}')
        elif penghasilan >= 5000000:
            pajak1 = (10/100 + pajak) * (penghasilan)
            gaji_bersih = penghasilan - pajak1

            print('>> Gaji >= 5jt dipotong pajak sebesar 10%.')
            print(f'>>> Gaji bersih Anda per bulan = Rp.{gaji_bersih}')
        else:
            print('>>> Gaji Anda tidak masuk akal! Mohon periksa kembali.')

    else:
        penghasilan = int(input('~ Penghasilan/bulan: Rp. '))
        if penghasilan >= 3000000 and penghasilan < 5000000:
            pajak1 = (5/100 * penghasilan)
            gaji_bersih = penghasilan - pajak1

            print('>> Gaji >= 3jt & < 5jt dipotong pajak sebesar 5%.')
            print(f'>>> Gaji bersih Anda per bulan = Rp.{gaji_bersih}')
        elif penghasilan >= 5000000:
            pajak1 = (10/100 * penghasilan)
            gaji_bersih = penghasilan - pajak1

            print('>> Gaji >= 5jt dipotong pajak sebesar 10%.')
            print(f'>>> Gaji bersih Anda per bulan = Rp.{gaji_bersih}')
        else:
            print('>> Anda tidak dikenakan pajak.')
            print('>>> Penghasilan Anda tetap Rp.',penghasilan)