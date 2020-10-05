from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Content
from .serializers import ContentSerializer, UserSerializer
from django.contrib.auth import authenticate


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = ()

    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def ContentList(request):
    if request.method == 'POST':
        category = request.POST["dropdown"]
        data = Content.objects.filter(tag=category)
        serializer = ContentSerializer(data, many=True)
        return Response(serializer.data)
    return Response({"message": "No data found"})
