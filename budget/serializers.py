from rest_framework import serializers

from django.contrib.auth.models import User

from budget.models import Expense, Income

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["id", "username", "email", "password"]

        read_only_fields = ["id"]

    def create(self, validated_data):

        return User.objects.create_user(**validated_data)
    

class ExpenseSerializer(serializers.ModelSerializer):

    owner = serializers.StringRelatedField()

    class Meta:

        model = Expense

        fields = "__all__"

        read_only_fields = ["id", "created_date", "owner"]


class IncomeSerializer(serializers.ModelSerializer):

    owner = serializers.StringRelatedField()

    class Meta:

        model = Income

        fields = "__all__"

        read_only_fields = ["id", "created_date", "owner"]

