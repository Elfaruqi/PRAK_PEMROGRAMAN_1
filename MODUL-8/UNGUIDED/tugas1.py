def linear_search(database, target):
    for number in database:
        if number == target:
            return True
    return False


database = ["R 2477 SR", "R 1234 DJ", "R 7015 LP", "R 0201 RR", "R 3304 DA", "R 2401 SK", "R 2103 RT", "R 1708 RI", "R 1111 SR", "R 4987 LH"]


target = input("Masukkan nomor plat kendaraan target: ")


if linear_search(database, target):
    print("Nomor plat kendaraan", target, "terdapat dalam database.")
else:
    print("Nomor plat kendaraan", target, "tidak terdapat dalam database.")
