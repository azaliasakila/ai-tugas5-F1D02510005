# Sistem Pakar Diagnosis Gangguan WiFi dan Internet

## 1. Identitas

- **Nama:** Azalia Sakila
- **NIM:** F1D02510005

## 2. Topik dan Cara Menjalankan Program

### Topik
Program ini merupakan sistem pakar sederhana untuk mendiagnosis penyebab gangguan WiFi dan internet berdasarkan jawaban pengguna terhadap beberapa pertanyaan. Sistem menggunakan metode **Forward Chaining** untuk mencocokkan fakta yang diberikan pengguna dengan aturan yang tersedia dalam knowledge base.

### Teknologi yang Digunakan
- Bahasa pemrograman: Python
- Versi: Python 3.x
- Basis pengetahuan: JSON (`kb_wifi.json`)
- Library: `json` (bawaan Python)

### Cara Menjalankan Program

Pastikan Python sudah terinstal pada komputer. Letakkan file `main.py` dan `kb_wifi.json` dalam satu folder.

Buka terminal pada folder tersebut, kemudian jalankan perintah:

```bash
python main.py
```

Program akan menampilkan sembilan pertanyaan diagnosis. Pengguna menjawab setiap pertanyaan menggunakan:
- `y` untuk Ya.
- `n` untuk Tidak.

Setelah seluruh pertanyaan dijawab, program akan mencocokkan fakta dengan aturan dan menampilkan hasil diagnosis beserta referensinya.

## 3. Daftar Sumber dan Tabel Aturan

### Daftar Sumber

| Kode | Judul dan Penerbit | URL | Tanggal Akses |
|---|---|---|---|
| S1 | Fix Wi-Fi Connection Issues in Windows – Microsoft Support | https://support.microsoft.com/id-id/windows/experience/connectivity-networking/fix-wi-fi-connection-issues-in-windows | 5 November 2026 |
| S2 | Troubleshoot Wireless Speed Issues – Cisco | https://www.cisco.com/c/en/us/support/docs/wireless/wireless-lan-controller-software/220877-troubleshoot-wireless-speed-issues.html | 5 November 2026 |

### Tabel Aturan (Rule Base)

| Aturan | Kondisi (IF) | Hasil (THEN) | Sumber |
|---|---|---|---|
| R1 | WiFi tidak aktif | Gangguan pada perangkat pengguna | S1 |
| R2 | WiFi aktif DAN nama jaringan tidak terlihat | Gangguan pada router atau jaringan WiFi | S1 |
| R3 | Perangkat terhubung DAN internet tidak dapat diakses DAN perangkat lain juga mengalami gangguan | Gangguan pada jaringan internet, modem, atau ISP | S1 |
| R4 | Perangkat terhubung DAN internet tidak dapat diakses DAN perangkat lain tidak mengalami gangguan | Gangguan pada perangkat pengguna | S1 |
| R5 | Sinyal WiFi lemah DAN koneksi membaik ketika perangkat didekatkan ke router | Gangguan pada jangkauan sinyal WiFi | S2 |

## 4. Metode yang Digunakan

Metode yang digunakan adalah **Forward Chaining (Pelacakan ke Depan)**.

Forward Chaining merupakan metode penalaran yang dimulai dari fakta atau informasi yang diberikan pengguna, kemudian mencocokkannya dengan aturan yang terdapat dalam basis pengetahuan untuk memperoleh kesimpulan.

### Alasan Pemilihan Metode

Metode Forward Chaining dipilih karena proses diagnosis dimulai dari kondisi yang dialami pengguna. Jawaban pengguna akan dikumpulkan sebagai fakta, kemudian sistem memeriksa aturan yang sesuai hingga menghasilkan diagnosis.

### Langkah Kerja

