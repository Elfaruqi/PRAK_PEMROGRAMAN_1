print("====PROGRAM MENCARI FPB")

#mendefinisikan fungsi
def hitung_fpb(x, y):

    #memilih bilangan yang paling kecil
    if x > y:
        terkecil = y
    else:
        terkecil = x
    for i in range(1, terkecil+1):
        if((x % i == 0) and (y % i==0)):
            fpb = i
    return fpb

nilai = int(input("Masukkan bilangan pertama: "))
nilai2 = int(input("Masukkan bilangan kedua: "))
print("FPB = ",hitung_fpb(nilai, nilai2))               


