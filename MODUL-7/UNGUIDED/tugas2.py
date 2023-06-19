def selectionSort(namaAnggota):
    n = len(namaAnggota)

    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if namaAnggota[j] < namaAnggota[min_idx]:
                min_idx = j

        namaAnggota[i], namaAnggota[min_idx] = namaAnggota[min_idx], namaAnggota[i]

    return namaAnggota

anggotaOrganisasi = ['Zhafira', 'Nirmala', 'Aksara', 'Nalendra', 'Cakra', 'Sastra', 'Agni', 'Bagas', 'Jerome', 'Kiara']
print("Before:", anggotaOrganisasi)

anggotaOrganisasi = selectionSort(anggotaOrganisasi)
print("After :", anggotaOrganisasi)
