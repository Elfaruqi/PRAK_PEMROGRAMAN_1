# Program Python untuk menghitung hasil pangkat suatu bilangan
# Meminta input dari pengguna untuk bilangan yang akan dipangkatkan dan pangkatnya
bilangan = int(input("Masukkan bilangan: "))
pangkat = int(input("Masukkan pangkat: "))

# Inisialisasi variabel hasil
hasil = 1

# Menggunakan statement perulangan for untuk menghitung hasil pangkat
for i in range(pangkat):
    hasil *= bilangan

# Mencetak hasil pangkat
print("Hasil pangkat dari {}^{} adalah: {}".format(bilangan, pangkat, hasil))
