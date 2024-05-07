class Pegawai:
    def __init__(self, nama, jabatan, gajipokok):
        self.nama = nama
        self.jabatan = jabatan
        self.pajak = 0.1  # Pajak 10%
        self.gajipokok = gajipokok
        self.__gajibersih = 0  # Modifier private

    # Getter untuk atribut gajibersih
    def get_gajibersih(self):
        return self.__gajibersih

    # Setter untuk atribut gajibersih
    def set_gajibersih(self, gajibersih):
        self.__gajibersih = gajibersih

    # Metode untuk menghitung gajibersih berdasarkan ketentuan
    def hitung_gajibersih(self):
        self.__gajibersih = self.gajipokok - (self.gajipokok * self.pajak)


# Main program
if __name__ == "__main__":
    # Membuat objek Pegawai
    pegawai1 = Pegawai("Bryan OKtoviano Ramadhan", "Manager", 5000)

    # Menghitung gajibersih menggunakan metode hitung_gajibersih
    pegawai1.hitung_gajibersih()

    # Menampilkan hasil perhitungan dengan mengakses atribut gajibersih
    print(f"Nama: {pegawai1.nama}")
    print(f"Jabatan: {pegawai1.jabatan}")
    print(f"Gaji Pokok: {pegawai1.gajipokok}")
    print(f"Gaji Bersih: {pegawai1.get_gajibersih()}")
