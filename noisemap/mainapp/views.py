import os
import logging

from django.shortcuts import render
from django.http import JsonResponse
from pymongo import MongoClient

logger = logging.getLogger(__name__)

MONGO_URI = os.getenv("MONGO_URI", "")


def get_noise_pollution_data(request):
    location = request.GET.get("location")

    if not location:
        return JsonResponse({"error": "Location is a required parameter."}, status=400)

    try:
        noise_data = fetch_noise_from_mongo(location)
        if noise_data:
            return JsonResponse(noise_data, safe=False)
        else:
            return JsonResponse({"error": "No data found for the given location."}, status=404)
    except Exception as e:
        logger.exception("Unexpected error fetching noise pollution data:")
        return JsonResponse({"error": str(e)}, status=500)


def fetch_noise_from_mongo(location):
    client = None
    try:
        client = MongoClient(MONGO_URI)
        db = client["NoiseDatabase"]
        collection = db["NoiseCollection"]

        location = location.split(",")[0]
        noise_data = list(
            collection.find(
                {"Place": {"$regex": location, "$options": "i"}},
                {"_id": 0},
            )
        )
        return noise_data if noise_data else None
    except Exception as e:
        logger.error(f"Error fetching data from MongoDB: {e}")
        return None
    finally:
        if client:
            client.close()


def data_search(request):
    return render(request, "mainapp/data.html")