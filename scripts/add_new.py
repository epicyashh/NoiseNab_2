import os
import time
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

API_NINJAS_KEY = os.getenv("API_NINJAS_KEY", "")


def fetch_coordinates(city):
    base_url = "https://api.api-ninjas.com/v1/geocoding"
    headers = {"X-Api-Key": API_NINJAS_KEY}
    params = {"city": city}

    try:
        response = requests.get(base_url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        if data:
            return data[0]["latitude"], data[0]["longitude"]
        else:
            print(f"No coordinates found for city: {city}")
            return None, None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for city: {city} - {e}")
        return None, None


def update_csv_with_coordinates(input_csv, output_csv):
    df = pd.read_csv(input_csv)

    if "Place" not in df.columns:
        print("The input CSV file must contain a 'Place' column.")
        return

    latitudes = []
    longitudes = []

    for location in df["Place"]:
        lat, lon = fetch_coordinates(location)
        latitudes.append(lat)
        longitudes.append(lon)
        time.sleep(1)

    df["latitude"] = latitudes
    df["longitude"] = longitudes

    df.to_csv(output_csv, index=False)
    print(f"Updated CSV file saved as: {output_csv}")


if __name__ == "__main__":
    update_csv_with_coordinates("compiled_noise_data 2.csv", "updated_noise_data.csv")
