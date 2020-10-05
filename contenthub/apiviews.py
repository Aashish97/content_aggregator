from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Content
from  .serializers import ContentSerializer

class ContentList(APIView):
    def get(self, request):
        contents = Content.objects.all()
        data = ContentSerializer(contents, many=True).data
        return Response(data)


class ContentDetail(APIView):
    def get(self, request, pk):
        content = get_object_or_404(Content, pk=pk)
        data = ContentSerializer(content).data
        return Response(data)