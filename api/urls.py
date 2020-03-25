from django.urls import path

from .views import UserAPIView, UserDetail, AccountAPIView, AccDetail, AddressAPIView, AddressDetail

urlpatterns = [
    path('', UserAPIView.as_view()),
    path('<int:pk>/', UserDetail.as_view()),
    path('acc/', AccountAPIView.as_view()),
    path('acc/<int:pk>/', AccDetail.as_view()),
    path('address/', AddressAPIView.as_view()),
    path('address/<int:pk>/', AddressDetail.as_view()),

]