while True:
    print('=' * 30)
    print('=' + 'Program Mencari Volume Kubus'.center(50) + '=')
    print('=' * 30)
    print()
    
    kubus = float(input('~ Masukkan panjang rusuknya (m): '))
    hasil = int(kubus) ** 3
    print(f'>> Volume kubus = {hasil} m**3' + ' <<')
    print('---------------------------------------')
    
    tanya = input('~ Mau lanjut? (y/n): ')
    if tanya == 'y' or tanya == 'Y':
        print()
    else:
        break



while True:
    print('\n' * 2)
    print('=' * 30)
    print('=' + 'Program Mencari Volume Balok'.center(50) + '=')
    print('=' * 30)
    print()
    
    pj = float(input('~ Masukkan panjang rusuknya (m): '))
    lb = float(input('~ Masukkan lebar rusuknya (m): '))
    tg = float(input('~ Masukkan tinggi rusuknya (m): '))
    hasil2 = int(pj * lb * tg)
    print(f'>> Volume balok = {hasil2} m**3' + ' <<')
    print('---------------------------------------')
    
    tanya = input('~ Mau lanjut? (y/n): ')
    if tanya == 'y' or tanya == 'Y':
        print()
    else:
        break
