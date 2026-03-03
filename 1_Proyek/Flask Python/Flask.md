Flask adalah **micro web framework berbasis Python** yang digunakan untuk membangun:

- Website
- REST API
- Backend aplikasi
- Microservice
- Endpoint untuk Machine Learning

Flask dibuat oleh: Armin Ronacher
Dan secara resmi dikelola oleh: Pallets Projects

# 🧠 Kenapa Flask Dibuat?

Sebelum Flask populer, banyak framework terasa:

- Berat
    
- Over-engineered
    
- Banyak aturan bawaan
    

Flask muncul dengan filosofi:

> “Kasih developer kendali penuh.”

Flask hanya menyediakan:

- Routing
    
- Request handling
    
- Response handling
    
- Template rendering
    

Sisanya? Kamu tentukan sendiri.

Ini cocok banget kalau kamu tipe yang suka desain sistem dari nol.

---

# 🏗️ Apa Itu Web Framework Sebenarnya?

Sebelum masuk Flask, kita pahami dulu:

Web framework itu bertugas untuk:

1. Menjalankan server
    
2. Menerima HTTP request
    
3. Mengatur routing URL
    
4. Mengirim HTTP response
    

Tanpa framework, kamu harus:

- Bikin socket manual
    
- Parsing HTTP request sendiri
    
- Mengelola header dan status code
    

Flask menyederhanakan itu.

---

# ⚙️ Konsep Dasar Flask

Flask dibangun di atas dua komponen utama:

## 1️⃣ Werkzeug

Library untuk:

- Handling HTTP
    
- Routing
    
- Request & Response object
    

## 2️⃣ Jinja2

Template engine untuk rendering HTML dinamis.

---

# 🧩 Arsitektur Internal Flask

Ketika user membuka:

http://localhost:5000/

Yang terjadi sebenarnya:

Browser  
   ↓  
HTTP Request  
   ↓  
WSGI Server  
   ↓  
Flask App  
   ↓  
Route Matching  
   ↓  
Function Execution  
   ↓  
Response Object  
   ↓  
Browser

---

# 📦 Apa Itu WSGI?

WSGI = Web Server Gateway Interface

Ini adalah standar Python untuk komunikasi antara:

- Web server
    
- Python application
    

Flask itu sebenarnya **WSGI application**.

Jadi dia tidak langsung bicara ke browser.  
Dia bicara ke server (misalnya Gunicorn).

---

# 🧬 Filosofi “Micro” pada Flask

Micro bukan berarti kecil.

Micro berarti:

- Tidak memaksa struktur
    
- Tidak memaksa ORM
    
- Tidak memaksa authentication system
    

Berbeda dengan:

Django

Django adalah full-stack framework (banyak fitur built-in).

Flask adalah toolkit fleksibel.

---

# 🏁 Instalasi dan Setup

pip install flask

File dasar:

from flask import Flask  
  
app = Flask(__name__)  
  
@app.route("/")  
def home():  
    return "Hello World"  
  
if __name__ == "__main__":  
    app.run(debug=True)