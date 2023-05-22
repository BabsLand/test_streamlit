import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"


df_car = pd.read_csv(link)

df_car

st.title("Correlation analysis")


df_car_eu = df_car.loc[df_car["continent"] == " Europe.", :]
df_car_eu.drop("continent", axis=1, inplace=True )

df_car_us = df_car.loc[df_car["continent"] == " US.", :]
df_car_us.drop("continent", axis=1, inplace=True )

df_car_jp = df_car.loc[df_car["continent"] == " Japan.", :]
df_car_jp.drop("continent", axis=1, inplace=True )



button_japan_corr = st.button('Japan')
button_europe_corr = st.button('Europe')
button_us_corr = st.button('US')

if button_japan_corr:
	viz_1 = sns.heatmap(df_car_jp.corr().corr(), cmap='RdBu', center=0)
	viz_1.set_title('Correlation between all caracteristics')
	st.pyplot(viz_1.figure)

if button_europe_corr:
	viz_2 = sns.heatmap(df_car_eu.corr().corr(), cmap='RdBu', center=0)
	viz_2.set_title('Correlation between all caracteristics')
	st.pyplot(viz_2.figure)

if button_us_corr:
	viz_3 = sns.heatmap(df_car_us.corr().corr(), cmap='RdBu', center=0)
	viz_3.set_title('Correlation between all caracteristics')
	st.pyplot(viz_3.figure)


st.title("Analysis of the speed by the cylinders")
st.set_option('deprecation.showPyplotGlobalUse', False)


button_japan_dis = st.button('Japan', key='button_japan_dis')
button_europe_dis = st.button('Europe', key='button_europe_dis')
button_us_dis = st.button('US', key='button_us_dis')

if button_japan_dis:
	chart_data_1 = st.bar_chart(df_car_jp, x='cylinders', y='time-to-60')
	

if button_europe_dis:
	chart_data_2 = st.bar_chart(df_car_eu, x = 'cylinders', y='time-to-60')
	

if button_us_dis:
	chart_data_3 = st.bar_chart(df_car_us, x = 'cylinders', y='time-to-60')
	
