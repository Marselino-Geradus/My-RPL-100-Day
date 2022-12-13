# if dalam if menggunakan perulangan 'while'
lulus =  input("Yakin kamu lulus? [ya/tidak]: ")

while True:
    if lulus == "ya":
        nilai = int(input("Masukkan nilai kamu: "))
        if nilai >= 85 and nilai <= 100:
            print("Nilaimu = A. ")
        elif nilai >= 75 and nilai <= 84:
            print("Nilaimu = B. ")
        else:
            print("Kalo nilaimu segitu, artinya kamu gak lulus. Tetap semangat untuk mendapat nilai yang terbaik.")
    else:
        print("Jangan menyerah! Tetap semangat belajarnya. Ini demi masa depan kamu bro! Salam Hangat:)")
        break
