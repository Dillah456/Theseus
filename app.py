import streamlit as st
import os
import PyPDF2
import markdown

st.set_page_config(page_title="Repository Reader", layout="wide")

st.title("📂 Repository Document Reader")

# ====== KONFIGURASI ROOT FOLDER ======
ROOT_DIR = "."  # "." berarti folder tempat app.py berada

# ====== Fungsi Baca PDF ======
def read_pdf(path):
    text = ""
    with open(path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
    return text

# ====== Fungsi Baca Markdown ======
def read_markdown(path):
    with open(path, "r", encoding="utf-8") as file:
        md_text = file.read()
    html = markdown.markdown(md_text)
    return md_text, html

# ====== Scan Subfolder ======
subfolders = [
    f for f in os.listdir(ROOT_DIR)
    if os.path.isdir(os.path.join(ROOT_DIR, f))
]

selected_folder = st.sidebar.selectbox(
    "📁 Pilih Folder",
    subfolders
)

if selected_folder:
    folder_path = os.path.join(ROOT_DIR, selected_folder)

    files = [
        f for f in os.listdir(folder_path)
        if f.endswith(".md") or f.endswith(".pdf")
    ]

    if files:
        selected_file = st.selectbox(
            "📄 Pilih File",
            files
        )

        file_path = os.path.join(folder_path, selected_file)

        if selected_file.endswith(".pdf"):
            st.subheader("📄 PDF Content")
            pdf_text = read_pdf(file_path)
            st.text_area("Extracted Text", pdf_text, height=500)

        elif selected_file.endswith(".md"):
            st.subheader("📝 Markdown Content")

            md_text, html = read_markdown(file_path)

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### Raw Markdown")
                st.text_area("Markdown", md_text, height=500)

            with col2:
                st.markdown("### Rendered Preview")
                st.markdown(html, unsafe_allow_html=True)

    else:
        st.info("Tidak ada file .md atau .pdf di folder ini.")