from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


USER_MODEL = get_user_model()


class UserSignUpForm(UserCreationForm):
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
        model = USER_MODEL
        fields = UserCreationForm.Meta.fields + ('email',)
        widgets = {
            'username': forms.TextInput(attrs={'placeholder':'Username'}),
            'email': forms.TextInput(attrs={'placeholder':'Email', 'required': True})
        }
        labels = {
            'username':'',
            'email':''
        }


class PrivacySettingForm(forms.ModelForm):
    class Meta:
        model = USER_MODEL
        fields = ('is_private',)
        labels = {'is_private': 'Private Account'}