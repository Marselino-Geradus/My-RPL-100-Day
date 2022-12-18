'''Membuat Fungsi'''

def hello_world(nama):
    '''Fungsi hello world untuk menerima input dengan variabel nama.'''
    print(f'Selamat datang ke rumah barumu, {nama}!')

hello_world('Marsel')


def tambah(angka1,angka2):
    hasil = angka1 + angka2
    print(f'angka 1 + angka 2 = {hasil}')

tambah(1,3)

def say_hi(list_peserta):
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f'''
        Yth. CEO MamasaFarm, {peserta}
        Di tempat.''')

anggota = ['Mars', 'Tian', 'Alia']
say_hi(anggota)