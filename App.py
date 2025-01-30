import streamlit as st  # type: ignore
import pandas as pd  # Change 'pt' to 'pd' for standard naming convention
import matplotlib.pyplot as plt

# Corrected FLOWER_DATA with commas between dictionary entries
FLOWER_DATA = {
    "Marigold": {"cellulose": 30, "pectin": 12, "conversion": 0.3},  # Added a comma
    "Rose": {"cellulose": 25, "pectin": 10, "conversion": 0.25}  # Fixed conversion value to 0.25
}

PLASTIC_EMISSIONS = 6  # kg CO₂ per kg of plastic

# Streamlit app UI
st.title("Carbon Footprint Calculator for Flower Waste")
st.subheader("An estimator of how much biodegradable packaging you can make and how much plastic you can avoid by using flower waste")

# User input
FLOWER_TYPE = st.selectbox("Select Flower Type", list(FLOWER_DATA.keys()))
WEIGHT = st.number_input("Enter Flower Waste Weight in KG", min_value=0.1)

if st.button("Calculate"):
    if FLOWER_TYPE and WEIGHT:
        packaging = WEIGHT * FLOWER_DATA[FLOWER_TYPE]["conversion"]
        plastic_reduction = packaging  # 1:1 replacement of plastic
        co2_savings = plastic_reduction * PLASTIC_EMISSIONS

        # 🎯 Display results
        st.success(f"✅ From {WEIGHT} kg of {FLOWER_TYPE} waste, you can create **{packaging:.2f} kg** of biodegradable packaging!")
        st.success(f"♻️ This avoids **{plastic_reduction:.2f} kg** of plastic waste, reducing **{co2_savings:.2f} kg CO₂** emissions!")

        # 📊 Graph
        fig, ax = plt.subplots()
        labels = ["Biodegradable Packaging", "Plastic Waste Avoided"]
        values = [packaging, plastic_reduction]
        ax.bar(labels, values, color=["green", "blue"])
        st.pyplot(fig)
