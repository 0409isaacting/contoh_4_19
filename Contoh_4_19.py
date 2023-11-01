#Contoh_4_19
def corak(aksara,bilangan):
    print(aksara*bilangan)
def menu():
    print("1.Penyulitan(Encrption)")
    print("2.Nyahsulit(Decryption)")
def mesej():
    teks=str(input("Masukkan nama anda:"))
    return teks
def songsang(ayat):
    str=""
    for i in ayat:
        str=i + str
    print("")
    corak("#",len(str))
    print(str)
    corak("#",len(str))

corak("*",32)
print("Penyulitan/Penyahsulitan Mesej")
print(corak("*",32))
menu()
print("")
pilihan=int(input("Masukkan pilihan anda"))

if pilihan ==1:
    mesej_asal=str(input("Masukkan mesej anda:"))
    songsang(mesej_asal)
else:
    mesej_sulit=str(input("Masukkan mesej sulit anda:"))
    songsang(mesej_sulit)
        