1. Sistem membaca basis pengetahuan dari file `kb_wifi.json`.
2. Pengguna menjawab sembilan pertanyaan diagnosis.
3. Jawaban Ya (`y`) disimpan sebagai fakta.
4. Sistem memeriksa setiap aturan dalam knowledge base.
5. Sistem menggunakan fungsi `all()` untuk memeriksa apakah seluruh kondisi aturan terpenuhi karena aturan menggunakan operator AND.
6. Jika kondisi terpenuhi, sistem menampilkan aturan yang aktif, hasil diagnosis, dan referensi sumber.
7. Jika tidak ada aturan yang sesuai, sistem menampilkan pesan bahwa diagnosis belum ditemukan.

### Perhitungan Manual

Contoh pengujian aturan R3:

**Fakta yang diberikan pengguna:**
- Perangkat terhubung = Ya.
- Internet tidak dapat diakses = Ya.
- Perangkat lain juga mengalami gangguan = Ya.

Aturan R3:

IF (Perangkat terhubung) AND (Internet tidak dapat diakses) AND (Perangkat lain juga mengalami gangguan)

THEN Gangguan pada jaringan internet, modem, atau ISP.

Perhitungan:

- Kondisi 1 = True
- Kondisi 2 = True
- Kondisi 3 = True

Maka:

`True AND True AND True = True`

Karena seluruh kondisi terpenuhi, aturan R3 aktif dan sistem menghasilkan diagnosis berupa gangguan pada jaringan internet, modem, atau ISP.

## 5. Pengujian Program

Pengujian dilakukan menggunakan tiga kasus untuk memastikan sistem dapat menghasilkan diagnosis berdasarkan aturan yang tersedia.

### Kasus 1: WiFi Tidak Aktif

**Input:**
- WiFi tidak aktif = Ya.
- Kondisi lainnya = Tidak.

**Hasil yang diharapkan:**

Aturan R1 aktif.

Diagnosis: Gangguan pada perangkat pengguna.

**Screenshot:**

[Masukkan screenshot hasil pengujian kasus 1 di sini]

### Kasus 2: Nama Jaringan Tidak Terlihat

**Input:**
- WiFi aktif = Ya.
- Nama jaringan tidak terlihat = Ya.
- Kondisi lainnya = Tidak.

**Hasil yang diharapkan:**

Aturan R2 aktif.

Diagnosis: Gangguan pada router atau jaringan WiFi.

**Screenshot:**

[Masukkan screenshot hasil pengujian kasus 2 di sini]

### Kasus 3: Gangguan Internet pada Beberapa Perangkat

**Input:**
- Perangkat terhubung = Ya.
- Internet tidak dapat diakses = Ya.
- Perangkat lain juga mengalami gangguan = Ya.
- Kondisi lainnya = Tidak.

**Hasil yang diharapkan:**

Aturan R3 aktif.

Diagnosis: Gangguan pada jaringan internet, modem, atau ISP.

**Screenshot:**

[Masukkan screenshot hasil pengujian kasus 3 di sini]

## 6. Batas Keberlakuan Sistem

Sistem pakar ini menggunakan pengetahuan yang bersumber dari dokumentasi resmi Microsoft Support dan Cisco. Diagnosis yang diberikan hanya mencakup kondisi WiFi tidak aktif, nama jaringan tidak terlihat, kegagalan koneksi, gangguan akses internet, gangguan pada perangkat lain, dan sinyal WiFi lemah. Sistem ditujukan sebagai alat bantu diagnosis awal berdasarkan jawaban pengguna, bukan untuk menggantikan pemeriksaan teknis secara langsung atau menjadi keputusan akhir dalam menentukan penyebab gangguan.

## 7. Penggunaan Alat Bantu AI

Dalam pengerjaan tugas ini, alat bantu AI (ChatGPT) digunakan untuk membantu penyusunan dokumentasi README dan penjelasan struktur dokumentasi program. Implementasi kode program, basis pengetahuan, serta aturan diagnosis disesuaikan dengan program yang digunakan dalam tugas ini.
