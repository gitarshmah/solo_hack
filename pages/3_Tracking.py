import streamlit as st
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt 
st.title(" Weight Loss Tracking")
time  = datetime.datetime.now()
person_bmr = st.number_input('Enter your BMR: ')
weight = st.number_input('Enter your current weight: ')
target_weight = st.number_input("Enter the target weight(Weight Loss): ", min_value=0.001)
selected_value = st.slider('Calorie Deficit', min_value=500, max_value=int(person_bmr))

       
if st.button('Calculate'):
         days_to_reach_target = (weight - target_weight) * 7700 / selected_value
         dates = pd.date_range(start=pd.Timestamp.now(), periods=int(days_to_reach_target), freq='D')
         weights = [weight - (selected_value / 7700 * i) for i in range(int(days_to_reach_target))]
         df = pd.DataFrame({'Date': dates, 'Weight': weights})
         exact_time  = ((df.iloc[-1])['Date']).strftime("%b %d, %Y")
         st.line_chart(df.set_index('Date'))
         plt.figure(figsize=(14, 6))
         plt.plot(df['Date'], df['Weight'], marker='o', linestyle='-')
         plt.title('Weight Loss Progress')
         plt.xlabel('Date')
         plt.ylabel('Weight (kg)')
         plt.grid(True)
         plt.xticks(rotation=45)
         plt.tight_layout()
         st.pyplot(plt)
         st.write('You will reach the goal by ' + exact_time)
