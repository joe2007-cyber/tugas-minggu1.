# Tugas Praktikum Minggu 1

## 👤 Nama
RUKMANA ABDI FEBRYANSAH

## 📚 Deskripsi
Tugas ini membahas:
1. Analisis objek (aliasing)
2. Perbandingan penggunaan memori pada tipe data Python

---

## 🔹 4.1 Analisis Objek (Aliasing)

Program menunjukkan bahwa jika list `a` diubah, maka list `b` juga ikut berubah.

Hal ini terjadi karena:
- `b = a` tidak membuat data baru
- tetapi hanya menunjuk ke alamat memori yang sama

---

## 🔹 4.2 Eksplorasi Tipe Data

Program membandingkan:
- Integer
- List yang berisi satu integer

Menggunakan:
```python
sys.getsizeof()
