a = 7
b = 3
c = a+b
print('a\nb\nc')
print("Hasil =",c)
print("ini baris baru")

nama=(input("Masukan Nama Anda :"));
print("Program Hitung Lusa Lingkaran");
print("==================================");
print(nama);
PHI = 3.14
r = int(input("Masukan Nilai Jari-Jari: "))
# r = 10
Luas = PHI*r**2
print("Hasil Luas Lingkaran = ",Luas)
print("==========================================================");

# mhs_c = 25
# mhs_d = 18

def bandingkan_dan_tampilkan(bil1, bil2):
    if bil1 > bil2:
        print(f"Bilangan {bil1} lebih besar dari bilangan {bil2}.")
    elif bil2 > bil1:
        print(f"Bilangan {bil2} lebih besar dari bilangan {bil1}.")
    else:
        print("Kedua bilangan tersebut sama besar.")

# Input dua bilangan dari pengguna
bilangan1 = float(input("Masukkan bilangan pertama: "))
bilangan2 = float(input("Masukkan bilangan kedua: "))

# Memanggil fungsi untuk membandingkan dan menampilkan bilangan yang lebih besar
bandingkan_dan_tampilkan(bilangan1, bilangan2)
print("==========================================================");

# Program Python dengan perulangan for

# Mencetak angka dari 1 hingga 10
for i in range(1, 11):
    print(i)
print("==========================================================");

# Program Python dengan loop

# Mencetak angka dari 1 hingga 10
i = 1
while i <= 10:
    print(i)
    i += 1
