def cari_kata(array, kata):
    for i, k in enumerate(array):
        if k.lower() == kata.lower():
            return i
    return -1

jumlah_kata = int(input("Masukkan Jumlah Kata: "))

kata_array = []
for i in range(jumlah_kata):
    kata = input("Masukkan kata: ")
    kata_array.append(kata)

kata_cari = input("Masukkan kata yang ingin dicari: ")

indeks = cari_kata(kata_array, kata_cari)
if indeks != -1:
    print(f"{kata_cari} ditemukan di indeks ke-{indeks}")
else:
    print(f"{kata_cari} tidak ditemukan")
