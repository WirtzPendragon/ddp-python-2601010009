## Trace Table Dasar-Dasar Pemrograman: Pertemuan 6

## Daftar latihan
1. latihan1_biodata.py: menampilkan biodata dengan f-string
2. latihan2_persegi_panjang.py: menghitung luas dan keliling
3. latihan3_konversi_suhu.py: konversi Celsius ke Fahrenheit dan Kelvin
4. latihan4_total_belanja.py: menghitung total belanja dengan PPN 11%


## Panduan Membaca Simbol Trace Table
1. Tanda Strip (-) pada Nilai Awal: Variabel belum dibuat atau belum dialokasikan di memori sebelum baris tersebut berjalan.
2. Tanda Strip (-) pada Baris print	Baris tersebut hanya melakukan aksi output ke layar, tidak membuat/mengubah variabel baru.
3. Operator *, /, +	Simbol komputasi berturut-turut untuk perkalian (*), pembagian (/), dan penjumlahan (+).
4. Tanda Kurung ( )	Menandakan operasi matematika di dalamnya wajib dihitung terlebih dahulu.

## Latihan 1 Biodata

------------------------------------------------------------------------------------------------------
Baris | Variabel | Tipe Data | Nilai Awal | Nilai Akhir                    | Keterangan
------------------------------------------------------------------------------------------------------
 2    | nama     | string    | -          | "Made Suastika Aditya Wiranata"| Inisialisasi nama
 4    | nim      | string    | -          | "2601010009"                   | Inisialisasi NIM
 6    | prodi    | string    | -          | "Sistem Informasi"             | Inisialisasi prodi
 8    | hobi     | string    | -          | "Gaming tipis tipis"           | Inisialisasi hobi
 11   | -        | -         | -          | -                              | Mencetak teks biodata
------------------------------------------------------------------------------------------------------
Trace table membuktikan program sukses menyimpan data teks (string) identitas mahasiswa ke dalam memori secara berurutan. Semua data tersebut kemudian berhasil dipanggil dan ditampilkan ke layar dengan rapi menggunakan metode f-string.

## Latihan 2 Menghitung  Luas dan Keliling Persegi Panjang

(Contoh Kasus: Panjang = 5.0, Lebar = 3.0)
---------------------------------------------------------------------------
Baris | Variabel  | Tipe Data | Nilai Awal | Nilai Akhir | Keterangan
---------------------------------------------------------------------------
 4    | panjang   | float     | -          | 5.0         | Input user
 5    | lebar     | float     | -          | 3.0         | Input user
 8    | luas      | float     | -          | 15.0        | 5.0 * 3.0
 9    | keliling  | float     | -          | 16.0        | 2 * (5.0 + 3.0)
 12   | -         | -         | -          | -           | Mencetak output
---------------------------------------------------------------------------
Penelusuran menunjukkan alur perhitungan rumus matematika pada program sudah berjalan dengan valid dan akurat. Menggunakan contoh input desimal (float), program berhasil menghasilkan nilai luas 15.0 dan keliling 16.0 tanpa error.


## Latihan 3 Menghitung  Konversi Suhu Celcius ke Fahrenheit & Kelvin

(Contoh Kasus: Celcius = 25.0)
------------------------------------------------------------------------------
Baris | Variabel   | Tipe Data | Nilai Awal | Nilai Akhir | Keterangan
------------------------------------------------------------------------------
 4    | celcius    | float     | -          | 25.0        | Input user
 7    | fahrenheit | float     | -          | 77.0        | (25.0 * 9/5) + 32
 8    | kelvin     | float     | -          | 298.15      | 25.0 + 273.15
 11   | -          | -         | -          | -           | Mencetak hasil
------------------------------------------------------------------------------
Trace table mengonfirmasi bahwa rumus konversi suhu berbasis input desimal (float) sudah bekerja sesuai aturan fisika. Nilai input Celsius (25.0) berhasil diubah secara akurat menjadi 77.0°F dan 298.15°K sebelum dicetak.


## Latihan 4 Menghitung Total Belanja dengan PPN 11%

(Contoh Kasus: Buku, Harga = 50000.0, Jumlah = 2)
------------------------------------------------------------------------------------
Baris | Variabel      | Tipe Data | Nilai Awal | Nilai Akhir | Keterangan
------------------------------------------------------------------------------------
 4    | nama_barang   | string    | -          | "Buku"      | Input user
 5    | harga_satuan  | float     | -          | 50000.0     | Input user
 6    | jumlah_barang | integer   | -          | 2           | Input user
 9    | subtotal      | float     | -          | 100000.0    | 50000.0 * 2
 10   | ppn           | float     | -          | 110000.0    | 100000.0 * 0.11
 11   | total_belanja | float     | -          | 111000.0    | 100000.0 + 11000.0
 14   | -             | -         | -          | -           | Mencetak rincian
------------------------------------------------------------------------------------
Tabel pelacakan membuktikan bahwa proses perhitungan berantai yang melibatkan tipe data campuran (string, float, integer) berjalan tepat. Program sukses menghitung subtotal belanja, mengakumulasikan tarif PPN 11%, dan menghasilkan total bayar akhir yang benar.