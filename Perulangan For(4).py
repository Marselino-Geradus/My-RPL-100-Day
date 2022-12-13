#contoh 1
simbol = int(input("Masukkan angka: "))
for a in range(1,simbol+1):
    for b in range(1, simbol+a,  +1):
        print(b, end=" ")
    print()
