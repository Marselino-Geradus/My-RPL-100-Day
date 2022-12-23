def fungsi_cabang(nilai=80):
    huruf = ''
    if nilai >= 0 and nilai < 20:
        huruf = 'Nilai Anda = E'
    elif nilai >= 20 and nilai < 40:
        huruf = 'Nilai Anda = D'
    elif nilai >= 40 and nilai < 60:
        huruf = 'Nilai Anda = C'
    elif nilai >= 60 and nilai < 80:
        huruf = 'Nilai Anda = B'
    elif nilai >= 80 and nilai <= 100:
        huruf = 'Nilai Anda = A'
    else:
        huruf = 'Mohon maaf! Anda harus remedial.'
    return print(huruf,'.')

fungsi_cabang(100)