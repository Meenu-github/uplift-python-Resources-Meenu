import streamlit as st
import pandas as pd
xls = pd.ExcelFile('bookDonation.xlsx')
df = pd.read_excel(xls,"bookdonation")
st.write(df)