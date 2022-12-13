# Break (Untuk menginterupsi dengan paksa suatu iterasi pada perulangan)
print(">>>Break<<<")
print("Contoh 1")
for i in range (10,20):
    if (i == 15):
        break
    print(i)
print()

print("Contoh 2")
for i in range(20,40):
    if (i == 31):
        break
    print(i)
print('\n'*2)
    
# Continue (Untuk men-skip sebuah data dalam suatu iterasi pada perulangan)
print(">>>Continue<<<")
print("Contoh 1")
for a in range (1,21):
    if (a >= 15 and a <= 18):  #nilai 15-18 akan dilangkahi (di-skip) sehingga tidak akan dimunculkan
        continue
    print(a)
print()

print("Contoh 1")
for j in range (11,21):
    if (j == 15):  #nilai 15 akan dilangkahi (di-skip) sehingga tidak akan dimunculkan
        continue
    print(j)
print()



