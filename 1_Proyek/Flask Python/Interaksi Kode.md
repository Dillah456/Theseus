
Kita akan bahas:
1. 📁 `app.py` (Backend / API Layer)
2. 🌐 `index.html` (Frontend Structure)
3. ⚙️ `script.js` (Client Logic / Interaksi API)
4. 🔄 Interaksi antar file (Full Flow Lifecycle)

---

# 🧠 1️⃣ app.py → Otak Sistem (Backend API)

Sumber:

File ini adalah **Flask server + REST API + data persistence layer**.

---

## 🔹 A. Inisialisasi

```python
app = Flask(__name__)
FILE = "Inventory.json"
```

- `app` = aplikasi Flask
    
- `FILE` = tempat penyimpanan data (JSON file sebagai database sederhana)
    

Jadi kamu tidak pakai DBMS, tapi **file-based persistence**.

---

## 🔹 B. load_inventory()

```python
def load_inventory():
```

Fungsi ini:

- Mengecek apakah file ada
    
- Kalau tidak ada → return list kosong
    
- Kalau ada → baca JSON → return sebagai list Python
    

Artinya:  
👉 File JSON dianggap sebagai array of object

---

## 🔹 C. save_inventory(data)

```python
def save_inventory(data):
```

Fungsi ini:

- Menulis ulang seluruh file JSON
    
- Menggunakan indent=2 supaya readable
    

Ini artinya sistem kamu menggunakan pendekatan:

> Overwrite whole dataset setiap perubahan

Untuk skala kecil: aman  
Untuk skala besar: perlu database.

---

## 🔹 D. Route: "/"

```python
@app.route("/")
def index():
    return render_template("index.html")
```

Ini:

- Menampilkan halaman utama
    
- Tidak ada logika data
    
- Hanya serve HTML
    

---

## 🔹 E. API Endpoints

### 📥 GET Inventory

```python
@app.route("/api/inventory", methods=["GET"])
```

Mengembalikan seluruh inventory dalam bentuk JSON.

---

### 📤 POST Save All

```python
@app.route("/api/inventory", methods=["POST"])
```

Menyimpan seluruh inventory sekaligus.

---

### ➕ Add Item

```python
@app.route("/api/inventory/add", methods=["POST"])
```

Flow:

1. Load inventory
    
2. Tambah item
    
3. Save ulang
    
4. Return status
    

---

### 🔄 Update Quantity

```python
@app.route("/api/inventory/update", methods=["POST"])
```

Loop mencari item berdasarkan Id  
Kalau cocok → update Quantity

---

### ❌ Delete Item

```python
@app.route("/api/inventory/delete", methods=["POST"])
```

Menggunakan list comprehension untuk:

- Membuat list baru tanpa item tertentu
    

---

# 🌐 2️⃣ index.html → Struktur UI

Sumber:

File ini adalah:

> Template tampilan statis

Flask hanya mengirimkan ini tanpa data awal.

---

## 🔹 Struktur Utama

### 📦 Form Input

```html
<form id="inventoryForm">
```

Input field:

- Item_Name
    
- Quantity
    
- No_Rak
    
- No_Gudang
    
- Jenis
    
- Keterangan
    

Ini adalah input layer.

---

### 📊 Table

```html
<tbody id="tableBody"></tbody>
```

Kosong saat load.

Isi tabel akan dibuat oleh JavaScript.

---

### ⚙️ Script

```html
<script src="/static/script.js"></script>
```

Artinya:

- Semua interaksi dinamis dikontrol JS
    
- HTML hanya struktur
    

---

# ⚙️ 3️⃣ script.js → Otak Frontend

Sumber:

File ini:

> Menghubungkan UI dengan API Flask

Menggunakan `fetch()` untuk komunikasi HTTP.

---

## 🔹 A. loadInventory()

```javascript
const res = await fetch("/api/inventory");
```

Ini:

- Request GET ke backend
    
- Ambil JSON
    
- Render ke tabel
    

---

## 🔹 B. render(data)

Loop data:

```javascript
data.forEach(item => {
```

Membuat `<tr>` secara dinamis.

Di sini penting:  
Tombol aksi memanggil:

```javascript
updateQty()
deleteItem()
```

Berarti:  
Frontend tidak reload page  
Semua AJAX-based.

---

## 🔹 C. updateQty()

```javascript
await fetch("/api/inventory/update", { method: "POST" })
```

Setelah update:

```javascript
loadInventory();
```

Artinya:  
Refresh data ulang dari server.

---

## 🔹 D. deleteItem()

Mirip update:

- POST
    
- Refresh data
    

---

## 🔹 E. Form Submit

```javascript
document.getElementById("inventoryForm").onsubmit
```

Saat submit:

1. Cegah reload page
    
2. Buat object item
    
3. POST ke `/api/inventory/add`
    
4. Reset form
    
5. Reload inventory
    

---

# 🔄 4️⃣ Interaksi Antar File (Full Flow)

Sekarang kita lihat sistem secara menyeluruh.

---

## 🚀 Saat Browser Dibuka

```text
User → GET /
```

Flask:  
→ return index.html

Browser:  
→ load script.js

script.js:  
→ langsung jalankan loadInventory()

---

## 📦 Saat loadInventory()

```text
Browser → GET /api/inventory
```

Flask:  
→ load_inventory()  
→ return JSON

JS:  
→ render()

---

## ➕ Saat Tambah Item

```text
User Submit Form
↓
JS POST /api/inventory/add
↓
Flask add_item()
↓
save_inventory()
↓
Return JSON
↓
JS loadInventory()
```

---

## 🔄 Saat Update Quantity

```text
Click ➕ / ➖
↓
JS POST /api/inventory/update
↓
Flask update_qty()
↓
save_inventory()
↓
JS reload table
```

---

## ❌ Saat Delete

```text
Click ❌
↓
JS POST /api/inventory/delete
↓
Flask delete_item()
↓
save_inventory()
↓
Reload
```

---

# 🏗️ Arsitektur Sistem Kamu

Secara arsitektur:

```text
Frontend (HTML + JS)
        ↓
REST API (Flask)
        ↓
JSON File Storage
```

Ini disebut:

> Single Page Application (mini version) + REST backend

---

# 📊 Karakter Sistem Ini

✔ Stateless request  
✔ REST-style endpoint  
✔ File-based persistence  
✔ AJAX interaction  
✔ Client-side rendering

---

# ⚠️ Kelemahan Saat Skala Besar

Kalau jumlah user banyak:

- JSON overwrite bisa konflik
    
- Tidak ada concurrency control
    
- Tidak ada validation
    
- Tidak ada auth
    

---

# 🧠 Secara Sistemik

Kita bisa gambarkan:

```text
UI Event → JS Function → HTTP Request → Flask Route → File I/O → JSON Response → UI Update
```

Kamu sudah membangun:

- Full CRUD
    
- REST API
    
- Client-server architecture
    

Dan itu bukan level dasar lagi 🔥

---

Kalau kamu mau, kita bisa lanjut ke:

- 🏗️ Refactor ke arsitektur modular (Blueprint)
    
- 🔐 Tambahkan authentication
    
- 🗄️ Ganti JSON jadi SQLite
    
- ⚡ Tambahkan caching
    
- 📈 Tambahkan analytics (tracking stok keluar-masuk)
    

Kamu mau sistem ini naik kelas ke arah mana?