# Bab 2 — Arsitektur Server & Aksesibilitas Data

Pada fase ini, sistem dijalankan menggunakan **Node.js HTTP server native** tanpa framework dan tanpa pemisahan eksplisit antara _public_ dan _private_. Seluruh struktur proyek—termasuk `PARA`, `REAP`, dan file di root—dipetakan langsung sebagai sumber HTTP.

Pendekatan ini menjadikan server bukan sekadar web server, tetapi **interface baca terhadap struktur pengetahuan**.

## 2.1 Prinsip Kerja Server

Konfigurasi server menggunakan root berbasis direktori proyek:

- URL dipetakan langsung ke struktur folder
    
- Tidak ada pembatasan akses berbasis folder
    
- Browser berperan sebagai klien pembaca file
    

Dengan demikian, sistem bekerja menyerupai _static knowledge server_ berbasis filesystem.

## 2.2 Relasi dengan PARA & REAP

Kondisi ini konsisten dengan filosofi PARA dan REAP:

- **PARA** → domain kerja, proyek, dan arsip aktif
    
- **REAP** → domain baca, refleksi, dan integrasi pengetahuan
    

Keduanya berorientasi _akses dan keterhubungan_, bukan keamanan.

## 2.3 Alasan Tidak Memisahkan Public & Private

Pada fase eksplorasi dan pembentukan struktur:

- Pembatasan akses justru menghambat iterasi
    
- Konsistensi navigasi lebih penting daripada proteksi
    
- Boundary lebih efektif diterapkan setelah pola stabil
    

Maka, absennya konsep _public/private_ adalah keputusan desain, bukan kekurangan teknis.

---

# 🔹 Bab 3 — Navigasi, Path, dan Modularitas Sistem

Bab ini membahas bagaimana sistem tetap **portabel, konsisten, dan mudah dikembangkan** tanpa framework.

## 3.1 Root-Relative Path sebagai Standar

Untuk menghindari masalah perbedaan domain (`localhost`, IP LAN, domain lokal), digunakan **root-relative path**:

`<a href="/PARA/4_Archive/Informal/">Kembali</a> <iframe src="/REAP/Read/Viewer.html"></iframe>`

Keuntungannya:

- Tidak perlu hardcode domain
    
- Jalan di laptop maupun HP
    
- Konsisten di LAN maupun lokal
    

## 3.2 Navigasi Lintas PARA dan REAP

PARA dan REAP diperlakukan sebagai **namespace logis**, bukan folder terisolasi.

Artinya:

- Project boleh mengakses Archive
    
- Read boleh menarik asset dari Area
    

Selama path absolut digunakan, dependensi tetap stabil.

## 3.3 Modularitas Tanpa Framework

Modularitas dicapai lewat **konvensi**, bukan bundler:

- HTML → struktur
- JS → logika
- Folder → konteks

Contoh:

`<script src="/PARA/_shared/navigation.js"></script>`

Perubahan navigasi cukup dilakukan di satu file.

## 3.4 Perilaku Asset Non-HTML

Karena server bersifat statis:

- `.pdf`, `.xlsx`, `.docx` cenderung di-download
- Ini adalah perilaku default browser, bukan error server

Preview memerlukan viewer khusus atau pengaturan MIME lanjutan.

## 3.5 Penutup Bab 3

Pada tahap ini, sistem telah:

- Mandiri tanpa framework
- Konsisten lintas perangkat
- Siap dikembangkan ke public/private **tanpa refactor besar**