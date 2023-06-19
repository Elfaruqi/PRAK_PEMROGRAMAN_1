# Program Python untuk menghitung total nilai dari suatu bilangan yang diinputkan
# Meminta input dari pengguna untuk jumlah bilangan yang akan dijumlahkan
n = int(input("Masukkan jumlah bilangan = "))

# Inisialisasi variabel total
total = 0

# Menggunakan statement perulangan for untuk meminta input bilangan dan menghitung total
for i in range(n):
    bilangan = int(input("Masukkan bilangan ke-{}: ".format(i+1)))
    total += bilangan

# Mencetak total nilai
print("Total nilai dari {} bilangan yang diinputkan adalah: {}".format(n, total))
