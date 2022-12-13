def kalkulator():
    print('''
===============
   Kalkulator Sederhana
===============
|       1. Tambah (+)       |
|       2. Kurang (-)         |
|       3. Kali (*)               |
|       4. Bagi (/)              |
|       5. Pangkat (**)       |
|       6. Modulo (%)       |
|       7. Pembulatan       |
|           ke bawah (//)   |
~~~~~~~~~~~~~~~
''')
    pilih = input('Pilih nomor operator: ')    
    while True:
        if pilih == '1':
            jumlah()
        elif pilih == '2':
            kurang()
        elif pilih == '3':
            kali()
        elif pilih == '4':
            bagi()
        elif pilih == '5':
            pangkat()
        elif pilih == '6':
            modulo()
        elif pilih == '7':
            bulatan()
        else:
            print('Operator tersebut tidak ada. Mohon periksa kembali!')
        break
    print()
    kalkulator()

#Definisikan operator yang diperlukan ( (+) , (-) , (*) , (/))
def jumlah():
    a = int(input('>>Masukkan nilai a: '))
    b = int(input('>>Masukkan nilai b: '))
    c = a + b
    print('=> Hasil dari a + b =  ',c)
    print()
    
def kurang():
    a = int(input('>>Masukkan nilai a: '))
    b = int(input('>>Masukkan nilai b: '))
    d = a-b
    print('=> Hasil dari a - b =  ',d)
    print()

def kali():
    a = int(input('>>Masukkan nilai a: '))
    b = int(input('>>Masukkan nilai b: '))
    e = a*b
    print('=> Hasil dari a * b =  ',e)
    print()
    
def bagi():
    a = int(input('>>Masukkan nilai a: '))
    b = int(input('>>Masukkan nilai b: '))
    f = a/b
    print('=> Hasil dari a / b =  ',f)
    print()

def pangkat():
    a = int(input('>>Masukkan nilai a: '))
    b = int(input('>>Masukkan nilai b: '))
    g = a**b
    print('=> Hasil dari a ** b =  ',g)
    print()

def modulo():
    a = int(input('>>Masukkan nilai a: '))
    b = int(input('>>Masukkan nilai b: '))
    h = a%b
    print('=> Hasil dari a % b =  ',h)
    print()

def bulatan():
    a = int(input('>>Masukkan nilai a: '))
    b = int(input('>>Masukkan nilai b: '))
    i = a//b
    print('=> Hasil dari a // b =  ',i)
    print()
    
kalkulator()
