print('Tugas')

jenis1=" "
jenis2=" "

print("===Program Kasir Sederhana===")
nama=input("Masukkan Nama konsumen: ")
tgl=input("Tanggal pembelian: ")
print("Nama Konsumen: ",nama)
print("Tanggal Pembelian: ",tgl)


print()
print("Produk Pakaian")
def pilihan(i):
     daftar={
         1: '----Celana sarung = Rp.150.000----',
         2: '----Celana jeans = Rp.100.000----',
         3: '----Jaket = Rp.200.000----',
         4: '----Baju Muslim = Rp.170.000----',
         }
     return daftar.get(i,"Masukkan Pilihan Yang Benar!")
print("1. Celana sarung")
print("2. Celana jeans")
print("3. Jaket")
print("4. Baju Muslim")
nomor=int(input("Masukkan Pilihan: "))


c=pilihan(nomor)
print(c)

jumlah1=int(input("Banyak unit yang dibeli: "))
if nomor==1:
     a=jumlah1*150000
     print("Sub-Total= Rp. ",a)
     jenis1=("Celana sarung")
if nomor==2:
     a=jumlah1*100000
     print("Sub-Total= Rp. ",a)
     jenis1=("Celana jeans")
if nomor==3:
     a=jumlah1*200000
     print("Sub-Total= Rp. ",a)
     jenis1=("Jaket")
if nomor==4:
     a=jumlah1*170000
     print("Sub-Total= Rp. ",a)
     jenis1=("Baju Muslim")

     
def pilihan (i):
     daftar2={
         1: '----Baju Gamis = Rp.100.000----',
         2: '----Jilbab pasmina = Rp.40.000----',
         3: '----Rok plisket = Rp.75.000----',
         4: '----Kemeja= Rp.95.000----',
         }
     return daftar2.get(i,"Masukkan Pilihan Yang Benar!")


print("\nProduk Celana")
print("1. Baju Gamis")
print("2. Jilbab pasmina")
print("3. Rok plisket")
print("4. Kemeja")
nomor=int(input("Masukkan Pilihan: "))


c=pilihan(nomor)
print(c)

jumlah2=int(input("Banyak unit yang dibeli: "))
if nomor==1:
    b=jumlah2*100000
    print("Sub-Total= Rp. ",b)
    jenis2=(" Baju Gamis")
if nomor==2:
    b=jumlah2*40000
    print("Sub-Total= Rp. ",b)
    jenis2=("Jilbab pasmina")
if nomor==3:
    b=jumlah2*75000
    print("Sub-Total= Rp. ",b)
    jenis2=("Rok plisket")
if nomor==4:
    b=jumlah2*95000
    print("Sub-Total= Rp. ",b)
    jenis2=("Kemeja")

    print()
    print(">>>Total Belanja= Rp.",a+b)
        
uang=int(input("\nUang Tunai: Rp."))
akhir=int(uang-(a+b))
print("|==============================|")
print("|============ STRUK =============|")
print("|==============================|")
print ("========     Nama : ",nama,"               =========")
print ("========     Tanggal : ",tgl,"                =========")
print ("========      Beli: ",jumlah1,jenis1,"    =========")
print ("========      Beli: ",jumlah2,jenis2, "   =========")
print ("========      Tagihan: Rp. ",a+b, "       =========")
print ("========      Bayar: Rp. ",uang, "         =========")
print ("========      Kembalian: Rp. ",akhir,"  =========")
print("|==============================|")
print ("|========= TERIMA KASIH ===========|")
print ("|=== TELAH BERBELANJA DI TOKO SURYA  ===|")
print ("| ============================= |")
