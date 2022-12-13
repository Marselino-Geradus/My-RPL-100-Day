#Menampilkan tiga bilangan yang berbeda; jika sama maka tampilkan pemberitahuan
while True:
    a = int(input('Masukkan nilai A: '))
    b = int(input('Masukkan nilai B: '))
    c = int(input('Masukkan nilai C: '))
    if (a ==  b) or (a == c) or (b == c):
        print('Ada bilangan yang sama.')
    else:
        print('Ketiga bilangan yang ditampilkan berbeda.')

