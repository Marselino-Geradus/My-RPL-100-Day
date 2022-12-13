'''
Menentukan angka terkecil dari tiga (3) buah angka yang tersedia (angka 1, angka 2, angka 3)
'''

while True:
    a = int(input("Nilai a: "))
    b = int(input("Nilai b: "))
    c = int(input("Nilai c: "))
    if a < b and a < c:
        print("Nilai A adalah angka terkecil.")
    elif b < a and b < c:
        print("Nilai B adalah angka terkecil.")
    elif c<a and c<b:
        print("Nilai C adalah angka terkecil.")
    else:
        print("Tidak bisa ditentukan!")
        break
    
