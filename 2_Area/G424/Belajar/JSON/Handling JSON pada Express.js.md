## 

### 1. Peran JSON di Express.js

Express.js (berbasis Node.js) menggunakan JSON sebagai **format utama** untuk:

- Request body dari client (frontend / mobile)
    
- Response API
    
- Komunikasi antar service (microservices)
    
- Integrasi dengan database & pihak ketiga
    

Berbeda dengan PHP yang bersifat _request–response blocking_, Express.js bersifat **event-driven & non-blocking**, sehingga handling JSON lebih efisien untuk beban tinggi.

---

### 2. Parsing JSON (Middleware Wajib)

Express **tidak otomatis membaca JSON** tanpa middleware.

`const express = require('express'); const app = express();  app.use(express.json()); // wajib`

📌 Tanpa `express.json()`, `req.body` akan `undefined`.

---

### 3. Menerima JSON dari Client (Request Body)

Contoh request:

`{   "username": "najwa",   "role": "admin" }`

Handling di Express:

`app.post('/user', (req, res) => {   const data = req.body;    res.json({     status: 'success',     data: data   }); });`

📌 `req.body` sudah berbentuk **object JavaScript**, bukan string.

---

### 4. Mengirim Response JSON

Gunakan `res.json()` (disarankan):

`res.json({   status: true,   message: 'Data berhasil disimpan' });`

Keuntungan `res.json()`:

- Otomatis set header `Content-Type: application/json`
    
- Otomatis stringify object
    

---

### 5. Handling JSON dari Query & Params

#### Query String:

`GET /user?role=admin`

`app.get('/user', (req, res) => {   const role = req.query.role;   res.json({ role }); });`

#### URL Params:

`GET /user/10`

`app.get('/user/:id', (req, res) => {   res.json({ id: req.params.id }); });`

---

### 6. Validasi Data JSON (Best Practice)

Gunakan validasi manual atau library.

#### Manual:

`if (!req.body.username) {   return res.status(400).json({     error: 'username wajib diisi'   }); }`

#### Dengan Validator (contoh `express-validator`):

`const { body, validationResult } = require('express-validator');  app.post('/user',   body('username').notEmpty(),   (req, res) => {     const errors = validationResult(req);     if (!errors.isEmpty()) {       return res.status(422).json(errors.array());     }     res.json({ status: 'ok' }); });`

---

### 7. Error Handling JSON Global

Middleware error handler:

`app.use((err, req, res, next) => {   res.status(500).json({     status: 'error',     message: err.message   }); });`

📌 Error tetap dikirim dalam format JSON → konsisten untuk API.

---

### 8. Handling JSON Besar (Limit Payload)

Secara default:

`app.use(express.json({ limit: '1mb' }));`

Jika data besar (mis. IoT / bulk data):

`app.use(express.json({ limit: '10mb' }));`

---

### 9. JSON & Security di Express.js

Best practice:

- Batasi ukuran JSON
    
- Validasi semua field
    
- Gunakan `helmet`
    
- Jangan kirim stack trace ke client
    

`res.status(500).json({   error: 'Internal Server Error' });`

---

### 10. JSON dalam Arsitektur REST & Microservices

Di Express.js:

- JSON = kontrak data (API contract)
    
- Struktur harus **konsisten**
    
- Gunakan versioning API:
    

`/api/v1/users`

📌 JSON yang rapi = API yang mudah dipelihara.

---

### Ringkasan Singkat

|Aspek|Express.js|
|---|---|
|Parsing|`express.json()`|
|Input|`req.body`|
|Output|`res.json()`|
|Error|JSON response|
|Cocok untuk|REST API, Microservices|