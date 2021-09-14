from django.urls import path
from .views import load_data, QueryResponseView, med_details

urlpatterns = [
    path('', QueryResponseView.as_view(), name="base"),
    path('med/<int:pk>/', med_details, name='detail'),
    path('load/', load_data, name='load'),
]