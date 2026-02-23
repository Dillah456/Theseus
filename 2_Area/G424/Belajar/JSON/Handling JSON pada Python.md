## 

### 1. Peran JSON dalam Ekosistem Python

Di Python, JSON digunakan untuk:

- Pertukaran data antar aplikasi
- REST API & microservices
- Konfigurasi aplikasi
- Data interchange dengan JavaScript, IoT, dan sistem lain

Python punya dukungan JSON **built-in**, jadi sangat kuat tanpa dependensi tambahan.

---

## A. JSON di Python Murni (Standard Library)

### 2. Modul `json`

Python menyediakan modul `json` secara bawaan.

`import json`

---

### 3. Encoding (Python → JSON)

Mengubah object Python menjadi JSON string:

`data = {     "nama": "Najwa",     "aktif": True,     "level": 3 }  json_str = json.dumps(data) print(json_str)`

Output:

`{"nama": "Najwa", "aktif": true, "level": 3}`

#### Pretty Print:

`print(json.dumps(data, indent=2))`

---

### 4. Decoding (JSON → Python)

`json_str = '{"nama": "Najwa", "aktif": true}' data = json.loads(json_str)  print(data["nama"])`

📌 JSON object → `dict`, JSON array → `list`

---

### 5. JSON & File Handling

#### Simpan ke file:

`with open("data.json", "w") as f:     json.dump(data, f, indent=2)`

#### Baca dari file:

`with open("data.json", "r") as f:     data = json.load(f)`

---

### 6. Error Handling JSON

`try:     data = json.loads(json_str) except json.JSONDecodeError:     print("Format JSON tidak valid")`

---

## B. JSON di Flask (Web Framework Ringan)

### 7. Parsing JSON Request (Flask)

`from flask import Flask, request, jsonify  app = Flask(__name__)  @app.route('/user', methods=['POST']) def user():     data = request.get_json()     return jsonify(data)`

📌 Flask otomatis parse JSON jika `Content-Type: application/json`.

---

### 8. Response JSON di Flask

`return jsonify({     "status": "success",     "message": "Data diterima" })`

Keuntungan `jsonify()`:

- Set header JSON otomatis
    
- Cegah error encoding
    

---

### 9. Validasi JSON di Flask

`data = request.get_json()  if not data or "username" not in data:     return jsonify({"error": "username wajib"}), 400`

---

## C. JSON di FastAPI (Modern & High Performance)

### 10. Kenapa FastAPI?

FastAPI:

- Native JSON
    
- Validasi otomatis
    
- Dokumentasi API otomatis (Swagger)
    

---

### 11. Handling JSON Request (FastAPI)

`from fastapi import FastAPI from pydantic import BaseModel  app = FastAPI()  class User(BaseModel):     username: str     role: str  @app.post("/user") def create_user(user: User):     return user`

📌 JSON otomatis:

- Diparse
    
- Divalidasi
    
- Didokumentasikan
    

---

### 12. Response JSON di FastAPI

`return {     "status": "ok",     "data": user }`

FastAPI otomatis serialize ke JSON.

---

### 13. Error Handling JSON di FastAPI

`from fastapi import HTTPException  if user.role not in ["admin", "user"]:     raise HTTPException(status_code=400, detail="Role tidak valid")`

Response:

`{   "detail": "Role tidak valid" }`

---

## 14. JSON & Keamanan di Python

Best practice:

- Validasi struktur & tipe data
    
- Batasi ukuran payload
    
- Jangan simpan data mentah tanpa filter
    
- Gunakan schema (Pydantic / Marshmallow)