def bilangan(a, b):
    if a > b:
        return a
    else:
        return b

# Input nilai pertama
nilai1 = (input("Masukkan bilangan 1: "))

# Input nilai kedua
nilai2 = (input("Masukkan bilangan 2: "))

# Memanggil fungsi untuk mencari nilai terbesar
nilai_terbesar = bilangan(nilai1, nilai2)

# Menampilkan nilai terbesar
print("Bilangan yang lebih besar adalah:", nilai_terbesar)
