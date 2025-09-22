from django import forms

from .models import Blog, Comment


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = (
            'category',
            'topic',
            'body',
        )
        widgets = {
            'topic': forms.TextInput(attrs={'placeholder': 'Blog Topic'}),
            'body': forms.Textarea(attrs={'placeholder': 'Blog Body'}),
        }
        labels = {
            'category': 'Choose a category for your blog',
            'topic' : '',
            'body' : ''
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        widgets = {
            'comment': forms.TextInput(attrs={
                'placeholder': 'Leave a comment',
                'class': 'comment-form'})
        }
        labels = {
            'comment': ''
        }