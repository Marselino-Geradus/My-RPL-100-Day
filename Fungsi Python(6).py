def fungsi_cabang(nilai=80):
    huruf = ''
    if nilai >= 0 and nilai < 20:
        huruf = 'E'
    elif nilai >= 20 and nilai < 40:
        huruf = 'D'
    elif nilai >= 40 and nilai < 60:
        huruf = 'C'
    elif nilai >= 60 and nilai < 80:
        huruf = 'B'
    elif nilai >= 80 and nilai < 100:
        huruf = 'A'

    return huruf

fungsi_cabang(70)