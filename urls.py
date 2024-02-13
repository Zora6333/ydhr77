from django.urls import path
from .views import upload_json, view_data

urlpatterns = [
    path('upload/', upload_json, name='upload_json'),
    path('data/', view_data, name='view_data'),
]