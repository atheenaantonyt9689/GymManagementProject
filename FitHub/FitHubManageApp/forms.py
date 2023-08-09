from django import forms
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from FitHubManageApp.models import GymInformation, GymTrainer, AdminVideoGallery, Blog, Plan, Equipments, FitHubMember, \
    Payment


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


class AdminVideoCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['thumbnail'].widget.attrs['class'] = "company-icon-filepond"
        self.fields['name'].widget.attrs['placeholder'] = 'Gym Name'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        # It should be from youtube iframe section
        self.fields['url'].widget.attrs['placeholder'] = 'Youtube URL'
        self.fields['url'].widget.attrs['class'] = 'form-control'
        self.fields['sort_order'].widget.attrs['placeholder'] = 'Sort Order'
        self.fields['sort_order'].widget.attrs['class'] = 'form-control'
        self.fields['is_admin'].widget.attrs['class'] = 'is-switch'

    class Meta:
        model = AdminVideoGallery
        fields = ['name', 'url', 'sort_order', 'is_admin']

    def clean(self):
        admin_video = AdminVideoGallery.objects.filter(url__iexact=self.cleaned_data['url']).first()
        if admin_video:
            raise ValidationError('Video with the same url already exists!')
        return super().clean()


class AdminVideoEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['thumbnail'].widget.attrs['class'] = "company-icon-filepond"
        self.fields['name'].widget.attrs['placeholder'] = 'Gym Name'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        # It should be from youtube iframe section
        self.fields['url'].widget.attrs['placeholder'] = 'Youtube URL'
        self.fields['url'].widget.attrs['class'] = 'form-control'
        self.fields['sort_order'].widget.attrs['placeholder'] = 'Sort Order'
        self.fields['sort_order'].widget.attrs['class'] = 'form-control'
        self.fields['is_admin'].widget.attrs['class'] = 'is-switch'

    class Meta:
        model = AdminVideoGallery
        fields = ['name', 'url', 'sort_order', 'is_admin']

    def clean(self):
        admin_video = AdminVideoGallery.objects.filter(url__iexact=self.cleaned_data['url']).first()
        if admin_video:
            if admin_video != self.instance:
                raise ValidationError('Video with the same url already exists!')
        return super().clean()


class AdminBlogCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'Blog Title'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        # add image field file upload
        # self.fields['image'].widget.attrs['placeholder'] = 'Blog Image'
        # self.fields['image'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['placeholder'] = 'Blog Description'
        self.fields['description'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Blog
        fields = ['title', 'description', 'image']


# get PlanCreateForm

class PlanCreateForm(forms.ModelForm):
    # getting kwargs from view and passing it to form
    def __init__(self, *args, **kwargs):
        gym_id = kwargs.pop('gym_id', None)
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Plan Name'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['price'].widget.attrs['placeholder'] = 'Plan Price'
        self.fields['price'].widget.attrs['class'] = 'form-control'
        self.fields['duration'].widget.attrs['placeholder'] = 'Plan Duration'
        self.fields['duration'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['placeholder'] = 'Plan Description'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['gym_info'].widget.attrs['placeholder'] = 'Gym Information'
        self.fields['gym_info'].widget.attrs['class'] = 'form-control'
        self.fields['gym_info'].widget.attrs['readonly'] = True
        #     add query based on gym infok
        self.fields['gym_info'].queryset = GymInformation.objects.filter(id=gym_id)

    class Meta:
        model = Plan
        fields = ['name', 'price', 'duration', 'description', 'gym_info']


class EquipmentCreateForm(forms.ModelForm):
    # required True for Image field
    image = forms.ImageField(required=True)

    def __init__(self, *args, **kwargs):
        gym_id = kwargs.pop('gym_id', None)
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Equipment Name'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['placeholder'] = 'Equipment Description'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['placeholder'] = 'Equipment Image'
        self.fields['image'].widget.attrs['class'] = 'form-control'
        self.fields['gym_info'].widget.attrs['placeholder'] = 'Gym Information'
        self.fields['gym_info'].widget.attrs['class'] = 'form-control'
        self.fields['gym_info'].widget.attrs['readonly'] = True
        self.fields['gym_info'].queryset = GymInformation.objects.filter(id=gym_id)
        self.fields['count'].widget.attrs['placeholder'] = 'Equipment Count'
        self.fields['count'].widget.attrs['class'] = 'form-control'
        self.fields['price'].widget.attrs['placeholder'] = 'Equipment Price'
        self.fields['price'].widget.attrs['class'] = 'form-control'
        self.fields['is_available'].widget.attrs['class'] = 'is-switch'

    class Meta:
        model = Equipments
        fields = ['name', 'description', 'image', 'gym_info', 'count', 'price', 'is_available']


# class GymUserCreateForm(forms.Form):
#     password = forms.CharField(widget=forms.PasswordInput())
#     confirm_password = forms.CharField(widget=forms.PasswordInput())
#     first_name = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100)
#     email = forms.EmailField(max_length=100)
#     sex = forms.CharField(max_length=100, required=False)
#     plan = forms.ModelChoiceField(queryset=Plan.objects.all(), required=False)
#     phone = forms.CharField(max_length=10)
#     address = forms.CharField(max_length=200)
#
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
#         self.fields['first_name'].widget.attrs['class'] = 'form-control'
#         self.fields['last_name'].widget.attrs['class'] = 'form-control'
#         self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
#         self.fields['email'].widget.attrs['placeholder'] = 'Email'
#         self.fields['email'].widget.attrs['class'] = 'form-control'
#         self.fields['password'].widget.attrs['placeholder'] = 'Password'
#         self.fields['password'].widget.attrs['class'] = 'form-control'
#         self.fields['confirm_password'].widget.attrs['placeholder'] = 'Confirm Password'
#         self.fields['confirm_password'].widget.attrs['class'] = 'form-control'
#         self.fields['phone'].widget.attrs['placeholder'] = 'Mobile Number'
#         self.fields['phone'].widget.attrs['class'] = 'form-control'
#         self.fields['address'].widget.attrs['placeholder'] = 'Address'
#         self.fields['address'].widget.attrs['class'] = 'form-control'
#         self.fields['plan'].widget.attrs['placeholder'] = 'Plan'
#         self.fields['plan'].widget.attrs['class'] = 'form-control'
#         self.fields['plan'].queryset = Plan.objects.all()
#
#         # class Meta:
#         #     model = FitHubMember
#         #     fields = ['first_name', 'last_name', 'email', 'password', 'confirm_password', 'phone', 'address', 'plan']
#
#         def clean_password(self):
#
#             if self.data['password'] != self.data['confirm_password']:
#                 raise ValidationError('Password and Confirmation Password mismatch!')
#             validate_password(self.data['password'])
#             return self.data['password']
#
#         def clean_email(self):
#             validate_email(self.data['email'])
#             user = User.objects.filter(username=self.data['email']).first()
#             if user:
#                 raise ValidationError(' Email already exists')
#             return self.data['email']


class GymMembershipPaymentForm(forms.ModelForm):
    payment_method = forms.CharField(max_length=100, required=False)
    card_details = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        plan_name = kwargs.pop('plan_name', None)
        super().__init__(*args, **kwargs)
        self.fields['payment_method'].widget.attrs['placeholder'] = 'Payment Method(Online)'
        self.fields['payment_method'].widget.attrs['class'] = 'form-control'
        self.fields['payment_method'].widget.attrs['readonly'] = True
        self.fields['amount'].widget.attrs['placeholder'] = 'Payment Amount'
        self.fields['amount'].widget.attrs['class'] = 'form-control'

        self.fields['plan'].widget.attrs['placeholder'] = 'Plan'
        self.fields['plan'].widget.attrs['class'] = 'form-control'
        self.fields['plan'].widget.attrs['readonly'] = True
        self.fields['card_details'].widget.attrs['placeholder'] = 'Card Number'
        self.fields['card_details'].widget.attrs['class'] = 'form-control'
        self.fields['plan'].queryset = Plan.objects.filter(name=plan_name)

    class Meta:
        model = Payment
        fields = ['amount', 'payment_method','plan', 'card_details']


class GymUserCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    phone = forms.CharField(max_length=10)
    address = forms.CharField(max_length=200)
    plan_name = forms.CharField(max_length=100, required=False)

    # override the fields of the model
    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['phone'].widget.attrs['placeholder'] = 'Mobile Number'
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['placeholder'] = 'Address'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['confirm_password'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['confirm_password'].widget.attrs['class'] = 'form-control'
        self.fields['plan_name'].widget.attrs['placeholder'] = 'Plan'
        self.fields['plan_name'].widget.attrs['class'] = 'form-control'
        # self.fields['plan'].queryset = Plan.objects.all()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'confirm_password', 'plan_name', 'phone', 'address']

    def clean_password(self):

        if self.data['password'] != self.data['confirm_password']:
            raise ValidationError('Password and Confirmation Password mismatch!')
        validate_password(self.data['password'])
        return self.data['password']

    def clean(self):
        validate_email(self.data['email'])
        user = User.objects.filter(username=self.data['email']).first()
        if user:
            # messages.error(self.request, 'User with the given email already exists')
            raise ValidationError('User with the given email already exists')
        return super().clean()
