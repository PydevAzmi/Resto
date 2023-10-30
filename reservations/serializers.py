from rest_framework import serializers
from .models import Branch, Reservation


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Branch
        fields=(
            "name",
            "admin",
            "address",
            "phone_num",
            "open_at",
            "closed_at",
            "guests_per_half_an_hour",
        )

class ReservationSerializer(serializers.ModelSerializer):
    status = serializers.ReadOnlyField()
    class Meta:
        model=Reservation
        fields=(
            "branch",
            "guests",
            "day",
            "time",
            "status",
        )

    def create(self, validated_data):
        day=validated_data['day']
        hour=validated_data['time'].hour
        branch=Branch.objects.get(name=validated_data['branch'])
        reservation_list=Reservation.objects.filter(branch=branch, day=day)
        for reservation in reservation_list:
            guests=validated_data["guests"]
            if reservation.time.hour == hour:
                guests += reservation.guests
        if guests <= branch.guests_per_half_an_hour:
            reservation=Reservation.objects.create(user= self.context["request"].user,**validated_data)
        else:
            raise serializers.ValidationError("This Branch is Fully completed at that moment, please try again with another hour entry")
        return reservation
        