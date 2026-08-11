import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Vehicle Sales Dashboard")

car_data = pd.read_csv("vehicles_us.csv")

hist_button = st.button("Create histogram")

if hist_button:
    st.write("Creating a histogram for the odometer column")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button("Create scatter plot")

if scatter_button:
    st.write("Creating a scatter plot for price vs odometer")
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
