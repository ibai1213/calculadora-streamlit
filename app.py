import streamlit as st

# Configuración básica de la página
st.set_page_config(
    page_title="El objetivo, en tus manos",
    page_icon="🧮",
    layout="wide"
)

# Estilos personalizados para replicar el diseño de la imagen
st.markdown(
    """
    <style>
    /* Fondo principal y tipografía */
    .stApp {
        background-color: #0b1329;
        color: #ffffff;
    }

    /* Título principal */
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 2rem;
    }

    /* Tarjeta contenedora */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #0d1b38;
        border: 1px solid #1c2e56;
        border-radius: 12px;
        padding: 1.5rem;
    }

    /* Botón Calcular (Turquesa / Teal) */
    div.stButton > button[kind="primary"] {
        background-color: #5eead4 !important;
        color: #0b1329 !important;
        border: none !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        padding: 0.5rem 1.5rem !important;
    }
    div.stButton > button[kind="primary"]:hover {
        background-color: #2dd4bf !important;
        color: #0b1329 !important;
    }

    /* Botón Limpiar (Azul oscuro / Grisáceo) */
    div.stButton > button[kind="secondary"] {
        background-color: #1e293b !important;
        color: #ffffff !important;
        border: 1px solid #334155 !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        padding: 0.5rem 1.5rem !important;
    }
    div.stButton > button[kind="secondary"]:hover {
        background-color: #334155 !important;
        color: #ffffff !important;
    }

    /* Texto de resultado en color turquesa */
    .result-text {
        color: #4ee1c3;
        font-size: 1.8rem;
        font-weight: 700;
        margin-top: 1.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Inicializar estado en session_state para permitir la función de "Limpiar"
if "num1" not in st.session_state:
    st.session_state.num1 = 12.0
if "num2" not in st.session_state:
    st.session_state.num2 = 3.0
if "op_idx" not in st.session_state:
    st.session_state.op_idx = 0
if "resultado" not in st.session_state:
    st.session_state.resultado = "—"

def limpiar():
    st.session_state.num1 = 0.0
    st.session_state.num2 = 0.0
    st.session_state.op_idx = 0
    st.session_state.resultado = "—"

# Título de la aplicación
st.markdown('<div class="main-title">El objetivo, en tus manos</div>', unsafe_allow_html=True)

# Contenedor con borde que emula la tarjeta de la imagen
with st.container(border=True):
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        num1 = st.number_input("Primer número", value=float(st.session_state.num1), step=1.0, key="input_num1")

    with col2:
        operaciones = ["Sumar", "Restar", "Multiplicar", "Dividir"]
        op = st.selectbox("Operación", opciones := operaciones, index=st.session_state.op_idx, key="input_op")

    with col3:
        num2 = st.number_input("Segundo número", value=float(st.session_state.num2), step=1.0, key="input_num2")

    # Botones
    col_btn1, col_btn2, _ = st.columns([0.15, 0.15, 0.7])
    with col_btn1:
        calcular = st.button("Calcular", type="primary")
    with col_btn2:
        if st.button("Limpiar", type="secondary"):
            limpiar()
            st.rerun()

    # Lógica de cálculo
    if calcular:
        st.session_state.num1 = num1
        st.session_state.num2 = num2
        st.session_state.op_idx = operaciones.index(op)

        if op == "Sumar":
            res = num1 + num2
            st.session_state.resultado = f"{res:g}"
        elif op == "Restar":
            res = num1 - num2
            st.session_state.resultado = f"{res:g}"
        elif op == "Multiplicar":
            res = num1 * num2
            st.session_state.resultado = f"{res:g}"
        elif op == "Dividir":
            if num2 == 0:
                st.session_state.resultado = "Error: División por cero"
            else:
                res = num1 / num2
                st.session_state.resultado = f"{res:g}"

    # Visualización del resultado
    st.markdown(
        f'<div class="result-text">Resultado: {st.session_state.resultado}</div>',
        unsafe_allow_html=True
    )
