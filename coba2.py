class Mhs:
    def __init__(self, nama):
        self.nama = nama
        
    def belajar(self, kondisi):
        print(self.nama, 'sedang belajar', kondisi)
        
    def malas(self):
        print(self.nama, 'tidur')

nama = input("Masukan nama: ")
mhs = Mhs(nama)

if nama.lower() != 'bryan':  # Mengonversi nama ke huruf kecil dan memeriksa apakah tidak sama dengan 'bryan'
    mhs.malas()  # Jika nama bukan 'Bryan', panggil metode malas
else:
    mhs.belajar("dengan giat")  # Jika nama adalah 'Bryan', panggil metode belajar dengan kondisi 'dengan giat'
