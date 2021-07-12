import streamlit as st
st.title("FOOD DONATION")
st.header("LET US COME TOGETHER AND FEED THE NEEDY PERSON.")
st.subheader("This is just a trial website.")
st.text("for donating the food\n you can mail your location with your mobile number\n we will reach to you and pick the food from you and distribute it to the needy.\n mail us on : name@gmail.com ")

donate = st.selectbox("donate : ",["ALREADY DONATED", "WANT TO DONATE"])
if donate=="WANT TO DONATE":
    st.info("Do it fast..\n many are waiting for your donation.")
if donate=="ALREADY DONATED":
    st.success("SUCCESSFULLY DONATED FOOD AND SAVED SOMESONE LIFE.")
from PIL import Image
pic = Image.open("E:\Meenu\Snapchat\hunger.jpg")
st.image(pic,width=500,caption="Hunger")
import datetime
today = st.date_input("Today is", datetime.datetime.now())
the_time = st.time_input("time is : ")

import time
my_bar = st.progress(0)
for p in range(100):
    my_bar.progress(p+1)
    time.sleep(.001)
with st.spinner('Waiting..'):
    time.sleep(.001)

st.success("Finished")
st.balloons()
st.sidebar.header("About")
st.sidebar.text("This is just a try")
st.sidebar.header("Menu")
st.sidebar.header("Info")
st.sidebar.header("Contact us")
color = st.color_picker('Choose A Color', '#ffffff')
st.write('The current color is', color)
