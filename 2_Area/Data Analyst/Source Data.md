Q : Jika membaca file.xlsx lewat python untuk menjadi file JSON gimana ? Perjelas Format Colomn nya agar aku paham

A : 
Oke 👍 kita bahas **alur lengkapnya** supaya kamu benar-benar paham struktur kolomnya.

Tujuan:

> File `.xlsx` ➜ dibaca Python ➜ dikonversi menjadi file `.json`

Kita pakai `pandas`.

---

# 1️⃣ Install Library

```bash
pip install pandas openpyxl
```

---

# 2️⃣ Contoh Struktur Excel

Misalnya isi file `data.xlsx` seperti ini:

|id|nama|umur|jurusan|
|---|---|---|---|
|1|Ahmad|21|Informatika|
|2|Siti|22|Sistem Informasi|
|3|Budi|20|Teknik Komputer|

👉 **Baris pertama = Nama Kolom**  
👉 Baris berikutnya = Data

---

# 3️⃣ Cara Membaca dan Mengubah ke JSON

```python
import pandas as pd

# Baca file Excel
df = pd.read_excel("data.xlsx", engine="openpyxl")

# Konversi ke JSON format list of object
df.to_json("data.json", orient="records", indent=4)

print("Berhasil convert ke JSON!")
```

---

# 4️⃣ Hasil JSON (orient="records")

Output `data.json` akan seperti ini:

```json
[
    {
        "id": 1,
        "nama": "Ahmad",
        "umur": 21,
        "jurusan": "Informatika"
    },
    {
        "id": 2,
        "nama": "Siti",
        "umur": 22,
        "jurusan": "Sistem Informasi"
    },
    {
        "id": 3,
        "nama": "Budi",
        "umur": 20,
        "jurusan": "Teknik Komputer"
    }
]
```

---

# 📌 Penjelasan Format Kolom

Dalam pandas:

|Excel|Menjadi di JSON|
|---|---|
|Nama Kolom (Header)|Key JSON|
|Isi Baris|Value JSON|
|Setiap Baris|1 Object JSON|
|Semua Baris|List / Array|

Jadi secara struktur:

```text
Excel Table
   ↓
DataFrame (pandas)
   ↓
List of Dictionary
   ↓
JSON
```

---

# 5️⃣ Jika Ingin Format JSON Berbeda

## A. Format Index (Jarang Dipakai API)

```python
df.to_json("data.json", orient="index", indent=4)
```

Hasil:

```json
{
    "0": {"id":1,"nama":"Ahmad","umur":21,"jurusan":"Informatika"},
    "1": {"id":2,"nama":"Siti","umur":22,"jurusan":"Sistem Informasi"}
}
```

---

## B. Format Column-Oriented

```python
df.to_json("data.json", orient="columns", indent=4)
```

Hasil:

```json
{
    "id": {"0":1,"1":2,"2":3},
    "nama": {"0":"Ahmad","1":"Siti","2":"Budi"},
    "umur": {"0":21,"1":22,"2":20}
}
```

---

# 🎯 Format yang Paling Umum

Gunakan:

```python
orient="records"
```

Karena:

- Cocok untuk API
    
- Cocok untuk database
    
- Mudah diproses di JavaScript
    
- Format paling standar
    

---

# 6️⃣ Jika Excel Punya Banyak Sheet

```python
data = pd.read_excel("data.xlsx", sheet_name=None)

for nama_sheet, df in data.items():
    df.to_json(f"{nama_sheet}.json", orient="records", indent=4)
```

---

# ⚠️ Perlu Kamu Tahu

Jika Excel:

- Ada kolom kosong → akan jadi `null`
    
- Ada tanggal → akan jadi format timestamp (bisa diatur)
    
- Ada angka besar → bisa berubah tipe (int jadi float)
    

---

# 🔎 Supaya Kamu Lebih Paham Lagi

Sebenarnya pandas melakukan ini:

```python
df.to_dict(orient="records")
```

Hasilnya:

```python
[
  {'id':1, 'nama':'Ahmad', 'umur':21, 'jurusan':'Informatika'},
  ...
]
```

Baru kemudian disimpan menjadi JSON.

---

Kalau mau, saya bisa jelaskan juga:

- 🔥 Cara mapping kolom Excel ke struktur JSON custom
    
- 🔥 Cara nested JSON (misalnya jurusan jadi objek)
    
- 🔥 Cara validasi kolom sebelum convert
    
- 🔥 Cara handle file besar (ribuan baris)
    
