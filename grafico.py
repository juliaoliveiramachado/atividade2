# atividade2
pip install matplotlib

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

df = pd.read_csv('nascidosvivos_sexo_anoatual_distritos.csv')

total_masculino = df['masculino'].sum()
total_feminino = df['feminino'].sum()

contagens = [total_masculino, total_feminino]

labels = ['Masculino', 'Feminino']

fig, ax = plt.subplots()
ax.pie(contagens, labels=labels, autopct='%1.1f%%')
ax.set_title('Distribuição de Nascidos por Sexo')

st.pyplot(fig)
