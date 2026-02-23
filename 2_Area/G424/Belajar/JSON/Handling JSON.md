### Handling JSON pada PHP

#### 1. Peran JSON dalam PHP

Dalam PHP, JSON umum digunakan untuk:

- Pertukaran data antara **frontend (JavaScript)** dan **backend (PHP)**
- Format respons pada **REST API**
- Penyimpanan data terstruktur sederhana
- Komunikasi antar sistem berbasis web
    

PHP menyediakan ekstensi bawaan (`json`) sehingga pengolahan JSON dapat dilakukan tanpa pustaka tambahan.


#### 2. Encoding Data ke JSON (PHP → JSON)

Untuk mengubah data PHP menjadi JSON digunakan fungsi `json_encode()`.

#### Contoh:

`$data = [     "nama" => "Najwa",     "role" => "admin",     "aktif" => true ];  $json = json_encode($data); echo $json;`

**Output:**

`{"nama":"Najwa","role":"admin","aktif":true}`

#### Catatan Penting:

- Tipe data PHP otomatis dikonversi ke tipe JSON
- Gunakan `JSON_PRETTY_PRINT` agar lebih mudah dibaca

`echo json_encode($data, JSON_PRETTY_PRINT);`

---

### 3. Decoding JSON ke PHP (JSON → PHP)

Untuk membaca JSON digunakan fungsi `json_decode()`.

#### Decode ke Object (default):

`$json = '{"nama":"Najwa","role":"admin"}'; $obj = json_decode($json);  echo $obj->nama;`

#### Decode ke Array:

`$arr = json_decode($json, true); echo $arr['nama'];`

📌 **Best practice**: Gunakan array (`true`) untuk kemudahan manipulasi data.


#### 4. Handling JSON pada Request API (Input)

Pada API berbasis PHP, data JSON biasanya dikirim melalui **HTTP Body**.

`$input = file_get_contents("php://input"); $data  = json_decode($input, true);`

Contoh payload:

`{   "email": "user@mail.com",   "password": "secret" }`

#### 5. Mengirim Response JSON dari PHP

Gunakan header `Content-Type: application/json`.

`header("Content-Type: application/json");  $response = [     "status" => "success",     "message" => "Data berhasil diproses" ];  echo json_encode($response);`

📌 **Wajib** untuk API agar klien tahu format data.


### 6. Validasi & Error Handling JSON

Cek kesalahan decoding menggunakan `json_last_error()`.

`$data = json_decode($input, true);  if (json_last_error() !== JSON_ERROR_NONE) {     echo json_encode([         "status" => "error",         "message" => "Format JSON tidak valid"     ]);     exit; }`

---

### 7. JSON dan Database (Best Practice)

❌ Jangan simpan JSON mentah jika datanya sering difilter  
✅ Simpan JSON hanya untuk:

- Konfigurasi
- Log
- Metadata fleksibel

Jika pakai MySQL:

`CREATE TABLE log_api (     id INT AUTO_INCREMENT,     payload JSON,     PRIMARY KEY (id) );`


### 8. Keamanan Handling JSON di PHP

- Selalu **validasi input**
- Jangan percaya isi JSON dari klien
- Hindari `eval()` (❌)
- Sanitasi sebelum query database


### 9. Integrasi dengan Framework (CI4)

Di **CodeIgniter 4**:

`$data = $this->request->getJSON(true); return $this->response->setJSON($data);`

CI4 otomatis menangani header & parsing JSON 👌