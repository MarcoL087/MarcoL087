import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import streamlit as st

st.title('Hello Wilders, welcome to the best application of the year!')

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df = pd.read_csv(link)

df

df_correlation = sns.heatmap(df.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

st.pyplot(viz_correlation.figure)
