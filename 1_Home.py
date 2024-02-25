import streamlit as st 
import pandas as pd 
import streamlit_authenticator as stauth
from pathlib import Path 
import pickle


layout ='centered'
page_title = 'Weight Analysis by Calorie Measurement'

st.set_page_config(page_title=page_title, layout=layout)
st.header(page_title)

st.write('''BMI is a measurement of a person's leanness 
or corpulence based on their height and weight, and 
is intended to quantify tissue mass. 
It is widely used as a general indicator of whether a person has a healthy body weight for their height. Specifically, the value obtained from the calculation of BMI is used to categorize whether a person is underweight, normal weight, overweight, or obese depending on what range the value falls between. These ranges of BMI vary based on factors such as region and age, and are sometimes further divided into subcategories such as severely underweight or very severely obese. Being overweight or underweight can have significant health effects, so while BMI is an imperfect measure of healthy body weight, it is a useful indicator of 
whether any additional testing or action is required''')


st.subheader('BMI table and chart for adults')

st.write('''\n\nThis is the World Health Organization's (WHO) recommended body weight based on BMI values for adults. It is used for both men and women, age 20 or older.''')

st.image('/home/arshmah/Pictures/Screenshot from 2024-02-25 20-28-47.png')

st.write('''\n\nThis is a graph of BMI categories based on the World Health Organization data. The dashed lines represent subdivisions within a major categorization.
''')
st.image('https://d26tpo4cm8sb6k.cloudfront.net/img/bmi-chart.gif')


