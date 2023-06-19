def bubble_sort(keywords, nim):
    for i in range(len(nim)):
        for j in range(len(nim)-i-1):
            if nim[j] > nim[j+1]:
                nim[j], nim[j+1] = nim[j+1], nim[j]
    return binary_search(keywords, nim)

def binary_search(keywords, nim):
    left = 0
    right = len(nim) - 1
    while left <= right:
        mid = (left + right)//2
        if str(nim[mid]).lower() > keywords.lower():
            right = mid - 1
        elif str(nim[mid]).lower() < keywords.lower():
            left = mid + 1
        else:
            print(nim) 
            print(f"Keyword '{keywords}' nim ditemukan di indeks {mid}")
            return mid

    print(f"Keyword '{keywords}' not found")
    return -1

nim = [20103023, 20103002, 20103019, 20103001, 20103017, 20103005, 20103011, 20103003, 20103009, 20103021, 20103006, 20103015, 20103013, 20103007]
keywords = input("Masukkan keywords: ")
bubble_sort(keywords, nim)
