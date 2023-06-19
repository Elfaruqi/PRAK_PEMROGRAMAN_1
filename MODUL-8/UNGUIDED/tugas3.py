def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Daftar bilangan acak
numbers = [17, 2, 15, 7, 72, 31, 12, 57, 63, 71, 23, 92, 1]

# Urutkan daftar bilangan acak secara ascending
numbers.sort()

target = int(input("Masukkan angka yang dicari: "))

print("Daftar bilangan acak:", numbers)

result = binary_search(numbers, target)

if result != -1:
    print("Angka ditemukan di indeks ke-", result)
else:
    print("Angka tidak ditemukan dalam daftar.")
