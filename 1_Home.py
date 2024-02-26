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

st.subheader('BMI Formula')
st.write('''
     BMI in the International System of Units (SI)\n\n
     \t\t\t BMI = Mass(Kg)/(Height(m)^2)
''')


st.text('''You can use the small appliation to analyse your per day calories and 
weight loss analysis''')


st.subheader('Basal Metabolic Rate (BMR)')

st.write('''
The basal metabolic rate (BMR) is the amount of energy needed while resting in 
a temperate environment when the digestive system is inactive. It is the 
equivalent of figuring out how much gas an idle car consumes while parked. 
In such a state, energy will be used only to maintain vital organs, which 
include the heart, brain, kidneys, nervous system, intestines, liver, lungs, 
sex organs, muscles, and skin.
''')

st.write('''
\nMifflin-St Jeor Equation:\n
\nFor men:  BMR = 10W + 6.25H - 5A + 5\n
For women: BMR = 10W + 6.25H - 5A - 161
''')