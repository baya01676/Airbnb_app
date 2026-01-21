from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RulesViewSet,
    GuestViewSet, PropertyImageViewSet,PropertyDetailAPIView,PropertyListAPIView,
    BookingViewSet, ReviewViewSet, AmenityViewSet,UserProfileListAPIView,UserProfileDetailAPIView,
    CityDetailAPIView,CityListAPIView,LoginView,RegisterView,LogoutView
)

router = DefaultRouter()
router.register(r'rules', RulesViewSet)
router.register(r'guests', GuestViewSet)
router.register(r'property-images', PropertyImageViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'amenity', AmenityViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('property',PropertyListAPIView.as_view(),name='property_list'),
    path('property/<int:pk>/',PropertyDetailAPIView.as_view(),name='property_detail'),
    path('users',UserProfileListAPIView.as_view(),name='users_list'),
    path('users/<int:pk>/',UserProfileDetailAPIView.as_view(),name='user_detail'),
    path('city',CityListAPIView.as_view(),name='city_list'),
    path('city/<int:pk>/',CityDetailAPIView.as_view(),name='city_detail'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('register/',RegisterView.as_view(),name='register')
]