import requests
import pandas as pd
import time

def fetch_coordinates(city, api_key):
    """
    Fetches the latitude and longitude for a given city using the API Ninjas Geocoding API.

    Args:
        city (str): The name of the city to geocode.
        api_key (str): Your API Ninjas API key.

    Returns:
        tuple: A tuple containing the latitude and longitude, or (None, None) if not found.
    """
    base_url = 'https://api.api-ninjas.com/v1/geocoding'
    headers = {'X-Api-Key': 'y9coPug3N/l/R56ws1i04w==lkzCGhpIGOHt0BKx'}
    params = {'city': city}

    try:
        response = requests.get(base_url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        if data:
            return data[0]['latitude'], data[0]['longitude']
        else:
            print(f"No coordinates found for city: {city}")
            return None, None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for city: {city} - {e}")
        return None, None

def update_csv_with_coordinates(input_csv, output_csv, api_key):
    """
    Reads a CSV file with a 'location' column, fetches coordinates for each location,
    and writes the updated data to a new CSV file.

    Args:
        input_csv (str): Path to the input CSV file containing a 'location' column.
        output_csv (str): Path to the output CSV file to save the updated data.
        api_key (str): Your API Ninjas API key.
    """
    # Read the input CSV file
    df = pd.read_csv(input_csv)

    # Ensure the 'location' column exists
    if 'Place' not in df.columns:
        print("The input CSV file must contain a 'Place' column.")
        return

    # Initialize lists to store coordinates
    latitudes = []
    longitudes = []

    # Iterate over each location to fetch coordinates
    for location in df['Place']:
        lat, lon = fetch_coordinates(location, api_key)
        latitudes.append(lat)
        longitudes.append(lon)
        time.sleep(1)  # To adhere to API rate limits

    # Add the coordinates to the DataFrame
    df['latitude'] = latitudes
    df['longitude'] = longitudes

    # Write the updated DataFrame to the output CSV file
    df.to_csv(output_csv, index=False)
    print(f"Updated CSV file saved as: {output_csv}")

# Example usage:
# update_csv_with_coordinates('input.csv', 'output.csv', 'y9coPug3N/l/R56ws1i04w==lkzCGhpIGOHt0BKx')


update_csv_with_coordinates('compiled_noise_data 2.csv', 'updated_noise_data.csv', 'y9coPug3N/l/R56ws1i04w==lkzCGhpIGOHt0BKx')
