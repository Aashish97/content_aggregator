from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Content
from .serializers import ContentSerializer, UserSerializer
from django.contrib.auth import authenticate


'''
    UserCreate view provides the genric API view to create the new user
    authentication_classes = () and permission_classes = () are used to exempt UserCreate from global authentication scheme.
'''

class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


'''
    LoginView provides the API platform where user can give their username and password, and get a token back.
    We will not be adding a serializer, because we never save a token using this API.
    If the user credential matches the database credential the LoginView  sends the token, else error message is thrown
'''

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


'''
    By default only GET methods will be accepted. Other methods will respond with "405 Method Not Allowed".
    To alter this behaviour, we define @api_view(['GET', 'POST']) to get the POST data sent by the user
    ContentList view sends the list of serialized data(json data) filtering the POST value data from the database to user
'''

@api_view(['GET', 'POST'])
def ContentList(request):
    if request.method == 'POST':
        category = request.POST["dropdown"]
        data = Content.objects.filter(tag=category)
        serializer = ContentSerializer(data, many=True)
        return Response(serializer.data)
    return Response({"message": "No data found"})
