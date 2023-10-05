from django.urls import path
from . import views

urlpatterns = [
    path('sort-csv/', views.sort_csv_view, name='sort_csv'),
]