from rest_framework import serializers
from .models import Approval

class ApprovalSerializer(serializers.Serializer):
    class Meta:
        model = Approval
        fields = '__all__'