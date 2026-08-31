from django.urls import path

from .views import DiseaseDetailView,DiseaseListView

urlpatterns = [
    path('', DiseaseListView.as_view(),name='disease-list'),
    path('<int:pk>/', DiseaseDetailView.as_view(), name= 'disease-detail'),
]