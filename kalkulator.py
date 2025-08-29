import streamlit as st

st.title("Kalkulator Sederhana")

# Input angka
angka1 = st.number_input("Masukkan angka pertama:")
angka2 = st.number_input("Masukkan angka kedua:")

# Pilihan operator
operator = st.selectbox("Pilih operator:", ["+", "-", "×", "÷"])

# Tombol hitung
if st.button("Hitung"):
    if operator == "+":
        result = angka1 + angka2
    elif operator == "-":
        result = angka1 - angka2
    elif operator == "×":
        result = angka1 * angka2
    elif operator == "÷":
        if angka2 != 0:
            result = angka1 / angka2
        else:
            result = "Error: Tidak bisa dibagi dengan nol"
    else:
        result = "Operator tidak dikenal"

    st.success(f"Hasil: {result}")
