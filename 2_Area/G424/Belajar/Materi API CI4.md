1. https://www.youtube.com/watch?v=JZMBEJlcD20&t=789s

2. <iframe src="https://www.youtube.com/watch?v=vQJJ_K1JbEA&list=PLFIM0718LjIW7AsIbnhFg15t9yx4H-sQ0" width ="750px" height="400px"></iframe>
3. https://www.youtube.com/watch?v=rKVgINFyjPA&pp=ygUQY3BhbmVsIGZsYXNrIGFwcA%3D%3D
4. https://www.youtube.com/watch?v=260eDcsUheE&pp=ygUQY3BhbmVsIGZsYXNrIGFwcA%3D%3D

---
	Siap 😆 kita buat versi **rapi & formal untuk dokumentasi deployment Flask di cPanel (CloudLinux)**.  
Ini bisa langsung kamu masukkan ke laporan / dokumentasi teknis.

---

# 📘 Dokumentasi Deployment Flask pada Hosting cPanel (CloudLinux)

## 1️⃣ Persiapan Awal

### 1.1 Pastikan Hosting Mendukung Python

- Tersedia menu **Setup Python App**
    
- Versi Python minimal 3.x
    
- Mendukung Passenger (CloudLinux)
    

---

## 2️⃣ Membuat Aplikasi Python di cPanel

1. Login ke cPanel
    
2. Klik **Setup Python App**
    
3. Klik **Create Application**
    
4. Isi konfigurasi berikut:
    

|Field|Nilai|
|---|---|
|Python Version|3.x|
|Application Root|testing|
|Application URL|vidyasvatantra.my.id/testinginventaris|
|Application Startup File|passenger_wsgi.py|
|Entry Point|application|

5. Klik **Create**
    

---

## 3️⃣ Menyiapkan Struktur Folder

Masuk ke File Manager → folder `testing`

Struktur yang diperlukan:

```
testing/
│
├── app.py
├── passenger_wsgi.py
├── requirements.txt
├── Inventory.json
│
├── templates/
│     └── index.html
│
└── static/
      ├── style.css
      └── script.js
```

---

## 4️⃣ Konfigurasi File Penting

### 4.1 passenger_wsgi.py

```python
from app import app as application
```

---

### 4.2 requirements.txt

```
Flask
```

---

### 4.3 Konfigurasi Path JSON di app.py

Untuk menghindari error path di hosting, gunakan:

```python
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(BASE_DIR, "Inventory.json")
```

---

### 4.4 Isi Awal Inventory.json

Agar tidak terjadi JSONDecodeError:

```
[]
```

---

## 5️⃣ Penyesuaian Path API pada JavaScript

Karena aplikasi berjalan di subfolder, endpoint API tidak boleh menggunakan slash di depan.

❌ Salah:

```javascript
fetch("/api/inventory")
```

✅ Benar:

```javascript
fetch("api/inventory")
```

Penyesuaian ini dilakukan pada seluruh endpoint fetch.

---

## 6️⃣ Instalasi Dependency

1. Masuk kembali ke **Setup Python App**
    
2. Klik **Run Pip Install**
    
3. Setelah selesai, klik **Restart Application**
    

---

## 7️⃣ Pengujian Sistem

1. Akses URL aplikasi:
    
    ```
    https://vidyasvatantra.my.id/testinginventaris
    ```
    
2. Tambahkan data inventaris
    
3. Periksa apakah file `Inventory.json` terbuat otomatis
    
4. Pastikan data tampil pada tabel
    

---

## 8️⃣ Troubleshooting Umum

|Masalah|Penyebab|Solusi|
|---|---|---|
|500 Error|Startup file salah|Periksa passenger_wsgi.py|
|JSONDecodeError|File JSON kosong|Isi dengan []|
|Data tidak muncul|Path fetch salah|Gunakan relative path|
|Permission denied|Hak akses folder|Ubah ke 755 / 775|

---

# ✅ Status Akhir Deployment

Jika seluruh langkah berhasil dilakukan, maka:

- Aplikasi Flask berjalan di shared hosting
    
- API berfungsi normal
    
- File JSON dapat dibaca dan ditulis
    
- Static file termuat dengan benar
    

---

Kalau mau, aku bisa buatkan versi **lebih akademik (format laporan skripsi / TA)** juga 😏