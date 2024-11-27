from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from zoomz import views  # Import views module
from zoomz.views import (  # Keep this import if you need specific views like RegisterUserView, etc.
    RegisterUserView,
    LoginView,
    LogoutView,
    UserDetailView,
    CarViewSet,
    DealershipViewSet,
    FAQListCreateView,
    FAQDetailView,
    ReviewListCreateView,
    ReviewDetailView,
    SearchCarsView,
    ContactDealershipView,
)

# Router for ViewSets
router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='car')
router.register(r'dealerships', DealershipViewSet, basename='dealership')

urlpatterns = [
    # Admin route
    path('', views.home, name='home'),  # Now the 'views' module is properly imported

    # User Authentication Endpoints
    path('api/register/', RegisterUserView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/user/', UserDetailView.as_view(), name='user-detail'),

    # Car and Dealership Endpoints via Router
    path('api/', include(router.urls)),

    # FAQ Endpoints
    path('api/faqs/', FAQListCreateView.as_view(), name='faq-list-create'),
    path('api/faqs/<int:pk>/', FAQDetailView.as_view(), name='faq-detail'),

    # Review Endpoints
    path('api/reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('api/reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),

    # Search and Contact Endpoints
    path('api/search/', SearchCarsView.as_view(), name='search-cars'),
    path('api/contact/', ContactDealershipView.as_view(), name='contact-dealership'),
]
