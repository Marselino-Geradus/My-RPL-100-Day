#menghitung Mean secara manual
import statistics
data = [1, 2, 3, 1, 5]
data.sort()

def rata_rata (deret):
  return sum(deret) / len(deret)

def nilai_tengah(deret):
  deret.sort()
  n = len(deret) # ambil panjang data
  i_tengah = n // 2 # dibulatkan ke bawah

  # jika n adalah ganjil
  if n % 2 == 1:
    return deret[i_tengah]

  # jika n genap
  return (deret[i_tengah - 1] + deret[i_tengah]) / 2

def nilai_terbanyak(deret):
  # dictionary untuk mapping nilai terbanyak
  peta_kemunculan = {}

  # perulangan satu-persatu tiap bilangan
  for bilangan in deret:
    # periksa apakah sudah pernah muncul atau belum
    if bilangan in peta_kemunculan:
      peta_kemunculan[bilangan] += 1
    else:
      peta_kemunculan[bilangan] = 1

  # cari kemunculan terbanyak
  bilangan_terbesar = deret[0] # ambil angka pertama sebagai yg terbanyak
  for bilangan in peta_kemunculan.keys():
    jumlah = peta_kemunculan[bilangan]

    if jumlah > peta_kemunculan[bilangan_terbesar]:
      bilangan_terbesar = bilangan

  return bilangan_terbesar

print(f'Data terurut = {data}')
print(f'~ Mean = {rata_rata(data)}')
print(f'~ Median = {nilai_tengah(data)}')
print(f'~ Modus = {nilai_terbanyak(data)}')
