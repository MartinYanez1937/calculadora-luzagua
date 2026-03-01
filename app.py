import streamlit as st

st.title("💧 Calculadora Luz y Agua")

if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.total = 0
    st.session_state.total_general = 0
    st.session_state.personas = []

# Paso 1
if st.session_state.step == 0:
    total = st.text_input("Ingrese el total de luz y agua")
    if st.button("Continuar"):
        st.session_state.total = float(total.replace(".", ""))
        st.session_state.step = 1

# Paso 2
elif st.session_state.step == 1:
    cantidad = st.number_input("¿Cuántas personas?", min_value=1, step=1)
    if st.button("Continuar"):
        st.session_state.cantidad = int(cantidad)
        st.session_state.actual = 0
        st.session_state.step = 2

# Paso 3
elif st.session_state.step == 2:
    if st.session_state.actual < st.session_state.cantidad:
        st.subheader(f"Persona {st.session_state.actual + 1}")
        nombre = st.text_input("Nombre")
        dias = st.number_input("Total días x personas", min_value=0, step=1)
        
        if st.button("Guardar"):
            st.session_state.personas.append((nombre, dias))
            st.session_state.total_general += dias
            st.session_state.actual += 1
            st.rerun()
    else:
        valor = st.session_state.total / st.session_state.total_general
        
        st.subheader("Resultados")
        for nombre, total_persona in st.session_state.personas:
            pago = round(total_persona * valor)
            pago_formateado = f"{pago:,}".replace(",", ".")
            st.write(f"{nombre} paga {pago_formateado}")
