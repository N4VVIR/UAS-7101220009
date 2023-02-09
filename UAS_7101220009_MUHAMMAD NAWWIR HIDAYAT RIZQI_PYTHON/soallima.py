# Buat program menghitung harga penjualan buku dengan output berikut ini. Harga
# buku, jumlah pembelian buku dan diskon (dalam %) merupakan input. (15 point)

print("\n======PROGRAM PENJUALAN BUKU======\n")

buku = float(input("Harga satuan : Rp. "))
jumlah = float(input("Jumlah pembelian buku : "))
diskon = float(input("Diskon % : "))
print("\n-----------------------------------")

hsatuan = buku * jumlah
disk = hsatuan * (diskon / 100)
htotal = hsatuan - disk

print("\nHarga satuan : Rp.", int(buku))
print("Jumlah pembelian :", int(jumlah), "buku")
print("Diskon :", int(diskon), "%")
print("Total harga : Rp.", int(htotal))
print("\n----------------------------------\n")