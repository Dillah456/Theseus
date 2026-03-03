import streamlit as st
import PyPDF2
import markdown
from io import StringIO

st.set_page_config(page_title="File Reader", layout="wide")

st.title("📂 Markdown & PDF Reader")

uploaded_file = st.file_uploader(
    "Upload file (.md atau .pdf)",
    type=["md", "pdf"]
)

def read_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    return text

def read_markdown(file):
    stringio = StringIO(file.getvalue().decode("utf-8"))
    md_text = stringio.read()
    html = markdown.markdown(md_text)
    return md_text, html

if uploaded_file is not None:
    file_type = uploaded_file.type

    if "pdf" in file_type:
        st.subheader("📄 PDF Content")
        pdf_text = read_pdf(uploaded_file)
        st.text_area("Extracted Text", pdf_text, height=400)

    elif "markdown" in file_type or uploaded_file.name.endswith(".md"):
        st.subheader("📝 Markdown Content")

        md_text, html = read_markdown(uploaded_file)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Raw Markdown")
            st.text_area("Markdown", md_text, height=400)

        with col2:
            st.markdown("### Rendered Preview")
            st.markdown(html, unsafe_allow_html=True)

    else:
        st.warning("Format file tidak didukung.")