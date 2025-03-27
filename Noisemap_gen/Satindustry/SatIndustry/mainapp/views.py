from datetime import datetime, date
import os
import random
import re
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
import requests
import logging
import requests
import rasterio
import numpy as np
import matplotlib.pyplot as plt
from pymongo import MongoClient


logger = logging.getLogger(__name__)
def get_noise_pollution_data(request):
    location = request.GET.get('location')

    if not location:
        return JsonResponse({'error': 'Location is a required parameter.'}, status=400)

    try:
        noise_data = fetchNoiseMongo(location)
        if noise_data:
            return JsonResponse(noise_data, safe=False)  # safe=False to allow returning a list
        else:
            return JsonResponse({'error': 'No data found for the given location.'}, status=404)
    except Exception as e:
        logger.exception("Unexpected error fetching noise pollution data:")
        return JsonResponse({'error': str(e)}, status=500)

def fetchNoiseMongo(location):
    try:
        # Connect to MongoDB
        client = MongoClient("mongodb+srv://yashk:EBGXx1DWT1biDGaA@cluster0.19wz30r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  
        db = client["NoiseDatabase"]  
        collection = db["NoiseCollection"]  

        # Fetch noise pollution data
        noise_data = list(collection.find({"Place": {"$regex": location, "$options": "i"}}, {"_id": 0}))

        return noise_data if noise_data else None
    except Exception as e:
        logger.error(f"Error fetching data from MongoDB: {e}")
        return None
    finally:
        client.close()  # Ensure MongoDB connection is closed

def home(request): # Make sure your home view is still here
    return render(request, 'mainapp/home.html')

def about(request):
    return render(request, 'mainapp/about.html')

def report_form(request):
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'mainapp/report.html')

def data_search(request):
    return render(request, 'mainapp/data.html')