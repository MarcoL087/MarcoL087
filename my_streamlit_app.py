import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import streamlit as st

st.title('Hello Wilders, welcome to the best application of the year!')

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df = pd.read_csv(link)

df


