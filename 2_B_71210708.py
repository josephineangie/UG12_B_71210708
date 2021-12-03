

daftar_nama = []
daftar_kursi = []
print()

while True:
    nama = input("Masukkan nama : ")
    if nama == "STOP":
        break
    noKursi = int(input("Masukkan nomor kursi %s : " % nama))
    if noKursi not in daftar_kursi:
        daftar_nama.append(nama)
        daftar_kursi.append(noKursi)
    else:
        print("Mohon maaf kursi tersebut telah terisi!")

print("\nList kursi yang telah terisi :")
for i in range(len(daftar_nama)):
    print("Kursi nomor", daftar_kursi[i], "telah diisi oleh", daftar_nama[i])
print()
