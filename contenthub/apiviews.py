from rest_framework import generics

from .models import Content
from .serializers import ContentSerializer


class ContentList(generics.ListCreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


class ContentDetail(generics.RetrieveDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer