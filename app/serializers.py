from rest_framework import serializers

from app.models import UserLoan


class UserLoanSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserLoan
        fields = '__all__'