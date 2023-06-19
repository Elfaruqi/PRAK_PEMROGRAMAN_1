# Meminta input dari pengguna
kalimat = input("Masukkan sebuah kalimat: ")

# Memecah kalimat menjadi kata-kata
kata_kata = kalimat.split()

# Menampilkan jumlah kata
jumlah_kata = len(kata_kata)
print("Jumlah kata: ", jumlah_kata)

# Menampilkan array kata-kata
print("Array kata-kata:")
for kata in kata_kata:
    print(kata)
