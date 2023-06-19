gender = input("Perempuan atau laki-laki ? (L/P): ")

if (gender == 'L'):
    status = input ("Anda sudah menikah atau belum? (Y/N): ")
    if(status == 'Y'):
        print("Hallo Bapak!")
    elif(status == 'N'):
        print("Hallo Mas!")
    else:
        print("Tidak ada dalam pilihan")
elif(gender == 'P') :  
        status = input("Anda sudah menikah belum? (Y/N): ")
        if(status == 'Y'):
            print("Hallo Ibu!")
        elif(status == 'N'): 
            print("Hallo Mas!")
        else:
            print("Tidak ada dalam Pilihan")
else:
    print("Tidak ada dalam Pilihan")                               