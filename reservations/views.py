from django.shortcuts import render
from rest_framework import generics
from menus.permissions import IsAdminOrReadOnly
from .serializers import BranchSerializer, ReservationSerializer
from .models import Branch, Reservation


class BranchListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()
    permission_clases =[IsAdminOrReadOnly,]


class ReservationListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ReservationSerializer
    
    def get_queryset(self):
        queryset = Reservation.objects.filter(user = self.request.user)
        return queryset