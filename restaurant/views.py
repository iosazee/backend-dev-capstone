from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from .models import Booking, Menu
from django.contrib.auth.models import User
from .serializers import BookingSerializer, MenuSerializer, Userserializer
from rest_framework import permissions




# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]


class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Userserializer
    permission_classes = [permissions.IsAuthenticated]


