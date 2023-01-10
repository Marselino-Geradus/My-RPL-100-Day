# Program Menampilkan Bilangan Bulat 1 - x dengan Perulangan For

print('='*65)
x = int(input('~ Masukkan nilai x = '))
print('>>> Program akan menampilkan bilangan bulat dari 1 - (nilai x)', '<<<')
print('~'*65)

for i in range(1, x+1):
    print(f'> Ini perulangan ke-{i}')