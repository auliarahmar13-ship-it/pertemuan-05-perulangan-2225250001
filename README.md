

Nama: Aulia Rahma Ramadhani  
NIM: 2225250001  
Kelas: 3A  

---

## Tujuan

Pertemuan 05 membahas penggunaan perulangan dalam pemrograman Python. 
Perulangan digunakan untuk menjalankan suatu proses secara berulang sesuai dengan kondisi atau jumlah pengulangan yang telah ditentukan.

Pada pertemuan ini digunakan dua jenis perulangan, yaitu:

1. Perulangan `for`
2. Perulangan `while`

Melalui latihan dan kuis, program dibuat untuk menyelesaikan beberapa permasalahan sederhana yang membutuhkan proses berulang.

---

## Struktur Folder

Struktur folder pada tugas Pertemuan 05 adalah sebagai berikut:

```text
pertemuan-05-perulangan-2225250001/
│
├── latihan/
│   ├── 01_tabel_perkalian.py
│   ├── 02_jumlah_bilangan.py
│   ├── 03_validasi_input.py
│   └── 04_hitung_genap.py
│
├── kuis/
│   └── kuis2_deret_aritmetika.py
│
└── README.md

## Keterangan File

File	                   
01_tabel_perkalian.py : Menampilkan tabel perkalian dari suatu       bilangan dari 1 sampai 10 menggunakan for.
02_jumlah_bilangan.py : Menghitung jumlah bilangan dari 1 sampai n menggunakan for.
03_validasi_input.py : Memvalidasi nilai ujian agar berada pada rentang 0 sampai 100 menggunakan while.
04_hitung_genap.py	: Menghitung banyaknya bilangan genap dari 1 sampai n menggunakan for.
kuis2_deret_aritmetika.py	: Menghitung suku dan jumlah deret aritmetika menggunakan perulangan while.

---

##Latihan
Latihan 1 - Tabel Perkalian
Nama File
latihan/01_tabel_perkalian.py

##Tujuan
Program menerima satu bilangan bulat dan menampilkan tabel perkalian dari bilangan tersebut mulai dari perkalian 1 sampai perkalian 10.

Konsep yang Digunakan
Program menggunakan perulangan for.

##Algoritma
1. Meminta pengguna memasukkan sebuah bilangan.
2. Menyimpan bilangan tersebut ke dalam variabel n.
3. Melakukan perulangan menggunakan for dari 1 sampai 10.
4. Pada setiap perulangan, bilangan n dikalikan dengan nilai i.
5. Menampilkan hasil perkalian.
6. Perulangan berhenti setelah perkalian ke-10.

| Input | Keluaran yang Diharapkan            |
| ----- | ----------------------------------- |
| `4`   | Tabel perkalian 4 dari 1 sampai 10  |
| `-3`  | Tabel perkalian -3 dari 1 sampai 10 |
Program harus menghasilkan tepat 10 baris keluaran untuk setiap input.

##Latihan 2 - Jumlah 1 sampai n
Nama File
latihan/02_jumlah_bilangan.py

##Tujuan

Program menerima bilangan bulat positif n, kemudian menghitung jumlah:

1 + 2 + 3 + ... + n
Konsep yang Digunakan

Program menggunakan perulangan for.

##Algoritma
1. Meminta pengguna memasukkan bilangan n.
2. Membuat variabel total dan memberikan nilai awal 0.
3. Melakukan perulangan dari 1 sampai n.
4. Setiap nilai i ditambahkan ke dalam total.
5. Setelah perulangan selesai, program menampilkan nilai total.

Test Case
| Input | Keluaran yang Diharapkan |
| ----- | -----------------------: |
| `1`   |                      `1` |
| `5`   |                     `15` |
| `10`  |                     `55` |

Contoh:
n = 5
1 + 2 + 3 + 4 + 5 = 15

##Latihan 3 - Validasi Input
Nama File
latihan/03_validasi_input.py

##Tujuan

Program meminta pengguna memasukkan nilai ujian dari 0 sampai 100.

Jika nilai yang dimasukkan berada di luar rentang tersebut, program meminta pengguna memasukkan nilai kembali sampai mendapatkan nilai yang valid.

Konsep yang Digunakan

Program menggunakan perulangan while dan validasi kondisi.

##Algoritma
1. Meminta pengguna memasukkan nilai ujian.
2. Memeriksa apakah nilai kurang dari 0 atau lebih dari 100.
3. Jika nilai tidak valid, tampilkan pesan bahwa nilai tidak valid.
4. Meminta pengguna memasukkan nilai kembali.
5. Mengulangi proses selama nilai masih berada di luar rentang 0 sampai 100.
6. Jika nilai sudah berada pada rentang 0 sampai 100, perulangan berhenti.
7. Menampilkan nilai yang valid.

| Input | Keterangan                                       |
| ----- | ------------------------------------------------ |
| `120` | Ditolak karena lebih dari 100                    |
| `-5`  | Ditolak karena kurang dari 0                     |
| `75`  | Diterima karena berada pada rentang 0 sampai 100 |

Contoh proses:
Nilai 120 → tidak valid
Nilai -5  → tidak valid
Nilai 75  → valid

##Latihan 4 - Menghitung Bilangan Genap
Nama File

latihan/04_hitung_genap.py

##Tujuan
Program menerima bilangan positif n, kemudian menghitung banyak bilangan genap dari 1 sampai n.

##Konsep yang Digunakan
Program menggunakan perulangan for dan operator modulus %.

Bilangan dikatakan genap apabila:
i % 2 == 0

##Algoritma
1. Meminta pengguna memasukkan bilangan n.
2. Membuat variabel jumlah_genap dengan nilai awal 0.
3. Melakukan perulangan dari 1 sampai n.
4. Memeriksa setiap bilangan menggunakan kondisi i % 2 == 0.5. 
5. Jika kondisi benar, nilai jumlah_genap ditambah 1.
6. Setelah perulangan selesai, tampilkan jumlah bilangan genap.

| Input `n` | Keluaran yang Diharapkan |
| --------: | -----------------------: |
|       `1` |                      `0` |
|       `2` |                      `1` |
|       `5` |                      `2` |
|      `10` |                      `5` |
Contoh untuk n = 5:

Bilangan dari 1 sampai 5:
1 → ganjil
2 → genap
3 → ganjil
4 → genap
5 → ganjil

Jumlah bilangan genap = 2

##Kuis 2 - Deret Aritmetika
Nama File

kuis/kuis2_deret_aritmetika.py

##Tujuan

Program menerima:
suku pertama (a)
beda (d)
banyak suku (n)

Kemudian program menghitung suku-suku deret aritmetika dan jumlah seluruh suku.

Program menggunakan perulangan untuk menghasilkan setiap suku deret.

Konsep yang Digunakan

Program menggunakan:
float
while
validasi nilai n
perhitungan suku deret aritmetika
perhitungan jumlah deret
Rumus Suku ke-n

Suku ke-n deret aritmetika dihitung menggunakan:
Un = a + (n - 1)d

Keterangan:
Un = suku ke-n
a = suku pertama
d = beda
n = banyak suku
Rumus Jumlah Deret

Jumlah n suku deret aritmetika dapat dihitung menggunakan:
Sn = n/2 × (2a + (n - 1)d)

Keterangan:
Sn = jumlah n suku
a = suku pertama
d = beda
n = banyak suku

Algoritma Kuis

1. Membaca nilai a.
2. Membaca nilai d.
3. Membaca banyak suku n.
4. Memeriksa apakah n lebih besar dari 0.
5. Jika n tidak valid, program meminta input kembali sampai mendapatkan nilai yang valid.
6. Menentukan suku-suku deret menggunakan perulangan.
7. Menghitung setiap suku berdasarkan suku sebelumnya dan beda.
8. Menambahkan setiap suku ke dalam total.
9. Menampilkan seluruh suku deret.
10. Menampilkan jumlah seluruh suku.

##Cara Menjalankan Program

Pastikan terminal berada pada folder:
pertemuan-05-perulangan-2225250001

Menjalankan Latihan 1
python latihan/01_tabel_perkalian.py

Menjalankan Latihan 2
python latihan/02_jumlah_bilangan.py

Menjalankan Latihan 3
python latihan/03_validasi_input.py

Menjalankan Latihan 4
python latihan/04_hitung_genap.py

Menjalankan Kuis 2
python kuis/kuis2_deret_aritmetika.py

##Hasil Pengujian

Pengujian Latihan 1

Pengujian dilakukan dengan menjalankan setiap program menggunakan test case yang telah ditentukan pada soal.
| Input | Hasil yang Diharapkan               | Hasil Aktual            | Status |
| ----- | ----------------------------------- | ----------------------- | ------ |
| `4`   | Tabel perkalian 4 dari 1 sampai 10  | Sesuai keluaran program | Lulus  |
| `-3`  | Tabel perkalian -3 dari 1 sampai 10 | Sesuai keluaran program | Lulus  |

Pengujian Latihan 2
| Input | Hasil yang Diharapkan | Hasil Aktual | Status |
| ----- | --------------------: | -----------: | ------ |
| `1`   |                   `1` |          `1` | Lulus  |
| `5`   |                  `15` |         `15` | Lulus  |
| `10`  |                  `55` |         `55` | Lulus  |

Pengujian Latihan 3
| Input | Keterangan                     | Status |
| ----- | ------------------------------ | ------ |
| `120` | Ditolak karena di luar rentang | Lulus  |
| `-5`  | Ditolak karena di luar rentang | Lulus  |
| `75`  | Diterima karena valid          | Lulus  |
Program harus menolak dua input pertama dan berhenti setelah menerima nilai 75.

Pengujian Latihan 4
| Input | Hasil yang Diharapkan | Hasil Aktual | Status |
| ----- | --------------------: | -----------: | ------ |
| `1`   |                   `0` |          `0` | Lulus  |
| `2`   |                   `1` |          `1` | Lulus  |
| `5`   |                   `2` |          `2` | Lulus  |
| `10`  |                   `5` |          `5` | Lulus  |

Pengujian Kuis 2
|     a |     d |   n | Suku              | Jumlah |
| ----: | ----: | --: | ----------------- | -----: |
|   `2` |   `3` | `5` | `2, 5, 8, 11, 14` |   `40` |
|  `10` |  `-2` | `4` | `10, 8, 6, 4`     |   `28` |
| `1.5` | `0.5` | `3` | `1.5, 2.0, 2.5`   |  `6.0` |

##Refleksi
Pada pertemuan ini saya mempelajari penggunaan perulangan for dan while dalam Python.

Salah satu kesalahan yang perlu diperhatikan dalam membuat program perulangan adalah kesalahan pada batas perulangan. Kesalahan menentukan nilai awal, nilai akhir, atau kondisi perulangan dapat menyebabkan jumlah proses tidak sesuai dengan yang diharapkan.

Selain itu, pada perulangan while, kondisi harus dibuat dengan benar agar perulangan dapat berhenti ketika kondisi yang ditentukan telah terpenuhi. Jika kondisi tidak pernah berubah atau tidak pernah menjadi False, program dapat mengalami perulangan tanpa akhir.

Cara memperbaikinya adalah dengan memeriksa kembali:
1. Nilai awal variabel.
2. Kondisi perulangan.
3. Perubahan nilai variabel di dalam perulangan.
4. Batas akhir perulangan.
5. Hasil setiap test case.

Melalui latihan ini, saya menjadi lebih memahami bahwa penggunaan for cocok ketika jumlah pengulangan sudah diketahui, sedangkan while dapat digunakan ketika pengulangan bergantung pada suatu kondisi.

##Kesimpulan
Pada Pertemuan 05 telah dipelajari penggunaan perulangan pada Python melalui beberapa latihan dan kuis.

Latihan yang dikerjakan meliputi:
1. Membuat tabel perkalian.
2. Menghitung jumlah bilangan dari 1 sampai n.
3. Melakukan validasi input nilai.
4. Menghitung banyak bilangan genap.
5. Menghitung suku dan jumlah deret aritmetika pada kuis.

Dari latihan tersebut dapat dipahami bahwa perulangan membantu menjalankan instruksi yang sama secara berulang tanpa harus menuliskan instruksi tersebut berkali-kali.

Perulangan for digunakan pada proses dengan jumlah pengulangan yang dapat ditentukan, sedangkan while digunakan pada proses yang bergantung pada suatu kondisi.
