import os
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

csv_file_path = "compiled_noise_data 2.csv"
df = pd.read_csv(csv_file_path)

client = MongoClient(os.getenv("MONGO_URI"))
db = client["NoiseDatabase"]
collection = db["NoiseCollection"]

data = df.to_dict(orient="records")
collection.insert_many(data)

print(f"Inserted {len(data)} records into MongoDB successfully.")
