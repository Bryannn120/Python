user_credentials = {
    "teeja": "123", 

}

def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if username in user_credentials and user_credentials[username] == password:
        print("Login berhasil!")
        return username 
    else:
        print("Username atau password salah.")
        return None

def hitung_nilai_huruf(nilai_akhir):
    if nilai_akhir >= 80 and nilai_akhir <= 100:
        return "A"
    elif nilai_akhir >= 70 and nilai_akhir <= 79:
        return "B"
    elif nilai_akhir >= 60 and nilai_akhir <= 69:
        return "C"
    else:
        return "D"

def main():
    print("Selamat datang di Perhitungan Nilai!")
    username = None
    while username is None:
        username = login() 
    
    logged_in = True
    while logged_in:
        nilai_mhs = int(input('Silahkan masukkan nilai kamu: '))
        print('Selamat', username, ', kamu mendapatkan nilai =', hitung_nilai_huruf(nilai_mhs))
        
        opsi = input("Apakah Anda ingin melanjutkan? (ya/tidak): ")
        if opsi.lower() != 'ya':
            logged_in = False
            print("Logout berhasil!")

if __name__ == "__main__":
    main()
