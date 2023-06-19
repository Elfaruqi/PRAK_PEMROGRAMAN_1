# Program Python untuk menentukan KPK dari dua bilangan
# Meminta input dari pengguna untuk dua bilangan
bilangan1 = int(input("Masukkan bilangan pertama: "))
bilangan2 = int(input("Masukkan bilangan kedua: "))

# Menentukan bilangan terbesar dari kedua bilangan
if bilangan1 > bilangan2:
    bilangan_terbesar = bilangan1
else:
    bilangan_terbesar = bilangan2

# Menggunakan statement perulangan while untuk menentukan KPK
while True:
    if bilangan_terbesar % bilangan1 == 0 and bilangan_terbesar % bilangan2 == 0:
        kpk = bilangan_terbesar
        break
    bilangan_terbesar += 1

# Mencetak KPK
print("KPK dari {} dan {} adalah {}".format(bilangan1, bilangan2, kpk))
