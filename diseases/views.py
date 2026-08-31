from rest_framework import generics, permissions

# Create your views here.
from .models import DiseaseDetail
from .serializers import DiseaseDetailSerializer


class DiseaseListView(generics.ListAPIView):
    """
    GET api/diseases/
    GET api/diseases/?search=.....
    """
    queryset = DiseaseDetail.objects.all()
    serializer_class= DiseaseDetailSerializer
    permission_classes= [permissions.IsAuthenticated]
    search_fields=['name']
    
class DiseaseDetailView(generics.RetrieveAPIView):
    """
    GET api/diseases/<id>
    """
    queryset= DiseaseDetail.objects.all()
    serializer_class= DiseaseDetailSerializer
    permission_classes= [permissions.IsAuthenticated]
    