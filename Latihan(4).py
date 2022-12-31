'''Ini adalah soal UTS PBO Java, tapi aku modifikasi sedikit jadi Python'''

while True:
    print('='*50)
    pekerjaan = input('~ Pekerjaan: ').lower()
    print('~'*20)
    
    if pekerjaan == 'pns' or pekerjaan == 'pegawai negeri' or pekerjaan == 'pegawai negeri sipil' or pekerjaan == 'pegawai':
        print(' >>> Anda dikenakan pajak sebesar 5%.')
        print('~'*20)
        penghasilan = int(input('~ Masukkan gaji bulanan: '))
        if penghasilan >= 3000000 and penghasilan < 5000000:
            pajak = (5/100 + 5/100) * penghasilan
            gaji_bersih = penghasilan - pajak

            print('     -> Penghasilan >= 3jt dan < 5jt dikenakan pajak 5%.')
            print('     >>> Gaji bersih Anda (per bulan) = Rp. ',gaji_bersih)
            print('='*50)
        elif penghasilan >= 5000000:
            pajak = (10/100 + 5/100) * penghasilan
            gaji_bersih = penghasilan - pajak

            print('     -> Penghasilan >= 5jt dikenakan pajak 10%.')
            print('     >>> Gaji bersih Anda (per bulan) = Rp. ',gaji_bersih)
            print('='*50)

        else:
            print('     >>> Gaji Anda tidak masuk akal! Mohon periksa ulang!')
            print('='*50)

    else:
        penghasilan = int(input('~ Masukkan gaji bulanan: Rp. '))
        if penghasilan >= 3000000 and penghasilan < 5000000:
            pajak = (3/100)
            gaji_bersih = penghasilan - pajak
            print('     -> Penghasilan >= 3jt dan < 5jt dikenakan pajak 5%.')
            print('     >>> Gaji bersih seseorang per bulan = Rp. ',gaji_bersih)
            print('='*50)
        elif penghasilan >= 5000000:
            pajak = (10/100) * penghasilan
            gaji_bersih = penghasilan - pajak
            print('     -> Penghasilan >= 5jt dikenakan pajak 10%.')
            print('     >>> Gaji bersih Anda (per bulan) = Rp. ',gaji_bersih)
            print('='*50)
        else:
            print('     -> Anda tidak dikenakan pajak.') 
            print('     >>> Gaji bersih Anda (per bulan) = Rp. ',penghasilan)
            print('='*50)