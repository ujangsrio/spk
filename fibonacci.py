import streamlit as st 

st.title('Baris Fibonacci')

# Input jumlah bilangan
n = st.number_input("Masukkan jumlah bilangan Fibonacci:", min_value=1, step=1)

# Tombol generate
if st.button("Generate"):
        fib = []
        a, b = 0, 1
        for _ in range(int(n)):
            fib.append(a)
            a, b = b, a + b

        st.success(f"Deret Fibonacci hingga {n} bilangan:")
        st.write(fib)