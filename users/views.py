from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from .models import User
    # , UserAddress, Passport, AccountDetails

class UserListView(ListView):
    model = User\
        # , UserAddress, Passport, AccountDetails
    template_name = 'users/users_list.html'