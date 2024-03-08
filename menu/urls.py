from django.urls import path
from .views import MenuAPIView


urlpatterns = [
    path('view-menu/', MenuAPIView.as_view(), name='view-menu'),

]
