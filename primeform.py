# import module
import streamlit as st
import datetime

from PIL import Image
img = Image.open("PrimeForm.png")

st.image(img,width=600)

# Add Title
st.title("Welcome  to  PrimeForm  Services")

st.markdown("<h3 style='text-align: center; color: orange;'>... data and research made easy</h3>", unsafe_allow_html=True)

st.markdown('<div style="text-align: left; color: black;">Your opinion matters, kindly complete our Customer Satisfaction Survey form below;</div>', unsafe_allow_html=True) 

#Form
with st.form(key='form1', clear_on_submit=True):
    Name= st.text_input("Enter your Full Name:")
    Emailaddress = st.text_input("Enter your Email Address:")
    Mobileno= st.text_input("Enter your Mobile number")
    Gender = st.radio("Select Gender: ",("Male", " Female"))
    Age = st.radio("Age: ",("18-35","36-50","50+",))
    Services = st.radio("Which of our services do you enjoy most?: : ",("Data Analysis", " Research Training", " Artificial Inteligence"))
    Concern = st.radio("What would you improve if you could? : ",("Price","Quality","Service",))
    Message = st.text_area("In your own words, describe how you feel about our services")
    Rateus = st.slider("How will you rate our services in a scale of 5", min_value = 1, max_value = 5)
    
    submit = st.form_submit_button("Submit")
    st.write("Name is :" + " " + Name)
    st.write("Email Address :" + " " + Emailaddress)
    st.write("Mobile number :" +" "+  Mobileno)
    st.write("Gender :" +" "+  Gender)
    st.write("Age :" +" "+  Age)
    st.write("Services :" +" "+  Services)
    st.write("Message :" +" "+  Message)
    st.write("Concern :" +" "+  Concern)
    st.write(Rateus)
   
    
    st.write('<div style="text-align: center; color: black;">Thank you for choosing us.</div>', unsafe_allow_html=True)
