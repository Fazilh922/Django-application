from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import FilterSet, filters
from .models import Country, User, Blog
from .serializers import CountrySerializer, UserSerializer, BlogSerializer
from rest_framework.permissions import AllowAny
from rest_framework.serializers import ModelSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from django_filters.rest_framework import FilterSet, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import BasePermission

class CountryFilter(FilterSet):
    class Meta:
        model = Country
        fields = ['continent', 'country']

class BlogFilter(FilterSet):
    class Meta:
        model = Blog
        fields = ['created_by', 'created_at']

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filterset_class = CountryFilter
    permission_classes = [AllowAny]

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filterset_class = BlogFilter
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise ValidationError("User must be authenticated to create a blog.")
        serializer.save(created_by=self.request.user)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['expand'] = self.request.query_params.getlist('expand')
        return context
    
    

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            user = User.objects.create_user(
                username=serializer.validated_data['username'],
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password'],
                date_of_birth=serializer.validated_data.get('date_of_birth'),
                bio=serializer.validated_data.get('bio')
            )
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            # email=validated_data['email'],
           
        )
        return user

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")  # Safely get the 'refresh' token
            if not refresh_token:
                return Response({"error": "Refresh token is required."}, status=status.HTTP_400_BAD_REQUEST)

            # Initialize the RefreshToken class with the token
            token = RefreshToken(refresh_token)
            token.blacklist()  # Blacklist the refresh token

            return Response({"message": "Logged out successfully."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": f"Invalid token: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

class UserFilter(FilterSet):
    country = filters.CharFilter(field_name='country__country', lookup_expr='icontains')
    date_of_birth = filters.DateFilter(field_name='date_of_birth')

    class Meta:
        model = User
        fields = ['country', 'date_of_birth']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter
    permission_classes = [IsAuthenticated] 

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['expand'] = self.request.query_params.getlist('expand')
        return context

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user
    
class SampleModelAPIView(APIView):
    def get(self, request):
        samples = SampleModel.objects.all()
        serializer = SampleSerializer(samples, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SampleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)