import streamlit as st

st.title("💧 Calculadora Luz y Agua")

# Inicializar variables
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.total = 0
    st.session_state.cantidad = 0
    st.session_state.actual = 0
    st.session_state.personas = []
    st.session_state.total_general = 0
    st.session_state.veces = 0
    st.session_state.visita_actual = 0
    st.session_state.total_persona = 0
    st.session_state.nombre = ""

# PASO 1: Total servicios
if st.session_state.step == 0:
    total = st.text_input("Ingrese el total de luz y agua")
    if st.button("Continuar"):
        st.session_state.total = float(total.replace(".", ""))
        st.session_state.step = 1
        st.rerun()

# PASO 2: Cantidad personas
elif st.session_state.step == 1:
    cantidad = st.number_input("¿Cuántas personas?", min_value=1, step=1)
    if st.button("Continuar"):
        st.session_state.cantidad = int(cantidad)
        st.session_state.step = 2
        st.rerun()

# PASO 3: Nombre persona
elif st.session_state.step == 2:
    st.subheader(f"Persona {st.session_state.actual + 1}")
    nombre = st.text_input("Nombre")
    if st.button("Continuar"):
        st.session_state.nombre = nombre
        st.session_state.step = 3
        st.rerun()

# PASO 4: Cuántas veces fue
elif st.session_state.step == 3:
    veces = st.number_input("¿Cuántas veces fue en el mes?", min_value=1, step=1)
    if st.button("Continuar"):
        st.session_state.veces = int(veces)
        st.session_state.visita_actual = 0
        st.session_state.total_persona = 0
        st.session_state.step = 4
        st.rerun()

# PASO 5: Datos por visita
elif st.session_state.step == 4:
    if st.session_state.visita_actual < st.session_state.veces:
        st.write(f"Visita {st.session_state.visita_actual + 1}")

        dias = st.number_input("¿Cuántos días se quedó?", min_value=0, step=1)
        personas = st.number_input("¿Con cuántas personas fue?", min_value=0, step=1)

        if st.button("Guardar visita"):
            st.session_state.total_persona += dias * personas
            st.session_state.visita_actual += 1
            st.rerun()
    else:
        # Guardar persona completa
        st.session_state.personas.append(
            (st.session_state.nombre, st.session_state.total_persona)
        )
        st.session_state.total_general += st.session_state.total_persona
        st.session_state.actual += 1

        if st.session_state.actual < st.session_state.cantidad:
            st.session_state.step = 2
        else:
            st.session_state.step = 5

        st.rerun()

# PASO 6: Resultados
elif st.session_state.step == 5:
    st.subheader("Resultados")

    valor = st.session_state.total / st.session_state.total_general

    for nombre, total_persona in st.session_state.personas:
        pago = round(total_persona * valor)
        pago_formateado = f"{pago:,}".replace(",", ".")
        st.write(f"{nombre} paga {pago_formateado}")

    if st.button("Reiniciar"):
        st.session_state.clear()
        st.rerun()
