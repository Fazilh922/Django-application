from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import CountryViewSet, BlogViewSet, RegisterView
from .views import LogoutView
from .views import UserViewSet
from .views import SampleModelAPIView


router = DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'blogs', BlogViewSet, basename= 'blogs')
router.register(r'users', UserViewSet)

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('api/samples/', SampleModelAPIView.as_view(), name='sample-list'),
]

urlpatterns += router.urls
