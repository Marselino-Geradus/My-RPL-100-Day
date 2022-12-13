#Soal 1: Cari nilai maksimum dan minimum dari sebuah data
a = [12, 88, 35, 29]

#Soal 2: Cari nilai maks dan minim menggunakan logika perulangan
def nilai_maksimal (deret_bilangan):
  nilai_terbesar = deret_bilangan[0]
  
  for nilai in deret_bilangan:
      if nilai > nilai_terbesar:
          nilai_terbesar = nilai
          
  return nilai_terbesar

def nilai_minimal (deret_bilangan):
  nilai_terkecil = deret_bilangan[0]
  
  for nilai in deret_bilangan:
      if nilai < nilai_terkecil:
          nilai_terkecil = nilai
          
  return nilai_terkecil

  

print(a)
print('Nilai Maksimum dari list di atas adalah : ',nilai_maksimal(a))
print("Nilai Minimum dari list di atas adalah : ",nilai_minimal(a))
