

import streamlit as st

st.set_page_config(
    page_title='Document AI 1.0', 
    layout="wide",
    initial_sidebar_state="expanded",
 
)




header_html = """

<div style="background-color: #118DFF; padding: 20px; display: flex; align-items: left; flex-direction: column; text-align: center;">
  
    <h3 style="color: white; flex: 1;">Document AI  </h3>
     <h5 style="color: white;">"Explore Your Documents"</h5> 
    
</div>
"""
import google.generativeai as genai



def extract_text(file, temp_dir):
    file_path = os.path.join(temp_dir, file.name)
    with open(file_path, "wb") as f:
        f.write(file.read())

    all_text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            all_text += text

    return all_text

model = genai.GenerativeModel('gemini-pro')

# Mendapatkan input teks dari pengguna
nama = st.text_input('Masukkan pertanyaan')



data = []
if st.button("Run Program", key="run_button"):
    st.spinner('Please wait...')

    
    response = model.generate_content(nama)
    response.text

