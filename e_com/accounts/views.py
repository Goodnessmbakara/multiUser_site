from django.shortcuts import render

# Create your views here.
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import serializers, viewsets

from .serializers import SignupSerializer,LoginSerializer,UserSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=200)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def logout(request):
    request.user.auth_token.delete()
    return Response(status=204)


# class ProfileUpdateView(viewsets.RetrieveUpdateAPIView):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
