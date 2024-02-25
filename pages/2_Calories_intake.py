import streamlit as st 
import datetime
import pandas as pd 
import matplotlib.pyplot as plt

height = st.number_input("Enter your height in(cms): ", min_value=0.001)
weight = st.number_input("Enter your weight in kgs: ", min_value=0.001)
def bmi(height, weight):
      value = weight/((height/100)**2)
      return value*(1.0)
def category(person_bmi):
    if person_bmi<16:
        return ("Severe Thiness")
    elif person_bmi>=16 and person_bmi<17:
        return ("Moderate Thiness")
    elif person_bmi>=17 and person_bmi<18.5:
        return ("Mild Thiness")

    elif person_bmi>=18.5 and person_bmi<25:
        return ("Normal")


    elif person_bmi>=25 and person_bmi<30:
        return ("Overweight")


    elif person_bmi>=30 and person_bmi<35:
        return ("Obese Class I")

    elif person_bmi>=35 and person_bmi<40:
        return ("Obese Class II")

    else:
        return ("Obese Class III")
    


if height and weight:
    person_bmi = bmi(height, weight)
    st.write("Your BMI is "+str(person_bmi)+'kg/m2')
    st.write("You lies under the category of " + category(person_bmi))
    if person_bmi>=18.5 and person_bmi<25:
       st.write("Your maintained a healthy life")
    else:
      target_weight = 1
      caloric_margin = 1
      if person_bmi>27.5:
       
       target_weight = st.number_input("Enter the target weight(Weight Loss): ", min_value=0.001)
       caloric_margin = st.number_input("Enter the daily caloric margin(Calorie Deficit): ", min_value=0.001)
       days_to_reach_target = (weight - target_weight) * 7700 / caloric_margin
       
      else:
         
         target_weight = st.number_input("Enter the target weight(Weight Gain): ",min_value=0.001)
         caloric_margin = st.number_input("Enter the daily caloric margin(Calorie Rise): ", min_value=0.001)
         days_to_reach_target = (target_weight-weight) * 7700 / caloric_margin
        

      if st.button('Calculate'):
        dates = pd.date_range(start=pd.Timestamp.now(), periods=int(days_to_reach_target), freq='D')
        weights = [weight - (caloric_margin / 7700 * i) for i in range(int(days_to_reach_target))]
        df = pd.DataFrame({'Date': dates, 'Weight': weights})
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


