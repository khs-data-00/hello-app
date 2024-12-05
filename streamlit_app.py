import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

chart_data=pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])

st.bar_chart(chart_data)
st.line_chart(chart_data)
