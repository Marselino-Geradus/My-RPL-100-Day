##fungsi dengan parameter biasa (tidak wajib)
def penutup():
    print()
    print('Sekian dan terima kasih'.center(163,'-'))


    
#fungsi dengan parameter wajib    
def perkenalan(nama,kelas):
    print(f'Halo ! Perkenalkan nama saya {nama} dari kelas Informatika-{kelas}.')
print('1')
perkenalan('Mage','G')

def hewan(berbulu,kaki):
    print(f'Aku pernah ke kebun binatang. Di sana aku melihat singa yang berbulu {berbulu} dan ia punya {kaki} kaki.')    
print('2')
hewan('tebal','4')

def kucing(suara):
    print(f'{suara} adalah suara kucing.')
print('3')
kucing('Meong')

def balita(nangis):
    print(f'Balita itu selalu {nangis} jika ibunya tidak ada.')
print('4')
balita('menangis')

def nangka(rasa):
    print(f'Buah nangka yang matang memiliki rasa yang {rasa}.')
print('5')
nangka('manis')


def sayur(warna,nama,rasa):
    print(f'Aku suka sayur {nama}. Ia punya warna {warna} yang unik jika dimasak dan rasanya juga {rasa}.')
print('6')
sayur('Bayam','ungu','enak')

def mahasiswa(tugas,pacar):
    print(f'Aku sering melihat temanku mengeluh karena banyaknya tugas{tugas} yang belum selesai;  ditambah lagi karena {pacar} yang selalu minta dihubungi setiap waktu.')
print('7')
mahasiswa('Matematika','pacarnya')

def mahasusah(pusing,sakit):
    print(f'Sebagai mahasiswa yang punya tanggung jawab besar, pastinya punya resiko yang besar pula, misalnya sering pusing pikirin {pusing} dan juga biasa kena sakit {sakit}.')
print('8')
mahasusah('tugas','maag')

def pengetahuan(sumber,manfaat):
    print(f'Salah satu sumber IPTEK yaitu {sumber}. Salah satu manfaat membaca {sumber} yaitu {manfaat}.')
print('9')
pengetahuan('buku','memperkaya kosakata kita')

def keluarga(hubungan,bagian):
    print(f'Keluarga merupakan rumah pertama yang mengenalkan {hubungan} terhadap sesama manusia. Keluarga inti terdiri dari {bagian}.')
print('10')
keluarga('kasih sayang','ayah, ibu, dan anak-anak')


penutup()
