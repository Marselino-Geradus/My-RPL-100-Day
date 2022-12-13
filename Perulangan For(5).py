makan = int(input("Berapa kali sehari? : "))
#Contoh 1
for a in range(1,makan+1):
    print(f"Aku makan {makan}x sehari." * a)
print()


#Contoh 2
for b in range(1,makan+1):
    print("1"*b)
print()


#Contoh 3
mandi = int(input("Berapa kali? : "))
for c in (1,mandi+1):
    print(f"Aku mandi {makan}x sehari."*c)
print()


#Contoh 4
tidur = int(input("Tidur? : "))
for i in (1,tidur, 2):        #langsung mencetak sesuai dengan apa yang kita 
    print(f"{tidur} kali."*i)
