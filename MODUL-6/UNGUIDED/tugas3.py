# Definisikan procedure untuk menjumlahkan dua bilangan
def add_numbers(num1, num2):
    result = num1 + num2
    print(f"Hasil penjumlahan: {result}")

# Definisikan procedure untuk mengurangkan dua bilangan
def subtract_numbers(num1, num2):
    result = num1 - num2
    print(f"Hasil pengurangan: {result}")

# Definisikan procedure untuk mengalikan dua bilangan
def multiply_numbers(num1, num2):
    result = num1 * num2
    print(f"Hasil perkalian: {result}")

# Definisikan procedure untuk membagi dua bilangan
def divide_numbers(num1, num2):
    if num2 != 0:
        result = num1 / num2
        print(f"Hasil pembagian: {result}")
    else:
        print("Error: Pembagian dengan nol tidak diizinkan")

# Definisikan procedure untuk menghitung pangkat dua bilangan
def power_numbers(num1, num2):
    result = num1 ** num2
    print(f"Hasil pangkat: {result}")

# Main program
def main():
    while True:
        print("=== KALKULATOR SEDERHANA ===")
        print("Pilih operasi:")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Pangkat")
        print("6. Keluar")

        choice = input("Masukkan pilihan (1-6): ")

        if choice == '1':
            num1 = float(input("Masukkan bilangan pertama: "))
            num2 = float(input("Masukkan bilangan kedua: "))
            add_numbers(num1, num2)
        elif choice == '2':
            num1 = float(input("Masukkan bilangan pertama: "))
            num2 = float(input("Masukkan bilangan kedua: "))
            subtract_numbers(num1, num2)
        elif choice == '3':
            num1 = float(input("Masukkan bilangan pertama: "))
            num2 = float(input("Masukkan bilangan kedua: "))
            multiply_numbers(num1, num2)
        elif choice == '4':
            num1 = float(input("Masukkan bilangan pertama: "))
            num2 = float(input("Masukkan bilangan kedua: "))
            divide_numbers(num1, num2)
        elif choice == '5':
            num1 = float(input("Masukkan bilangan: "))
            num2 = float(input("Masukkan pangkat: "))
            power_numbers(num1, num2)
        elif choice == '6':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Panggil fungsi main untuk menjalankan program
main()
