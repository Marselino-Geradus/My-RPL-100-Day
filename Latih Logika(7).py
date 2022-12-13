'''Tampilkan tabel perkalian suatu angka'''
while True:
    print('\n'*2)
    klp = int(input('Tampilkan tabel perkalian: '))
    print('='*20)
    for a in range(1, 11):
        print(a, ' x ', klp, ' = ' , (klp*a))
    print('='*20)
