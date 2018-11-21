x = input("Masukkan Password : ")
if x == "Alif":
    print("Anda Berhasil Login")
else:
    x = input("Maaf, Anda Salah Memasukkan Password. Masukkan Password : ")
    if x == "Alif":
        print("Anda Berhasil Login")
    else:
        print("Anda Telah Mencoba 3 Kali, Akses Anda Ditolak")
