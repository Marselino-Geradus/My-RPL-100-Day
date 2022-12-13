#Operator Logika
a = True
b = False

print("1. Dasar")
print('''
    a = True
    b = False ''')

print('''
(a). Fungsi AND
    T & T = T
    T & F = F
    F & F = F ''')
print("Contoh: ")
print("a and b = ",a and b)
print("a and a = ",a and a)
print("b and b = ",b and b)
print("---------------------")

print("(b). Fungsi OR")
print("Contoh: ")
print("a or b = ",a or b)
print("a or a = ",a or a)
print("b or b = ",b or b)
print("---------------------")

print("(c). Fungsi NOT")
print("not(a) = ",not(a))
print("---------------------")


print("================")
print("2. Tingkat Dua")
print(">>>Contoh (a)<<<")
print("a and b = ",a and 2+2==4 and 2-2==2)
print("a and a = ",a and 5>3)
print("b and b = ",b and "aku makan kue")
print("---------------------")

print(">>>Contoh (b)<<<")
print("a or b = ",a or 2==4)
print('''"kucing" or "ayam" =  ''',"kucing" or "ayam")
print('''"buku" or 2.5 = ''',"buku" or 2.5)
print("---------------------")

print(">>>Contoh (c)<<<")
print("not(20) = ",not(20))
print('''not("bayam") = ''',not("bayam"))
print("---------------------")


