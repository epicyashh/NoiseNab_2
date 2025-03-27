import pandas as pd
import requests
import time

def get_coordinates(location, city):
    location = location.lower()
    city = city.lower()
    query = f"{location}, {city}" if city else location
    url = f"https://nominatim.openstreetmap.org/search?format=json&q={query}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code} for {query}")
            return None, None
        
        try:
            data = response.json()
            if data:
                return data[0]['lat'], data[0]['lon']
            else:
                print(f"No data found for {query}")
        except requests.exceptions.JSONDecodeError:
            print(f"Failed to parse JSON response for {query}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed for {query}: {e}")
    
    return None, None

def update_csv_with_coordinates(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    
    if 'Place' not in df.columns or 'City' not in df.columns:
        raise ValueError("CSV file must contain 'Place' and 'City' columns")
    
    latitudes = []
    longitudes = []
    
    for place, city in zip(df['Place'], df['City']):
        lat, lon = get_coordinates(place, city)
        latitudes.append(lat)
        longitudes.append(lon)
        time.sleep(1)  # To prevent API rate limiting
    
    df['latitude'] = latitudes
    df['longitude'] = longitudes
    df.to_csv(output_csv, index=False)
    print(f"Updated CSV saved as {output_csv}")

# Example usage
update_csv_with_coordinates("compiled_noise_data 2.csv", "updated_noise_data.csv")