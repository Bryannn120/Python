# Daftar pengguna dan sandi
user_credentials = {
    "adelia": "123",
    "adeng": "456",
    "adel": "789"
}

def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if username in user_credentials and user_credentials[username] == password:
        print("Login berhasil!")
        return True
    else:
        print("Username atau password salah.")
        return False

def calculator():
    while True:
        print("\nOperasi yang tersedia:")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Keluar")
        
        choice = input("Pilih operasi (1/2/3/4/5): ")
        
        if choice == '5':
            print("Terima kasih telah menggunakan kalkulator.")
            break
        
        num1 = float(input("Masukkan bilangan pertama: "))
        num2 = float(input("Masukkan bilangan kedua: "))
        
        if choice == '1':
            print("Hasil:", num1 + num2)
        elif choice == '2':
            print("Hasil:", num1 - num2)
        elif choice == '3':
            print("Hasil:", num1 * num2)
        elif choice == '4':
            if num2 == 0:
                print("Error: Pembagian dengan nol tidak diizinkan.")
            else:
                print("Hasil:", num1 / num2)
        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")

# Fungsi utama
def main():
    print("Selamat datang di kalkulator!")
    logged_in = False
    while not logged_in:
        logged_in = login()
    calculator()

if __name__ == "__main__":
    main()
