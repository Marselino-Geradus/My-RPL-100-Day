print('''
==================================
USIA PENDIDIKAN ANAK INDONESIA SECARA UMUM
==================================''')
print()

a = int(input("Masukkan umur Anda: "))
if a  >= 7 and a <= 12:
    print("Anda termasuk anak SD.")
elif a  >= 13 and a <= 15:
    print("Anda termasuk anak SMP.")
elif a  >= 16 and a <= 18:
    print("Anda termasuk anak SMA.")
elif a  >= 19 and a <= 25:
    print("Anda termasuk Mahasiswa.")
else:
    print("Anda tidak sedang dalam bangku pendidikan.")
