# =========================================
# TUGAS PRAKTIKUM MINGGU 1
# Nama: RUKMANA ABDI FEBRYANSAH 
# =========================================

import sys

print("="*40)
print("4.1 ANALISIS OBJEK (ALIASING)")
print("="*40)

# Membuat list a
a = [1, 2, 3]

# b adalah alias dari a
b = a

print("Sebelum diubah:")
print("List a:", a)
print("List b:", b)

# Mengubah isi list a
a[0] = 100

print("\nSetelah diubah:")
print("List a:", a)
print("List b:", b)

print("\nPenjelasan:")
print("List b ikut berubah karena b dan a menunjuk ke alamat memori yang sama (aliasing).")

print("\n" + "="*40)
print("4.2 EKSPLORASI TIPE DATA (MEMORI)")
print("="*40)

# Integer
x = 10

# List berisi satu integer
y = [10]

print("Nilai integer x =", x)
print("Nilai list y =", y)

print("\nUkuran memori:")
print("Integer:", sys.getsizeof(x), "bytes")
print("List   :", sys.getsizeof(y), "bytes")

print("\nKesimpulan:")
print("List menggunakan memori lebih besar dibanding integer karena menyimpan struktur tambahan.")