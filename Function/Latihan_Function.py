#!/usr/bin/env python
# coding: utf-8

# In[1]:


#FPB adalah bilangan bulat positif terbesar yang dapat membagi habis dua atau lebih bilangan bulat.
#KPK adalah bilangan bulat positif terkecil yang dapat dibagi habis oleh dua atau lebih bilangan bulat.

#Fungsi python untuk perhitungan FPB
def hitung_fpb(a, b): #Fungsi hitung_fpb di defenisikan dengan 2 parameter, yaitu inpuan a dan b
    while b != 0: # while loop yang mana b tidak boleh sama dengan 0
        a, b = b, a % b
    return a

#Fungsi python untuk perhitungan KPK
def hitung_kpk(a, b): 
    if a == 0 or b == 0:
        return 0
    kpk = max(a, b)
    while True:
        if kpk % a == 0 and kpk % b == 0:
            return kpk
        kpk += 1

def tampilkan_menu(): #menu pilihan untuk mencari FPB dan KPK atau mau keluar dari program
    print("----- MENU PILIHAN -----")
    print("1. Menghitung FPB")
    print("2. Menghitung KPK")
    print("3. Keluar")

def main():
    while True:
        tampilkan_menu()
        try:
            print(" ")
            pilihan = int(input("Masukkan pilihan Anda: ")) #inputan untuk memilih pilihan yang akan dicari user
        except ValueError:
            print("Input data tidak valid, mohon input dengan benar") #ketika inputan salah / tidak sesuai dengan option
            continue

        if pilihan == 1: #case1 untuk mencari FPB
            try:
                print(" ")
                a = int(input("Masukkan bilangan A : ")) #inputan untuk bil.A
                b = int(input("Masukkan bilangan B: ")) #inputan untuk bil.B
            except ValueError:
                print("Input data tidak valid, mohon input dengan benar")
                continue
            fpb = hitung_fpb(a, b)
            print("FPB dari", a, "dan", b, "adalah", fpb) #data yang diinpukan diproses(hitung_fpb dari a & b) kemudian di print
            print(" ")

        elif pilihan == 2: #case2 untuk mencari KPK
            try:
                print(" ")
                a = int(input("Masukkan bilangan A : "))
                b = int(input("Masukkan bilangan B : "))
            except ValueError:
                print("Input data tidak valid, mohon input dengan benar") 
                continue
            kpk = hitung_kpk(a, b)
            print("KPK dari", a, "dan", b, "adalah", kpk)
            print(" ")

        elif pilihan == 3: #case 3 keluar dari program
            print("Terima Kasih, SEMOGA SUKSES!!")
            break

        else: 
            print("Input data tidak valid, mohon input dengan benar")

if __name__ == '__main__': # mengevaluasi program
    main()


# In[ ]:




