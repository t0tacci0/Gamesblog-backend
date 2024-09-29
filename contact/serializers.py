from rest_framework import serializers
from .models import ContactModel
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = ['name', 'subject', 'email', 'message', 'created_at']