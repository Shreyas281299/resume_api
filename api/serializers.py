from typing import SupportsRound
from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import Resume
from .doc_exc import get_info

class ResumeSerializers(serializers.ModelSerializer):
    model_phone = serializers.CharField(source='phone')
    model_email = serializers.CharField(source ='email')
        
    class Meta:
        model = Resume
        fields = "__all__"
        ReadOnlyField = (
            'model_phone','model_email'
        )
        



