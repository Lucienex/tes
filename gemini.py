

import streamlit as st


import google.generativeai as genai



# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY=('AIzaSyCCxOql_5-Q7DayztCmrOC2o6j-90czFrE')

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

# Mendapatkan input teks dari pengguna
nama = st.text_input('Masukkan pertanyaan')



data = []
if st.button("Run Program", key="run_button"):
    st.spinner('Please wait...')

    
    response = model.generate_content(nama)
    response.text
