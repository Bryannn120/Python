# Program Biodata Sederhana dengan Percabangan

# Input data dari user
nama = input("Masukkan nama Anda: ")
umur = int(input("Masukkan umur Anda: "))
hobi = input("Masukkan hobi Anda: ")

# Menampilkan output
print("\nNama Anda adalah " + nama)
print("Anda berumur " + str(umur) + " tahun")
# Percabangan untuk menentukan tingkat kedewasaan
if umur < 20:
    print("Anda masih anak-anak")
else:
    print("Anda sudah dewasa")
print("Hobi Anda adalah " + hobi)
