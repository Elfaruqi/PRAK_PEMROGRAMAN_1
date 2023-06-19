def insertionSort(judulBuku):
    n = len(judulBuku)

    for i in range(1, n):
        key = judulBuku[i]
        j = i - 1
        while j >= 0 and judulBuku[j] > key:
            judulBuku[j + 1] = judulBuku[j]
            j -= 1
        judulBuku[j + 1] = key

    return judulBuku

totalBuku = int(input("Masukkan Total Buku: "))
judulBuku = []

for i in range(totalBuku):
    judul = input("Masukkan judul ke-{}: ".format(i + 1))
    judulBuku.append(judul)

print("\n<=== === == Urutkan ? == === ===>")
print("1. Insertion Ascending")
print("2. Insertion Descending")

pilih = int(input("Pilih: "))

if pilih == 1:
    print("\nSorting Buku Secara Ascending")
    judulBuku = insertionSort(judulBuku)
elif pilih == 2:
    print("\nSorting Buku Secara Descending")
    judulBuku = insertionSort(judulBuku)[::-1]
else:
    print("Pilihan tidak valid.")

print("\n")
for i, judul in enumerate(judulBuku):
    print("Judul Buku ke-{}: {}".format(i + 1, judul))
