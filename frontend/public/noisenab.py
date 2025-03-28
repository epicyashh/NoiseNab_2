# -*- coding: utf-8 -*-
"""NoiseNab.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qhn4bqzDS7QWSXhDbngIN3TTOBx35Tay
"""

!pip install folium geopy

import pandas as pd
import folium
from folium.plugins import HeatMap

# Load dataset
df = pd.read_csv("final_data.csv")

# Ensure correct data types
df["Latitude"] = pd.to_numeric(df["Latitude"], errors="coerce")
df["Longitude"] = pd.to_numeric(df["Longitude"], errors="coerce")
df["Noise level(dB)"] = pd.to_numeric(df["Noise level(dB)"], errors="coerce")

# Drop any rows with missing values
df = df.dropna(subset=["Latitude", "Longitude", "Noise level(dB)"])

# Normalize noise levels for heatmap intensity
max_noise = df["Noise level(dB)"].max()
min_noise = df["Noise level(dB)"].min()

# Create a weighting function
def normalize_noise(noise_level):
    return (noise_level - min_noise) / (max_noise - min_noise)

# Prepare heat data with noise intensity
heat_data = []
for _, row in df.iterrows():
    # Add multiple points for each location based on noise intensity
    intensity = normalize_noise(row["Noise level(dB)"])
    num_points = max(1, int(intensity * 10))  # At least 1 point, up to 10 points
    for _ in range(num_points):
        heat_data.append([row["Latitude"], row["Longitude"], intensity])

# Initialize map centered on the mean location
m = folium.Map(location=[df["Latitude"].mean(), df["Longitude"].mean()], zoom_start=5)

# Add HeatMap layer with explicit type conversion
HeatMap(
    heat_data,
    name="Noise Intensity",
    radius=25,
    blur=15,
    max_zoom=1,
    min_opacity=0.5,
    max_opacity=0.8
).add_to(m)

# Add markers for each location with noise level
for idx, row in df.iterrows():
    # Color coding based on noise level
    if row['Noise level(dB)'] > 80:
        color = 'red'
        fill_color = 'darkred'
    elif row['Noise level(dB)'] > 70:
        color = 'orange'
        fill_color = 'orange'
    elif row['Noise level(dB)'] > 60:
        color = 'yellow'
        fill_color = 'yellow'
    else:
        color = 'green'
        fill_color = 'green'

    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=5,
        popup=f"Location: {row['Place']}, Noise Level: {row['Noise level(dB)']} dB",
        color=color,
        fill=True,
        fillColor=fill_color,
        fillOpacity=0.7
    ).add_to(m)

# Add layer control
folium.LayerControl().add_to(m)

# Save the map
m.save("noise_pollution_map.html")

print("Noise pollution map has been generated and saved as noise_pollution_map.html")

# Print some statistics for verification
print("\nNoise Level Statistics:")
print(df["Noise level(dB)"].describe())