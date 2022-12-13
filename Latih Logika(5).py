while True:
    print('''

----------------------------------------------------------------------------

    ========= HARGA PAPAN ARDUINO UNO ========
    Kuantitas  Minimum | Kuantitas Maksimum | Harga per Unit
    1                                |               5                    |       78.000
    6                                |               12                  |       75.000
    13                              |               20                  |       72.000
    21                              |               40                  |       68.000
    41                              |               99                  |       65.000
    100                            |                  -                 |       58.000

----------------------------------------------------------------------------
    ''')

    print()
    a = int(input('>> Jumlah unit yang ingin dibeli: '))
    h1 = 78000
    h2 = 75000
    h3 = 72000
    h4 = 68000
    h5 = 65000
    h6 = 58000
    if a >= 1 and a <= 5:
        print(f'> Harga per unit: Rp. {h1}')
        print('> Total harga: ',(a*h1))
    elif a >= 6 and a <= 12:
        print(f'> Harga per unit: Rp. {h2}')
        print('> Total harga: ',(a*h2))
    elif a >= 13 and a <= 20:
        print(f'> Harga per unit: Rp. {h3}')
        print('> Total harga: ',(a*h3))
    elif a >= 21 and a <= 40:
        print(f'> Harga per unit: Rp. {h4}')
        print('> Total harga: ',(a*h4))
    elif a >= 41 and a <= 99:
        print(f'> Harga per unit: Rp. {h5}')
        print('> Total harga: ',(a*h5))
    else:
        print(f'> Harga per unit: Rp. {h6}')
        print('> Total harga: ',(a*h6))
