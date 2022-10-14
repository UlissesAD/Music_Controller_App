from django import views
from django.urls import path
from .views import RoomView ,CreateRoomView

urlpatterns = [
    path('room', RoomView.as_view()),
    path('create-room', CreateRoomView.as_view())
]