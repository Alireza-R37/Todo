from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ('user',)  
        fields = ['title', 'complete'] 



User = get_user_model()

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email") 

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("این ایمیل قبلا ثبت شده است.")
        return email