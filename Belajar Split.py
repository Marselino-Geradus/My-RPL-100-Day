import re  #modul untuk memeriksa apakah suatu string berisi pola pencarian yang spesifik
print('>> Contoh 1')
data = 'aku, kamu, dia'
data.split(', ',0)   #menghilangkan suatu tanda pembatas di antara setiap kata
print(data)

print('>> Contoh 2')
kal = 'Mamasa Majene Mamuju'
a = re.split('\s', kal)   #memberikan suatu tanda pembatas di antara setiap kata
print(a)

