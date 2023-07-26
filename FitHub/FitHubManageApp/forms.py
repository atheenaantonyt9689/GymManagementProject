
from django import forms
from django.contrib.auth.models import User, Group


class AdminstratorCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    # override the fields of the model
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['confirm_password'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['confirm_password'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ['first_name',  'last_name', 'username', 'email', 'password', 'confirm_password']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        # Save user to Group adminstrator
        group_obj, _ = Group.objects.get_or_create(name='Administrator')
        instance.groups.add(group_obj)
        instance.save()
        return instance


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
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['confirm_password'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['confirm_password'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ['first_name',  'last_name', 'username', 'email', 'password', 'confirm_password']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        # Save user to Group Trainer
        group_obj, _ = Group.objects.get_or_create(name='Trainer')
        instance.groups.add(group_obj)
        instance.save()
        return instance






