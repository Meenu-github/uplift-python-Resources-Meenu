
import streamlit as st
from openpyxl import Workbook,worksheet,load_workbook
wb = Workbook()
ws = wb.active
ws.title = "blooddonation"
def bloodDonate():
    st.title("Blood Donation")
    from PIL import Image
    image = Image.open("E:\Meenu\Snapchat\_bloodDonation.jpg")
    st.image(image, caption='Blood Donation')
    st.write("This is the blood donation page.")
    st.write("Here if you are willing to donate blood\n you have to register yourself.")
    with st.form(key="Registration for Blood Donation"):
        bloodname = st.text_input("Enter your name : ")
        bgrp = st.text_input("Enter your blood group : ")
        age = st.slider(label="Enter your age ", min_value=18, max_value=45)
        bloodidProof =  st.text_input("Enter your Id Proof Number : ")
        
        submissionblood = st.form_submit_button(label="Submit")
        if submissionblood==True:
            ws.append([bloodname,bgrp,age,bloodidProof])
            wb.save('bloodDonation.xlsx')
            st.success("Successfully submitted your data.")
            st.info("Select a date to donate blood in your nearby blood donation center : ")
            
            
        else:
            st.info("Please register yourself.")
    
print(bloodDonate())   
    #adding date picker..

