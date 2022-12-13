#mengembalikan nilai
def luas_persegi(sisi):
    return sisi * sisi

#tidak mengembalikan output apapun
luas_persegi(4)


#ini mengembalikan output
print('Luas persegi yang memiliki sisi 4 yaitu ',luas_persegi(4))
print()


#menyimpan terlebih dahulu dalam sebuah variabel
persegi_a = luas_persegi(5)
persegi_b = luas_persegi(4)
print('Total luas persegi A dan B adalah ',persegi_a+persegi_b)
