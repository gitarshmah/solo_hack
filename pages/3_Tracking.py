import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


np.random.seed(0)
days = np.arange(1, 101)
target_weight = int(st.number_input('target_weight',min_value=0.001))
current_weight = int(st.number_input('current_weight',min_value=0.001))
calorie_intake = np.random.randint(1800, 2500, size=100) 
calorie_expenditure = np.random.randint(1600, 2200, size=100) 
calorie_deficit = calorie_expenditure - calorie_intake

weight_loss = np.cumsum(calorie_deficit) / 3500  
goal_weight = current_weight - weight_loss

data = pd.DataFrame({
    'Days': days,
    'Current Weight': current_weight - weight_loss,
    'Goal Weight': target_weight,
    'Calorie Deficit': calorie_deficit
})

st.title('Weight Loss Progress Visualization')

days_slider, weight_slider = st.slider(
    label="Adjust number of days and weight:",
    min_value=min(days), max_value=max(days), value=(min(days), max(days)),
    step=1
), st.slider(
    label="Adjust current weight:",
    min_value=int(min(data['Current Weight'])),
    max_value=int(max(data['Current Weight'])),
    value=int(max(data['Current Weight'])),
    step=1
)

filtered_data = data[(data['Days'] >= days_slider[0]) & (data['Days'] <= days_slider[1])]

highlight = alt.selection(type='single', on='mouseover', fields=['Days'], nearest=True)

line_chart = alt.Chart(filtered_data).mark_line().encode(
    x='Current Weight',
    y='Days',
    color=alt.condition(highlight, alt.value('orange'), alt.value('steelblue')),
    tooltip=['Days', 'Current Weight']
).properties(
    width=600,
    height=400
).add_selection(
    highlight
)


scatter_plot = alt.Chart(filtered_data).mark_circle(size=60).encode(
    x='Current Weight',
    y='Days',
    color=alt.condition(alt.datum['Calorie Deficit'] > 0, alt.value('red'), alt.value('green')),
    tooltip=['Days', 'Current Weight', 'Calorie Deficit']
)


combined_chart = line_chart + scatter_plot


st.altair_chart(combined_chart, use_container_width=True)
