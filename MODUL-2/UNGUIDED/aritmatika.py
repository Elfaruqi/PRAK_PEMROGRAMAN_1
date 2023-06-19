# Program Python untuk menghitung volume sebuah bangun ruang
# Fungsi untuk menghitung volume sebuah kubus
def hitung_volume_kubus(sisi):
    volume = sisi ** 3
    return volume

# Fungsi untuk menghitung volume sebuah balok
def hitung_volume_balok(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi
    return volume

# Fungsi untuk menghitung volume sebuah bola
def hitung_volume_bola(jari_jari):
    volume = (4/3) * 3.14 * jari_jari ** 3
    return volume

# Meminta input dari pengguna untuk memilih bangun ruang yang ingin dihitung volumenya
print("Pilih bangun ruang:")
print("1. Kubus")
print("2. Balok")
print("3. Bola")
pilihan = int(input("Masukkan pilihan Anda (1/2/3): "))

# Memeriksa pilihan pengguna dan meminta input yang diperlukan
if pilihan == 1:
    sisi = float(input("Masukkan panjang sisi kubus: "))
    print("Volume kubus adalah:", hitung_volume_kubus(sisi))
elif pilihan == 2:
    panjang = float(input("Masukkan panjang balok: "))
    lebar = float(input("Masukkan lebar balok: "))
    tinggi = float(input("Masukkan tinggi balok: "))
    print("Volume balok adalah:", hitung_volume_balok(panjang, lebar, tinggi))
elif pilihan == 3:
    jari_jari = float(input("Masukkan jari-jari bola: "))
    print("Volume bola adalah:", hitung_volume_bola(jari_jari))
else:
    print("Pilihan tidak valid")
