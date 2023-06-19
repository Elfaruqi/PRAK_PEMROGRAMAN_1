print("======LOGIN SEDERHANA======")

login = 0
while True:
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if login == 3:
        print("login gagal! Kesempatan mencoba sudah habis. Silahkan coba lagi nanti!")
        break
    
    if username == "adil el-faruqi" and password == "12345678":
        print("Selamat datang ", username, "!")
        break
    else:
        print("Coba cek kembali, username atau password salah!")
        login += 1