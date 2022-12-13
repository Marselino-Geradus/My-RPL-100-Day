#1. Cara membuat komentar (menggunakan '#' )
'''2. Cara membuat komentar
  dengan dua baris atau lebih
  menggunakan tanda petik tiga kali (''' ''')'''

print()
#Menampilkan output dengan beberapa cara
print('>>>Menampilkan output dengan beberapa cara<<<')
'''Cara 1: Membuat pemisah kalimat dengan separator(sep=' ')'''
print('>>Cara 1')
print('Andi', 'Budi', 'Tasya', 'Lala', sep='_^_')

'''Cara 2: Menyambungkan beberapa fungsi print dengan perintah yang dikehendaki oleh user menggunakan end(end=' ')'''
print()
print('>>Cara 2')
print('Merkurius', end=' ')
print('Venus', end=', ')
print('Bumi', end=', dan ')
print('Mars')


'''Cara 3: Menggunakan format() dengan indeks'''
print()
print('>>Cara 3')
print('{0} dan {1} suka makan buah.'.format('Budi', 'Joko'))


'''Cara 4: Menggunakan format() dengan kunci'''
print()
print('>>Cara 4')
print('Halo {nama1} {nama2}, senang berjumpa kembali:)!'.format(nama1='Marselino', nama2='Geradus'))


'''Cara 5: Menggunakan format() dengan kunci yang tersusun dalam beberapa baris.
              Tujuannya adalah agar program mudah dibaca'''
print()
print('>>Cara 5')
print('Halo {na} {ma}!'
      .format(
          na='Mage',
          ma='29'
          )
      )
