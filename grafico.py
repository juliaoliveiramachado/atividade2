# atividade2
import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 2),
    columns=["feminino", "masculino"])

st.bar_chart(chart_data)

