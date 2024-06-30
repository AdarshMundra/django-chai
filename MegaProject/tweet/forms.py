from django.forms import ModelForm
from .models import Tweet

class Tweetform(ModelForm):
    class Meta:
        model = Tweet
        fields = ['text','photo']
