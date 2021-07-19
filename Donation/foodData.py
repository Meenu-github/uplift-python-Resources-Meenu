import streamlit as st
import pandas as pd
xls = pd.ExcelFile('foodDonation.xlsx')
df = pd.read_excel(xls,"fooddonation")
st.write(df)