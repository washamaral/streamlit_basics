import streamlit as st
import pandas as pd

st.write(80 * "=")
st.markdown("# Elementos de texto do Streamlit")
st.write(80 * "=")

st.title("This is my title")

st.header("This is a header")

st.subheader("This is a subheader")

st.markdown("## This text is a markdown like *Anaconda* does.")
st.markdown("### This text is a markdown like *Anaconda* does.")

st.caption("This is a caption")
st.code(
    """
import pandas as pd

def import_data():
    df = pd.read_csv('data.csv')
    return df
"""
)

st.text("This is a raw text. It means that it is not a format.")

st.divider()
st.latex(r"\int_{a}^{b} x^2 dx")
st.divider()
st.write("This is a write function")  # pode escrever textos, dataframes, gráficos, etc.

# ==============================================================================
st.write(80 * "=")
st.markdown("# Elementos de display")
st.write(80 * "=")
# ==============================================================================

df = pd.read_csv("tst.csv", sep=";")
st.dataframe(df)
st.write(df)
st.table(df)

# Fica no estilo card do power bi:
st.metric(label="Metric label", value=900, delta="20%", delta_color="normal")

st.metric(
    label="Metric label", value=900, delta="20%", delta_color="inverse"
)  # delta_color="inverse" inverte a cor do delta


# ==============================================================================
st.write(80 * "=")
st.markdown("# Elementos de gráficos")
st.write(80 * "=")
# ==============================================================================
