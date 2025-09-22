from django import forms

from .models import FeedBack


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = ('message',)
        widgets = {
            'message': forms.Textarea(attrs={'placeholder':'Feedback Goes Here', 'class': 'text-center'})
        }
        labels = {
            'message': ''
        }