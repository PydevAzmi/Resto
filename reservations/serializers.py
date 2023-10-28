from rest_framework import serializers
from .models import Branch, Reservation


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = (
            "name",
            "address",
            "phone_num",
            "open_at",
            "closed_at",
            "guests_per_half_an_hour",
        )

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = (
            "branch",
            "guests",
            "day",
            "time",
            "status",
        )