import math

def calculate_area(radius):
    area = math.pi * radius**2
    return area

def calculate_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

def get_radius_input():
    radius = float(input("Masukkan jari-jari : "))
    return radius

def main():
    radius = get_radius_input()
    area = calculate_area(radius)
    circumference = calculate_circumference(radius)

    print(f"Luas lingkaran dengan jari-jari {radius} adalah {area:.2f} satuan luas")
    print(f"Keliling lingkaran dengan jari-jari {radius} adalah {circumference:.2f} satuan panjang")

main()
