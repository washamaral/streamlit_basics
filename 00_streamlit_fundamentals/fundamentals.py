import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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

df = pd.read_csv("sample.csv")

st.line_chart(df, x="year", y=["col1", "col2", "col3"])

st.area_chart(df, x="year", y=["col1", "col2", "col3"])

st.bar_chart(df, x="year", y=["col1", "col2", "col3"])

geo_df = pd.read_csv("sample_map.csv")

st.map(geo_df)

fig, ax = plt.subplots()
ax.plot(df["year"], df["col1"])
ax.set_title("Gráfico de linha")
ax.set_xlabel("Ano")
ax.set_ylabel("Valor")
fig.autofmt_xdate()

st.pyplot(fig)


# ==============================================================================
st.write(80 * "=")
st.markdown("# Elementos de input")
st.write(80 * "=")
# ==============================================================================

# Inserindo botões primário e secundário:
primary_btn = st.button(label="primary", type="primary")
secondary_btn = st.button(label="secondary", type="secondary")

# Interagindo com os botões:
# Os botões são associados à variáveis, pois eles retornam True se forem clicados e False caso contrário.

if primary_btn:
    st.write("Botão primário clicado")
if secondary_btn:
    st.write("Botão secundário clicado")

# é um checkbox que retorna True se estiver marcado e False caso contrário.

checkbox = st.checkbox("Remember me")

if checkbox:
    st.write("I will remember you")
else:
    st.write("I will forget you")

# é um radio button que retorna o valor da opção selecionada.
# options é uma lista de opções visíveis para o usuário. index é o índice da opção selecionada por padrão.
# horinzontal é um booleano que define se as opções serão exibidas horizontalmente ou verticalmente.

radio = st.radio("Choose a column", options=df.columns[1:], index=0)
st.write(radio)

select = st.selectbox("Choose a column", options=df.columns[1:], index=0)

st.write(select)

multi_select = st.multiselect(
    "Choose columns", options=df.columns[1:], default=["col1"], max_selections=3
)
st.write(multi_select)

slider = st.slider(
    "Pick a number", min_value=0, max_value=10, value=0, step=1
)  # todos os valores devem ser do mesmo tipo. Se um for int todos tem que ser. Se for float, todos tem que ser.

st.write(slider)

text_input = st.text_input("Enter a text", value="Type here...")
# value= "xxx" já deixa um valor preenchido previamente
# placeholder= "xxx" deixa um texto de orientação para o usuário
# type= "password" deixa o texto digitado como asteriscos
# max_chars= 10 limita o número de caracteres digitados

st.write(text_input)

num_input = st.number_input(
    "Enter a number", min_value=0, max_value=10, value=0, step=1
)

st.write(num_input)

text_area = st.text_area(
    "What do you want to tell me?", height=200, placeholder="Type here..."
)

st.write(text_area)


# ==============================================================================
st.write(80 * "=")
st.markdown("# Trabalhando com layouts")
st.write(80 * "=")
# ==============================================================================

with st.sidebar:
    st.write("This is a sidebar")

col1, col2, col3 = st.columns(3)
col1.write("Text in a column")

slider = col2.slider("Pick a number", min_value=0, max_value=10)

col3.write(slider)

tab1, tab2 = st.tabs(["Line plot", "Bar plot"])

# as tabs são abas dentro da página. Cada aba é um container que pode conter qualquer tipo de elemento.

with tab1:
    tab1.write("This is a line plot")
    st.line_chart(df, x="year", y=["col1", "col2", "col3"])

with tab2:
    tab2.write("This is a bar plot")
    st.bar_chart(df, x="year", y=["col1", "col2", "col3"])

with st.expander("Click to expand"):
    st.write("This is an expander")


with st.expander("This is another kind of expander"):
    taba, tabb = st.tabs(["Tab A", "Tab B"])
    with taba:
        taba.write("This is a line plot")
        st.line_chart(df, x="year", y=["col1", "col2", "col3"])

    with tabb:
        tabb.write("This is a bar plot")
        st.bar_chart(df, x="year", y=["col1", "col2", "col3"])

# Não aparece que temos um container. Não é necessário ficar usando.

with st.container():
    st.write("This is an inside container")
    st.line_chart(df, x="year", y=["col1", "col2", "col3"])

st.write("This is a container")
