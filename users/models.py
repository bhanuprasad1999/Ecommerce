from secrets import choice
from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import User

type = (
    ("seller", "Seller"),
    ("buyer", "buyer"),
)


class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=100, choices=type, default='buyer')
    user_created = models.DateTimeField(auto_now_add=True, editable=True)

    
