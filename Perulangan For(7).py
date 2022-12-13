while True:
    #Contoh 1
    makan = int(input('Makan berapa kali/hari?: '))
    for i in range(1,makan+1):
        print(f"Aku makan {makan}x sehari."*i)
    print()

    #Contoh 2
    mandi = int(input("Mandi berapa kali/hari? : "))
    for j in range (1,3):
        print(f"Aku mandi {mandi}x sehari. "*j)
    print()
