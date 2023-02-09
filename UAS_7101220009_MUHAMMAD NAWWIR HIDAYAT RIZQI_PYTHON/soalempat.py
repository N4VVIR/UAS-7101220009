# Tentukan keluaran dari algoritma pseudocode berikut ini: (10 point)
# Diketahui masukan A dan B masing-masing adalah 3 dan 9.

# Algoritma Ngoprek

print("\n===== Algoritma Ngoprek =====\n")

# Deklarasi :
#   read(A, B)

a = 3
b = 9

# Algoritma :
#   if A > B then
#     C <- A * B
#   else
#     C <- A + B
#     D <- C * C
#   write(C, D)   

if a > b:
    c = a * b
    print("\nC", "=", c)
else:
    c = a + b
    print("\nC", "=", c)    
    d = c * c
    print("\nD", "=", d)
    
print("\n---------------------------")