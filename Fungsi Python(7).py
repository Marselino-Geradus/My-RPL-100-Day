print('''>>> Perbandingan antara penggunaan print dan return <<<''')

print('~'*30)
print('#penggunaan print')
def fungsi_total_nilai1(var_harian, var_uts, var_uas):
    var_harian = int((var_harian) * 0.3)
    var_uts = int ((var_uts) * 0.3)
    var_uas = int((var_uas) * 0.4)

    var_total = var_harian + var_uts + var_uas
    print('Nilai akhir Anda: ',var_total)

fungsi_total_nilai1(70,80,86)


print('~'*30)
print('#penggunaan return')
def fungsi_total_nilai(var_harian, var_uts, var_uas):
    var_harian1 = int((var_harian) * 0.3)
    var_uts1 = int ((var_uts) * 0.3)
    var_uas1 = int((var_uas) * 0.4)

    var_total1 = var_harian1 + var_uts1 + var_uas1
    return var_total1


print('Nilai akhir Anda: ',fungsi_total_nilai(70,80,86)) 

print('+'*30)
print('''
Pada akhirnya, keduanya sama saja.
Jadi yang membedakan hanyalah keinginan programmer; kapan mau memakainya.''')