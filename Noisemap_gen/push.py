import pandas as pd
from pymongo import MongoClient

# Load CSV file
csv_file_path = "compiled_noise_data 2.csv"
df = pd.read_csv(csv_file_path)

# Connect to MongoDB
client = MongoClient("mongodb+srv://yashk:EBGXx1DWT1biDGaA@cluster0.19wz30r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # Change if needed
db = client["NoiseDatabase"]  # Database name
collection = db["NoiseCollection"]  # Collection name

# Convert DataFrame to dictionary and insert into MongoDB
data = df.to_dict(orient="records")
collection.insert_many(data)

print(f"Inserted {len(data)} records into MongoDB successfully.")
