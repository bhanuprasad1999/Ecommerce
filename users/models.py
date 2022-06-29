from django.db import models
from django.contrib.auth.models import User

type = (
    ("seller", "Seller"),
    ("buyer", "buyer"),
)


class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=100, choices=type, default='buyer')
    user_created = models.DateTimeField(auto_now_add=True, editable=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    phone_no = models.BigIntegerField(null=True, blank=True)
