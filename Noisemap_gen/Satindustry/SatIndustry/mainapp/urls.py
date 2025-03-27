from django.urls import path
from . import views 

urlpatterns = [
    path('data/', views.data_search, name='data_search'),
    path('fetch-noise-data/', views.get_noise_pollution_data, name='noise_pollution_data'),
]