'''Default Argumen'''

#contoh 1
def masukkan_nama(nama = "(masukkan nama Anda)"):
    print(f"Nama saya adalah {nama}")

masukkan_nama()
masukkan_nama("Bongga Lotong")
print('*'*20)

#contoh 2
def sapa_dia(nama, pesan='apa kabar?'):
    '''fungsi dengan satu input biasa & satu default argumen'''
    print(f'Hai {nama}, {pesan}')

sapa_dia('Dudung','Hai Ganteng')
sapa_dia('Beto')
print('*'*20)

#contoh 3
def hitung_pangkat(angka,pangkat):
    hasil = angka**pangkat
    return hasil

a1 = int(input('Angka = '))
a2 = int(input('Pangkat = '))
print(f'Nilai dari {a1}**{a2} adalah ',hitung_pangkat(2,4))
print('*'*20)
print('*'*20)