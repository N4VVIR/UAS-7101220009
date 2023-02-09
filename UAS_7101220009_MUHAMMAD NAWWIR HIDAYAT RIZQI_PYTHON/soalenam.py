print("\n======PROGRAM PERHITUNGAN GAJI KARYAWAN PT. XYZ======\n")
print("-----------------------------------------------------\n")

nama = input("Nama : ")
golongan = input("Golongan : ")
total_jam_kerja = float(input("Total jam kerja (jam) : "))

print("\n---------------------------------------------------\n")
print("\t\tDATA PEGAWAI")
print("\n---------------------------------------------------\n")
print("Nama :", nama)
print("Golongan :", golongan)
print("Total jam kerja :", int(total_jam_kerja), "jam")
print("\n---------------------------------------------------\n")
print("\t\tPERHITUNGAN GAJI")
print("\n---------------------------------------------------\n")

a = 1200000
b = 1600000
c = 2000000

lbr_a = 5000
lbr_b = 7500
lbr_c = 10000

if golongan == "a":
    gapok_a = a
    print("Gaji Pokok : Rp.", int(gapok_a))
elif golongan == "b":
    gapok_b = b
    print("Gaji Pokok : Rp.", int(gapok_b))
elif golongan == "c":
    gapok_c = c
    print("Gaji pokok : Rp.", int(gapok_c))
else:
    gapok = 0
    print("Gaji Pokok : Rp.", int(gapok))

if golongan == "a":
    tjg_a = 0.1 * a
    print("Tunjangan : Rp.", int(tjg_a))
elif golongan == "b":
    tjg_b = 0.15 * b
    print("Tunjangan : Rp.", int(tjg_b))
elif golongan == "c":
    tjg_c = 0.2 * c
    print("Tunjangan : Rp.", int(tjg_c))
else:
    tjg = 0
    print("Tunjangan : Rp.", int(tjg))

if golongan == "a":
    jam_lbr = total_jam_kerja - 200
    lembur_a = lbr_a * (jam_lbr / 60)
    print("Lembur : Rp.", int(lembur_a))
elif golongan == "b":
    jam_lbr = total_jam_kerja - 200
    lembur_b = lbr_b * (jam_lbr / 60)
    print("Lembur : Rp.", int(lembur_b))
elif golongan == "c":
    jam_lbr = total_jam_kerja - 200
    lembur_c = lbr_c * (jam_lbr / 60)
    print("Lembur : Rp.", int(lembur_c))
else:
    lbr = 0
    print("Lembur : Rp.", int(lbr))

if golongan == "a":
    total_a = a + tjg_a + lembur_a
    print("Total : Rp.", int(total_a))
elif golongan == "b":
    total_b = b + tjg_b + lembur_b
    print("Total : Rp.", int(total_b))
elif golongan == "c":
    total_c = c + tjg_c + lembur_c
    print("Total : Rp.", int(total_c))
else:
    total = 0
    print("Total : Rp.", int(total))

print("\n---------------------------------------------------\n")