import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.title("California Housing Data (1990) by Kaiyun Li")

df = pd.read_csv("housing.csv")

minimum_value = st.slider(
    "Minimal Median House Value",
    min_value=0,
    max_value=500001,
    value=200000,
)

st.subheader("See more filters in the sidebar:")

location_types = st.sidebar.multiselect(
    "Choose the location type",
    options=df["ocean_proximity"].unique(),
    default=df["ocean_proximity"].unique(),
)

income_level = st.sidebar.radio(
    "Choose income level",
    options=["Low", "Medium", "High"],
)

filtered_df = df[df["median_house_value"] >= minimum_value]
filtered_df = filtered_df[
    filtered_df["ocean_proximity"].isin(location_types)
]

if income_level == "Low":
    filtered_df = filtered_df[filtered_df["median_income"] <= 2.5]
elif income_level == "Medium":
    filtered_df = filtered_df[
        (filtered_df["median_income"] > 2.5)
        & (filtered_df["median_income"] < 4.5)
    ]
else:
    filtered_df = filtered_df[filtered_df["median_income"] >= 4.5]

st.map(filtered_df)

st.subheader("Median House Value Distribution")
fig, ax = plt.subplots()
ax.hist(filtered_df["median_house_value"], bins=30)
ax.set_xlabel("Median House Value (US dollars)")
ax.set_ylabel("Number of Districts")
st.pyplot(fig)
