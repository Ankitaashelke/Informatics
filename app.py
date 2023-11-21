# Example app.py

import streamlit as st

def main():
    st.title("My Streamlit App")
    st.write("Welcome to my app!")
    # Add more Streamlit code or your application logic here

if __name__ == "__main__":
    main()

import pandas as pd
import matplotlib.pyplot as plt

# File path to your dataset
file_path = r'C:\Users\admin\Desktop\Ankitaa\Assignments\Informatics\week 13\new-folder\seattle_home_prices-1.csv'

# Load the dataset into a DataFrame
data = pd.read_csv(file_path)

# Filter data for properties in Seattle
seattle_data = data[data['CITY'] == 'Seattle']

# Filter out rows with missing square footage or price data
seattle_data = seattle_data.dropna(subset=['SQUARE FEET', 'PRICE'])

# Calculate price per square foot
seattle_data['Price per Sq Ft'] = seattle_data['PRICE'] / seattle_data['SQUARE FEET']

# Group by property type and calculate mean price per square foot
grouped_data = seattle_data.groupby('PROPERTY TYPE')['Price per Sq Ft'].mean().reset_index()

# Create a bar plot showing the mean price per square foot for each property type
plt.figure(figsize=(10, 6))
plt.bar(grouped_data['PROPERTY TYPE'], grouped_data['Price per Sq Ft'], color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.xlabel('Property Type')
plt.ylabel('Mean Price per Sq Ft')
plt.title('Mean Price per Square Foot by Property Type in Seattle')
plt.tight_layout()

# Show the plot
plt.show()
