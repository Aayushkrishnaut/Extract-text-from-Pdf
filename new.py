import streamlit as st
import pdfplumber

def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Streamlit app
st.title("PDF Text Extractor")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    # Extract text from the uploaded PDF
    text = extract_text_from_pdf(uploaded_file)
    if text:
        st.subheader("Extracted Text")
        st.text_area("PDF Text", text, height=400)
    else:
        st.warning("No text could be extracted from this PDF.")
