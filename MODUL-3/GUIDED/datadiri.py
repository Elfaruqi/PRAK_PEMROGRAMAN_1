print("=========INPUT=========")
nama = input("Nama: ")
jk = input("Jenis Kelamin (L/P): ")
agama = int(input("Agama: "))
#1=Islam, 2=Protestan, 3=Katolik, 4=Hindu, 5=Budha
if(agama==1):
    agama = "Islam"
elif(agama==2):
    agama = "protestan"
elif(agama==3):
    agama = "Katolik"
elif(agama==4):
    agama = "Hindu"
elif(agama==5):
    agama = "Budha"
else:
    agama = "Agama tidak ditemukan"

print("=========OUTPUT=========")
print("Nama: ",nama) 
print("jenis Kelamin: ",jk)
print("Agama: ",agama)                      

