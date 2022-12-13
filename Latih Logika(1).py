while True:
    a = int(input("Nilai awal: "))
    b = int(input("Nilai akhir: "))
    for i in range(a, b+1):
        for j in range (1,i+1):
            print(j, end='')
        print()
