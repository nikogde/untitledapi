from rest_framework import serializers
from users.models import User, UserAddress, AccountDetails


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'balance', 'full_address')



class AccSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountDetails
        fields = ('user', 'gender', 'birth_date', 'balance','pensioner')


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ('user', 'street_address', 'city', 'country')