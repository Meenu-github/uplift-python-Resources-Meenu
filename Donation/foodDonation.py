import streamlit as st
from openpyxl import Workbook,worksheet,load_workbook
wb = Workbook()
ws = wb.active
ws.title = "fooddonation"
def foodDonate():
    st.markdown("FOOD DONATION")
    from PIL import Image
    image = Image.open("E:\Meenu\Snapchat\FoodDonation.jpg")
    st.image(image, caption='Food Donation')
    st.title("Welcome to the food donation page, your donated food can bring hope in someones life of survival.\nCome let us donate food for needy one.\nYou don't have to walk and donate it you just have to register yourself and we will pick the food from your house address that will be provided.")
    st.write("Here if you are willing to donate food\n you have to register yourself.")
    with st.form(key="Register for food donation"):
        namefood = st.text_input("Enter your name : ")
        foodaddress = st.text_input("Enter your address please : ")
        foodidProof = st.text_input("Enter your Id Proof Number : ")
        
        foodsubmission = st.form_submit_button(label="Submit")
        if foodsubmission==True:
            ws.append([namefood,foodaddress,foodidProof])
            wb.save('foodDonation.xlsx')
            st.success("Successfully registered for food donation")
        else:
            st.info("Please submit the form.")

print(foodDonate())