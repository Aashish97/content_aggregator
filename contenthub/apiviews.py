from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Content
from .serializers import ContentSerializer

@api_view(['GET', 'POST'])
def ContentList(request):
    if request.method == 'POST':
        category = request.POST["dropdown"]
        data = Content.objects.filter(tag=category)
        serializer = ContentSerializer(data, many=True)
        return Response(serializer.data)
    return Response({"message": "No data found"})
