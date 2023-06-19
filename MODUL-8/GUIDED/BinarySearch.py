def bubble_sort(keywords, data):
    for i in range(len(data)):
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return binary_search(keywords, data)

def binary_search(keywords, data):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] > int(keywords):
            right = mid - 1
        elif data[mid] < int(keywords):
            left = mid + 1
        else:
            print(data)
            print(f"Keyword '{keywords}' has been found at index {mid}")
            return mid

    print(f"Keyword '{keywords}' not found")
    return -1

data = [23, 3, 4, 78, 9, 10, 32]
keywords = input("Masukkan keywords: ")
bubble_sort(keywords, data)
