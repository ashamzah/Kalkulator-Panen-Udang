# Kalkulator Panen Udang

Aplikasi Python berbasis terminal untuk mengelola data panen udang dan menghitung estimasi keuntungan panen.

## Deskripsi

`Kalkulator_Panen_Udang.py` adalah program sederhana berbasis command line yang dibuat untuk membantu pencatatan dan perhitungan data panen udang. Data panen disimpan dalam bentuk list, kemudian dapat ditampilkan, ditambah, diubah, dihapus, serta digunakan untuk menghitung keuntungan panen.

## Fitur

Aplikasi ini memiliki beberapa fitur utama:

1. Menampilkan report seluruh data panen
2. Menampilkan report data panen tertentu
3. Menambah data panen baru
4. Mengubah data panen
5. Menghapus data panen
6. Menghitung keuntungan panen berdasarkan:

   * Total income
   * Total cost
   * Feed cost per kg udang
   * Profit/Loss
   * Profit/Loss per kg udang
   * Gross margin
   * ROI

## Struktur Data

Data panen disimpan dalam format list di dalam list:

```python
["Panen1", DOC, Size, Biomass, Harga]
```

Contoh:

```python
dataPanen = [
    ["Panen1", 60, 93, 200, 72500],
    ["Panen2", 70, 77, 200, 90000],
    ["Panen3", 80, 68, 200, 100000],
    ["Panen4", 90, 61, 200, 110000]
]
```

Keterangan:

* `Panen` = Nama / nomor panen
* `DOC` = Umur panen dalam hari
* `Size` = Ukuran udang dalam pcs/kg
* `Biomass` = Total biomass panen dalam kg
* `Harga` = Harga jual udang per kg

## Cara Menjalankan Program

Pastikan Python sudah terinstall di komputer.

Jalankan program melalui terminal atau command prompt:

```bash
python Kalkulator_Panen_Udang.py
```

Atau jika menggunakan Anaconda:

```bash
python "Kalkulator_Panen_Udang.py"
```

## Menu Aplikasi

Saat program dijalankan, user akan melihat menu utama:

```text
1. Report Data Panen
2. Menambah Data Panen
3. Mengubah Data Panen
4. Menghapus Data Panen
5. Menghitung Keuntungan Panen
6. Exit Program
```

User cukup memasukkan angka menu yang ingin dijalankan.

## Perhitungan Finansial

Beberapa rumus yang digunakan dalam aplikasi:

```text
Total Income = Biomass x Harga Jual

Total Pakan = FCR x Total Biomass

Total Biaya Pakan = Harga Pakan x Total Pakan

Total Cost = Total Biaya Pakan + Listrik + Gaji + Kimia + Biaya Lain

Profit/Loss = Total Income - Total Cost

Profit/Loss per kg = Profit/Loss / Total Biomass

Feed Cost per kg = Total Biaya Pakan / Total Biomass

Gross Margin = Profit/Loss / Total Income x 100

ROI = Profit/Loss / Total Cost x 100
```

## Klasifikasi Hasil Panen

Aplikasi juga memberikan keterangan hasil panen berdasarkan nilai ROI:

```text
ROI >= 30%  : Sangat Menguntungkan
ROI >= 15%  : Menguntungkan
ROI >= 0%   : Tipis / Perlu Efisiensi
ROI < 0%    : Rugi
```

## Catatan

Aplikasi ini dibuat sebagai latihan dasar Python dengan konsep:

* List
* Looping
* Conditional statement
* Function
* CRUD sederhana
* Perhitungan finansial sederhana
* Program berbasis terminal

Nonton Video : https://youtu.be/_zlNngn_4-s

## Author

Dibuat oleh Aris Sando Hamzah.

Personal Blog : https://arissandohamzah.hantulaut.web.id
