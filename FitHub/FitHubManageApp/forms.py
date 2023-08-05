from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from FitHubManageApp.models import GymInformation, GymTrainer


class AdminstratorCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    # get the gym information
    # gym_info = forms.ModelChoiceField(queryset=GymInformation.objects.all(), empty_label="Select Gym")

    # override the fields of the model
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        # self.fields['username'].widget.attrs['placeholder'] = 'Username'
        # self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['confirm_password'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['confirm_password'].widget.attrs['class'] = 'form-control'
        # self.fields['gym_info'].widget.attrs['placeholder'] = 'Gym Information'
        # self.fields['gym_info'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'confirm_password']

    # def clean(self):
    #     cleaned_data = super().clean()
    #     if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
    #         raise ValidationError("Password and Confirm Password mismatch !")
    #     return cleaned_data

    def clean_password(self):

        if self.data['password'] != self.data['confirm_password']:
            raise ValidationError('Password and Confirmation Password mismatch!')
        validate_password(self.data['password'])
        return self.data['password']

    def clean_email(self):
        validate_email(self.data['email'])
        user = User.objects.filter(username=self.data['email']).first()
        if user:
            raise ValidationError('User with the given email already exists')
        return self.data['email']


class TrainerCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    # override the fields of the model
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'

        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['confirm_password'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['confirm_password'].widget.attrs['class'] = 'form-control'


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'confirm_password']

    def clean_password(self):

        if self.data['password'] != self.data['confirm_password']:
            raise ValidationError('Password and Confirmation Password mismatch!')
        validate_password(self.data['password'])
        return self.data['password']

    def clean_email(self):
        validate_email(self.data['email'])
        user = User.objects.filter(username=self.data['email']).first()
        if user:
            raise ValidationError('User with the given email already exists')
        return self.data['email']



class TrainerUpdateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    # override the fields of the model
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'

        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['confirm_password'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['confirm_password'].widget.attrs['class'] = 'form-control'


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'confirm_password']

    def clean_password(self):

        if self.data['password'] != self.data['confirm_password']:
            raise ValidationError('Password and Confirmation Password mismatch!')
        validate_password(self.data['password'])
        return self.data['password']

    # def clean_email(self):
    #     validate_email(self.data['email'])
    #     user = User.objects.filter(username=self.data['email']).first()
    #     if user:
    #         raise ValidationError('User with the given email already exists')
    #     return self.data['email']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['password'].widget.attrs['class'] = 'form-control'


class ChangePasswordForm(forms.ModelForm):
    new_password = forms.CharField(widget=forms.PasswordInput, max_length=100, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, max_length=100, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['new_password'].widget.attrs['class'] = "form-control"
        self.fields['new_password'].widget.attrs['placeholder'] = "Enter your new password"
        self.fields['confirm_password'].widget.attrs['class'] = "form-control"
        self.fields['confirm_password'].widget.attrs['place-holder'] = "Confirm your password"

    class Meta:
        model = User
        fields = ['new_password', 'confirm_password']

    def clean(self):
        if self.cleaned_data['new_password'] != self.cleaned_data['confirm_password']:
            raise ValidationError("Password and Confirm Password mismatch !")
        # return super().clean()
        return super(ChangePasswordForm, self).clean()


class GymInformationCreateForm(forms.ModelForm):

    # override the fields of the model
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Gym Name'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['placeholder'] = 'Address'
        self.fields['phone'].widget.attrs['placeholder'] = 'Phone'
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['website'].widget.attrs['placeholder'] = 'Website'
        self.fields['website'].widget.attrs['class'] = 'form-control'
        self.fields['facebook'].widget.attrs['placeholder'] = 'Facebook'
        self.fields['facebook'].widget.attrs['class'] = 'form-control'
        self.fields['twitter'].widget.attrs['placeholder'] = 'Twitter'
        self.fields['twitter'].widget.attrs['class'] = 'form-control'
        self.fields['instagram'].widget.attrs['placeholder'] = 'Instagram'
        self.fields['instagram'].widget.attrs['class'] = 'form-control'
        self.fields['youtube'].widget.attrs['placeholder'] = 'Youtube'
        self.fields['youtube'].widget.attrs['class'] = 'form-control'
        self.fields['logo'].widget.attrs['placeholder'] = 'Logo'
        self.fields['logo'].widget.attrs['class'] = 'form-control'
        self.fields['about_us'].widget.attrs['placeholder'] = 'About Us'
        self.fields['about_us'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = GymInformation
        fields = ['name', 'address', 'phone', 'email', 'website', 'facebook', 'twitter', 'instagram', 'youtube', 'logo',
                  'about_us']
