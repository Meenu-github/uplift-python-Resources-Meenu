import streamlit as st
import pandas as pd
xls = pd.ExcelFile('bloodDonation.xlsx')
df = pd.read_excel(xls,"blooddonation")
st.write(df)