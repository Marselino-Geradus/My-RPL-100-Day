kata = input('Masukkan kata/kalimat: ')
kos = {
'a' : 0,
'i' : 0,
'u' : 0,
'e' : 0,
'o' : 0,
' ' : 0
}

jumlah = 0

for a in kata:
    if a in ['a', 'i', 'u', 'e', 'o', ' ']:
        kos[a] += 1
        jumlah += 1

print(f'''\n
a = {kos['a']}
i = {kos['i']}
u = {kos['u']}
e = {kos['e']}
o = {kos['o']}
spasi = {kos[' ']}

''')

print(f'Total karakter : {len(kata)}')
print(f'Total huruf vokalnya : {jumlah}')
