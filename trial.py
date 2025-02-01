import streamlit as st  # type: ignore
import pandas as pd
import matplotlib.pyplot as plt

# Waste Data (Flowers & Citrus Peels)
WASTE_DATA = {
    # Flowers
    "Marigold": {"cellulose": 30, "pectin": 12, "conversion": 0.3},
    "Rose": {"cellulose": 25, "pectin": 10, "conversion": 0.25},

    # Citrus Fruit Peels
    "Orange Peel": {"cellulose": 35, "pectin": 20, "conversion": 0.4},
    "Lemon Peel": {"cellulose": 38, "pectin": 22, "conversion": 0.45}
}

PLASTIC_EMISSIONS = 6  # kg CO₂ per kg of plastic

# Streamlit UI
st.title("🌿 Carbon Footprint Calculator for Waste-Based Packaging")
st.subheader("♻️ Estimate how much biodegradable packaging you can make and the plastic waste you can avoid!")

# Select category: Flowers or Fruit Peels
CATEGORY = st.radio("Select Waste Type", ["Flowers", "Fruit Peels"])

# Adjust options based on category
if CATEGORY == "Flowers":
    options = ["Marigold", "Rose"]
else:
    options = ["Orange Peel", "Lemon Peel"]

# Select specific waste type
WASTE_TYPE = st.selectbox("Select Specific Waste", options)

# Get user input for weight
WEIGHT = st.number_input("Enter Waste Weight in KG", min_value=0.1)

# Calculation & Display
if st.button("Calculate"):
    if WASTE_TYPE and WEIGHT:
        packaging = WEIGHT * WASTE_DATA[WASTE_TYPE]["conversion"]
        plastic_reduction = packaging  # Assuming 1:1 replacement of plastic
        co2_savings = plastic_reduction * PLASTIC_EMISSIONS

        # Display results
        st.success(f"✅ From {WEIGHT} kg of {WASTE_TYPE} waste, you can create **{packaging:.2f} kg** of biodegradable packaging!")
        st.success(f"♻️ This avoids **{plastic_reduction:.2f} kg** of plastic waste, reducing **{co2_savings:.2f} kg CO₂** emissions!")

        # 📊 Visualization
        fig, ax = plt.subplots()
        labels = ["Biodegradable Packaging", "Plastic Waste Avoided"]
        values = [packaging, plastic_reduction]
        ax.bar(labels, values, color=["green", "blue"])
        st.pyplot(fig)
