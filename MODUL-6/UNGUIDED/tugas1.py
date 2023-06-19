def check_odd_even():
    number = get_number_input()
    if number % 2 == 0:
        print(f"{number} adalah bilangan genap")
    else:
        print(f"{number} adalah bilangan ganjil")

def get_number_input():
    number = int(input("Masukkan sebuah bilangan: "))
    return number

def main():
    check_odd_even()

main()
