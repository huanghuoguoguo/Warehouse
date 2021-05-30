from django.urls import path
from . import views

urlpatterns = [
    path('', views.show),
    path('detail/<str:obj>/<int:_id>', views.detail)
]
