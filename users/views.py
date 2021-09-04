from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSignupSerializer, UserSignInSerializer

User = get_user_model()

class SignUpView(CreateAPIView):
    serializer_class = UserSignupSerializer
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response({"message":"SUCCESS"}, status = status.HTTP_201_CREATED)

class SignInView(APIView):
    serializer_class = UserSignInSerializer
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.data
        response = {
            "message":"SUCCESS",
            "user_name":User.objects.get(email = user["email"]).name,
            "token":user["token"]
        }
        return Response(response, status = status.HTTP_200_OK)