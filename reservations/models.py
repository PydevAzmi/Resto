from django.db import models
from accounts.models import Location
from project.settings import AUTH_USER_MODEL

STATUS = (
    ("In_progres", "In_progres"),
    ("Confirmed", "Confirmed"),
    ("Canceled", "Canceled"),
)

class Branch(models.Model):
    name = models.CharField(max_length=50)
    admin = models.ForeignKey(AUTH_USER_MODEL, related_name="branch_admin", on_delete=models.CASCADE)
    address = models.ForeignKey(Location, related_name="branch_address", on_delete=models.SET_NULL, null=True, blank=True)
    phone_num = models.CharField(max_length=50)
    open_at = models.TimeField()
    closed_at = models.TimeField()
    guests_per_half_an_hour = models.IntegerField(default=40)

    def __str__(self):
        return f"{self.name}"
    
class Reservation(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, related_name="user", on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, related_name="branch", on_delete=models.CASCADE)
    guests = models.IntegerField(default=1)
    time = models.TimeField()
    day = models.DateField()
    status = models.CharField(choices=STATUS ,max_length=50)


    def __str__(self):
        return f"{self.user} {self.branch} *{self.guests}"
    
