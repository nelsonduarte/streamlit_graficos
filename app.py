import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Visualização Gráfica de Dados")

upload_ficheiro = st.file_uploader("Upload de ficheiro CSV", type=["csv"])

if upload_ficheiro:
    df = pd.read_csv(upload_ficheiro)

    # Visualização de dados
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.subheader("Visualizar Dados")
    numero_linhas = st.slider("Escolha o número de linhas a visualizar", 1, 20, 5)
    st.write(df.head(numero_linhas))

    # Visualização gráfica
    st.subheader("Visualização Gráfica")
    tipo_grafico = st.selectbox("Selecione o tipo de gráfico", ['Bar', 'Line'])
    colunas_numericas = df.select_dtypes(['float64', 'int64']).columns.tolist()
    colunas_texto = df.select_dtypes(['object']).columns.tolist()

    if not colunas_numericas or not colunas_texto:
        st.error("O ficheiro CSV não tem colunas adequadas para a visualização.")
    else:
        col_x = st.selectbox("Selecione a coluna para o eixo X", colunas_texto)
        col_y = st.selectbox("Selecione a coluna para o eixo Y", colunas_numericas)

        if tipo_grafico == 'Bar':
            plt.bar(df[col_x], df[col_y])
        elif tipo_grafico == 'Line':
            plt.plot(df[col_x], df[col_y])

        plt.xlabel(col_x)
        plt.ylabel(col_y)
        plt.title(f"{col_x} vs {col_y}")
        plt.xticks(rotation=45)  # Roda os rótulos do eixo x
        st.pyplot()
