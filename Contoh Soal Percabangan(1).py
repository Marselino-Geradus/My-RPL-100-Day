'''
Bagaimana cara menentukan angka terbesar dari tiga (3) buah angka yang tersedia? (angka 1, angka 2, angka 3)
'''
#buat Variabel Input
a = int(input("Nilai a: "))
b = int(input("Nilai b: "))
c = int(input("Nilai c: "))

if a > b and a > c:
    print("Nilai A adalah angka terbesar.")
elif b > a and b > c:
    print("Nilai B adalah angka terbesar.")
else:
    print("Nilai C adalah angka terbesar.")


