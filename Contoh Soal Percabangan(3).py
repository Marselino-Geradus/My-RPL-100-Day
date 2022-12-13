'''
Menentukan nilai tengah dari suatu data ()
'''
while True:
    a = int(input("Nilai A: "))
    b = int(input("Nilai B: "))
    c = int(input("Nilai C: "))

    if (b > a > c) or (c > a > b):
        print(">> A adalah nilai tengah")
    elif (a > b > c) or (c > b > a):
        print(">> B adalah nilai tengah")
    elif (a > c > b) or (b > c > a):
        print(">> C adalah nilai tengah")
    else:
        print("## Tidak bisa ditentukan!")
