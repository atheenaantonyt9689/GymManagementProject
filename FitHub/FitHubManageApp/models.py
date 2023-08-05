from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class FitHubMember(models.Model):
    Male = "Male"
    Female = "Female"
    Others = "Others"
    GenderChoices = (
        (Male, "Male"),
        (Female, "Female"),
        (Others, "Others"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, unique=True)
    designation = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    sex = models.CharField(choices=GenderChoices, max_length=10)
    dob = models.DateField(null=True, blank=True)
    plan = models.ForeignKey('Plan', on_delete=models.CASCADE, null=True, blank=True)
    payment_status = models.BooleanField(default=False)
    joining_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}"


class Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    duration = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    gym_info = models.ForeignKey('GymInformation', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class GymInformation(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100, unique=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    youtube = models.CharField(max_length=100, blank=True, null=True)
    logo = models.ImageField(upload_to='gym_information/', null=True, blank=True,
                             default='gym_information/logo.png')
    about_us = models.TextField(blank=True, null=True)
    members = models.ManyToManyField(User, related_name='gym_members', null=True, blank=True)

    def __str__(self):
        return self.name


class AdminGymGallery(models.Model):
    name = models.CharField(max_length=512, default='')
    image = models.ImageField(upload_to='gym_gallery/', null=True, blank=True, default='gym_gallery/gym_image.png')
    sort_order = models.PositiveIntegerField(default=0)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.name)


class GymMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gym_info = models.ForeignKey('GymInformation', on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    is_trainer = models.BooleanField(default=False)
    is_normal_member = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}"


class GymAdministator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gym_info = models.ForeignKey('GymInformation', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"


class GymTrainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gym_info = models.ForeignKey('GymInformation', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"


class AdminVideoGallery(models.Model):
    name = models.CharField(max_length=512, default='')
    url = models.CharField(max_length=512, default='')
    thumbnail = models.ImageField(upload_to='gym_video_gallery/', null=True, blank=True,
                                  default='gym_video_gallery/gym_video_image.png')
    sort_order = models.PositiveIntegerField(default=0)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.name)


class Equipments(models.Model):
    name = models.CharField(max_length=512, default='')
    image = models.ImageField(upload_to='equipments/', null=True, blank=True, default='equipments/equipment_image.png')
    sort_order = models.PositiveIntegerField(default=0)
    gym_info = models.ForeignKey('GymInformation', on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return "{}".format(self.name)


class EquipmentOrder(models.Model):
    name = models.CharField(max_length=512, default='')
    image = models.ImageField(upload_to='equipments/', null=True, blank=True, default='equipments/equipment_image.png')
    sort_order = models.PositiveIntegerField(default=0)
    gym_info = models.ForeignKey('GymInformation', on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    user = models.ForeignKey('FitHubMember', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now=True)


class Payment(models.Model):
    member = models.ForeignKey('FitHubMember', on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    payment_date = models.DateTimeField(auto_now=True)
    payment_status = models.BooleanField(default=False)
    gym_info = models.ForeignKey('GymInformation', on_delete=models.CASCADE)
    plan = models.ForeignKey('Plan', on_delete=models.CASCADE)


class GymMemberVideoGallery(models.Model):
    name = models.CharField(max_length=512, default='')
    url = models.CharField(max_length=512, default='')
    thumbnail = models.ImageField(upload_to='gym_video_gallery/', null=True, blank=True,
                                  default='gym_video_gallery/gym_video_image.png')
    sort_order = models.PositiveIntegerField(default=0)
    gym_info = models.ForeignKey('GymInformation', on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.name)


class WorkoutVideo(models.Model):
    name = models.CharField(max_length=512, default='')
    url = models.CharField(max_length=512, default='')
    thumbnail = models.ImageField(upload_to='gym_video_gallery/', null=True, blank=True,
                                  default='gym_video_gallery/gym_video_image.png')
    sort_order = models.PositiveIntegerField(default=0)
    gym_info = models.ForeignKey('GymInformation', on_delete=models.CASCADE)
    trainer = models.ForeignKey(User, on_delete=models.CASCADE)


class DietChart(models.Model):
    name = models.CharField(max_length=512, default='')
    image = models.ImageField(upload_to='diet_chart/', null=True, blank=True, default='diet_chart/diet_chart_image.png')
    sort_order = models.PositiveIntegerField(default=0)
    gym_info = models.ForeignKey('GymInformation', on_delete=models.CASCADE)
    trainer = models.ForeignKey(User, on_delete=models.CASCADE)
    member = models.ForeignKey('FitHubMember', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    diet_chart_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)
