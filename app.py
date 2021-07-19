import streamlit as st
from Donation import bookDonation, bloodDonation, foodDonation, firstPage,loginPage

st.markdown("## Welcome to the Donation page.")
st.title("Donation")
st.header("Let us come together and donate something for the needy.")
menu = ["None", "Book Donation", "Blood Donation","Food Donation","Login"]
choice = st.selectbox("Navigation", menu)
if choice=="Book Donation":
    bookDonation.bookdonate()
if choice=="Blood Donation":
    bloodDonation.bloodDonate()
if choice=="Food Donation":
    foodDonation.foodDonate()
if choice == "None":
    firstPage.firstpage()
    st.text("DO YOU KNOW ?")
    st.text("HOW OLD THIS WEB PAGE IS ?")
    st.text("THIS WEB PAGE IS MADE ON 14 JULY 2021")
if choice == "Login":
    loginPage.loginPages()
