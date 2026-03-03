# 🔍 Penjelasan Mendalam Kode Dasar

## 🔹 `Flask(__name__)`

Membuat instance aplikasi.

`__name__` dipakai agar Flask tahu:

- Root path project
    
- Lokasi folder templates
    
- Lokasi folder static
    

---

## 🔹 Routing

@app.route("/")

Ini adalah decorator.

Artinya:  
Jika ada request ke "/" → jalankan fungsi di bawahnya.

Routing di Flask berbasis URL pattern matching.

---

## 🔹 Function sebagai View

def home():  
    return "Hello World"

Function ini disebut **View Function**.

Ia mengembalikan:

- String
    
- HTML
    
- JSON
    
- Response object
    

---

# 🌐 Dynamic Routing

@app.route("/user/<name>")  
def user(name):  
    return f"Hello {name}"

Flask bisa menangkap parameter URL.

Contoh:

/user/Altair

---

# 📬 HTTP Methods

Secara default Flask menerima GET.

Kalau ingin POST:

@app.route("/login", methods=["GET", "POST"])  
def login():  
    return "Login"

---

# 📄 Template Rendering

Struktur:

project/  
│  
├── app.py  
└── templates/  
    └── index.html

Kode:

from flask import render_template  
  
@app.route("/")  
def home():  
    return render_template("index.html")

Flask menggunakan:

Jinja2

---

# 📊 JSON Response (API Mode)

from flask import jsonify  
  
@app.route("/api")  
def api():  
    return jsonify({"status": "success"})

Flask sangat populer untuk API karena:

- Ringan
    
- Mudah integrasi ML
    
- Tidak banyak overhead