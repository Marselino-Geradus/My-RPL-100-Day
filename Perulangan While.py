'>>>Contoh Soal 1<<<'
print('>>>Contoh Soal 1<<<')
jawab = 'ya'
hitung = 0

while(jawab == 'ya'):
    hitung += 1
    jawab = input("Ulang lagi tidak? ")

print(f"Total perulangan: {hitung}")
print('\n' *2)



">>>Contoh soal 2<<<"
print(">>>Contoh soal 2<<<")
jumlah = 0
while True:
    jumlah += 1
    nama = input("Masukkan sandi: ")
    if nama == 'marsel':
        print("Sandi yang Anda masukkan benar!")
        print(f"Jumlah pengulangan sandi: {jumlah}")
        break
    else:
        print("Sandi yang Anda masukkan salah!. Silakan coba lagi.")
        
