from django.http import HttpResponse
from .serializers import LoginSerializer
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import User, Car, Dealership, FAQ, Review
from .serializers import (
    UserSerializer, 
    RegisterSerializer, 
    CarSerializer, 
    DealershipSerializer, 
    FAQSerializer, 
    ReviewSerializer
)
import logging

logger = logging.getLogger(__name__)

def home(request):
    return HttpResponse("IF YOU CAN SEE THIS, YOU ARE ABOUT TO BECOME A CAR OWNER!!")

# User Authentication Views
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class LoginView(APIView):
    def post(self, request):
        logger.debug(f"Request data: {request.data}")
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user:
                
                return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
            else:
                
                return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LogoutView(APIView):
    

    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful."}, status=status.HTTP_200_OK)

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

    def get_object(self):
        return self.request.user

# Car Views
class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsAuthenticated()]  # Restrict these to admin/dealership
        return [AllowAny()]

# Dealership Views
class DealershipViewSet(viewsets.ModelViewSet):
    queryset = Dealership.objects.all()
    serializer_class = DealershipSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsAuthenticated()]  # Restrict these to admin/authorized users
        return [AllowAny()]

# FAQ Views
class FAQListCreateView(generics.ListCreateAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method == 'POST':  # Adding FAQs restricted to admin
            return [IsAuthenticated()]
        return [AllowAny()]

class FAQDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    permission_classes = [IsAuthenticated]

# Review Views
class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

# Additional Endpoints
class SearchCarsView(APIView):
    def get(self, request):
        query_params = request.query_params
        cars = Car.objects.filter(**query_params.dict())  # Apply filters dynamically
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ContactDealershipView(APIView):
    def post(self, request):
        dealership_id = request.data.get('dealership_id')
        message = request.data.get('message')
        # Implement the logic to send an inquiry to the dealership (e.g., email or database entry)
        return Response({"message": "Inquiry sent successfully."}, status=status.HTTP_200_OK)
