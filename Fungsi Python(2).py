'''Fungsi dengan Return'''

#template dengan kembalian
#def nama_fungsi(argumen):
#   badan_fungsi
#   return output

#fungsi kuadrat
def kuadrat(input_angka):
    output_kuadrat = input_angka**2
    return output_kuadrat

y = kuadrat(3)
print(y)


#fungsi tambah
def fungsi_tambah(angka1, angka2):
    '''fungsi return dengan multi input(dua argumen)'''
    return angka1 + angka2

a = fungsi_tambah(10,8)
print(a)
print('*'*20)


#fungsi dengan return banyak
def operasi_mtk(angka1, angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2

    return tambah, kurang, kali, bagi


k, l, m, n = operasi_mtk(9,5)

print(f'Hasil tambah = {k}')
print(f'Hasil kurang = {l}')
print(f'Hasil kali = {m}')
print(f'Hasil bagi = {n}')
