import streamlit as st

st.title("Konversi Suhu")

# Input suhu
nilai = st.number_input('Masukkan nilai suhu')

# Input satuan asal
satuan_asal = st.selectbox('Satuan awal', ["Celcius", "Reamur", "Fahrenheit"])

# Input satuan tujuan
satuan_tujuan = st.selectbox('Satuan tujuan', ["Celcius", "Reamur", "Fahrenheit"])

if st.button("Konversi"):
    # Celcius ke lainnya
        if satuan_asal == "Celcius":
            if satuan_tujuan == "Reamur":
                hasil = (4/5) * nilai
            elif satuan_tujuan == "Fahrenheit":
                hasil = (9/5) * nilai + 32
            else:
                hasil = nilai
                
    # Reamur ke lainnya
        elif satuan_asal == "Reamur":
            if satuan_tujuan == "Celcius":
                hasil = (5/4) * nilai
            elif satuan_tujuan == "Fahrenheit":
                hasil = (9/4) * nilai + 32
            else:
                hasil = nilai

    # Fahrenheit ke lainnya
        elif satuan_asal == "Fahrenheit":
            if satuan_tujuan == "Celcius":
                hasil = (5/9) * (nilai - 32)
            elif satuan_tujuan == "Reamur":
                hasil = (4/9) * (nilai - 32)
            else:
                hasil = nilai

        st.success(f"Hasil: {hasil} {satuan_tujuan}")