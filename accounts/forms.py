from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="",
        strip=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "new-password",
            "placeholder": "Password"
        }),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            "autocomplete": "new-password",
            "placeholder": "Password confirmation"
            }),
        strip=False,
        help_text=("Enter the same password as before, for verification."),
    )
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields
        widgets = {
            'username': forms.TextInput(attrs={'placeholder':'Username'})
        }
        labels = {
            'username':''
        }