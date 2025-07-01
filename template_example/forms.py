from django import forms
from django.core import validators
from . models import Usercustom , UserProfileInfo
from django.contrib.auth.models import User 

# Custom validator function to check the length of the name
def clean_name(value):
    if len(value) < 3:
        raise forms.ValidationError("Name must be at least 3 characters long.")
    return value

class FormName(forms.Form):
    name = forms.CharField(validators=[clean_name])
    email = forms.EmailField(label='Enter your email') # Custom label for the email field
    verify_email = forms.EmailField(label='Enter your email again') # Custom label for the verify_email field
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                  widget=forms.HiddenInput
                                  , validators=[validators.MaxLengthValidator(0)]
                                )

    # Custom validation method for the email fields
    def clean(self):
        cleaned_data = super().clean() # Super call to get the cleaned data
        email = cleaned_data["email"]
        verify_email = cleaned_data["verify_email"] 

        if email and verify_email and email != verify_email:
            raise forms.ValidationError("Emails do not match.")

        return cleaned_data
    # def clean_botcatcher(self): # Custom validation method for botcatcher field
    #     botcatcher = self.cleaned_data.get('botcatcher')
    #     if botcatcher:
    #         raise forms.ValidationError("Bot detected!")
    #     return botcatcher


class NewuserForm(forms.ModelForm):
    class Meta:
        model = Usercustom
        fields = '__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())


    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfo(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')

        

