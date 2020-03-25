from django.contrib import admin

from .models import User, AccountDetails, UserAddress, Passport


admin.site.register(User)
admin.site.register(AccountDetails)
admin.site.register(UserAddress)
admin.site.register(Passport)