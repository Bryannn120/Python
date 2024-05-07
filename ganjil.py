# Program Python sederhana untuk menentukan bilangan genap atau ganjil

def cek_genap_ganjil(bilangan):
    if bilangan % 2 == 0:
        print(f"{bilangan} adalah bilangan genap.")
    else:
        print(f"{bilangan} adalah bilangan ganjil.")

# Input bilangan dari pengguna
bilangan = int(input("Masukkan sebuah bilangan: "))

# Memanggil fungsi untuk mengecek apakah bilangan genap atau ganjil
cek_genap_ganjil(bilangan)
