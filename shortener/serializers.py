#This is the structure for our API.
#Serializers = It handles converting Django model instances to JSON (GET) and validating JSON data for new link creation (POST).
from rest_framework import serializers
from .models import ShortURL

class ShortURLSerializer(serializers.ModelSerializer):   
    # Define the short_code as read-only, so the client doesn't 
    # need to provide it during POST, but it is included in the response.
    short_code = serializers.CharField(read_only=True)
    
    class Meta:        
        model = ShortURL # Use the ShortURL model from your shortener app        
        fields = ['original_url', 'short_code', 'created_at'] # We want to expose the original_url and the auto-generated short_code