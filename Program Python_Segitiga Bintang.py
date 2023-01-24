'Program Segitiga Bintang Python'

print('=' * 37)
print(' = Program Segitiga Bintang Python ='.upper())
print('=' * 37)

print()
print('-'*20)
tinggi_segitiga = int(input('> Tinggi segitiga: '))
print('-'*20)

#Cara 1_Manual
print('= Cara 1_Manual =')
tinggi_sgtiga = 4
print('*')
print('* *')
print('* * *')
print('* * * *')



#Cara 2_Perulangan For Tunggal
print()
print('= Cara 2_For Tunggal =')
for a in range(tinggi_segitiga+1):
    print('* ' * a)


#Cara 3_Perulangan For Ganda
print()
print('= Cara 3_For Ganda =')
for i in range(tinggi_segitiga):
    for j in range(i+1):
        print('*',end=' ')
    print()