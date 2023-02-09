# Sebuah komputer dijual secara kredit selama setahun sehingga harganya (hkredit)
# bertambah 20% dari harga normal (hnormal). Agar bisa membeli secara kredit,
# pembeli harus membayar uang muka (umuka) sebesar 30% dari harga kredit.
# Buatlah algoritma menghitung besarnya uang muka dan cicilan (ucicil) setiap bulan
# dengan masukkan harga normal. (15 point)

print("\n========== Program Menghitung Besaran Uang Muka Dan Cicilan Setiap Bulan ==========\n")
print("-----------------------------------------------------------------------------------\n")

harga_normal = float(input("Harga normal : Rp. "))

print("\n-----------------------------------------------------------------------------------\n")

hnormal = harga_normal * 0.2
print("Bunga", "20%", "=", int(hnormal), "/ bulan")

hkredit = harga_normal + (hnormal * 12)
print("Harga Beli Secara Kredit : Rp.:", int(hkredit))

umuka = hkredit * 0.3
print("Bersarnya Uang Muka : Rp.:", int(umuka))

ucicil = (hkredit - umuka) / 12
print("Besarnya Cicilan : Rp.:", int(ucicil), "/ bulan")
print("\n-----------------------------------------------------------------------------------\n")



