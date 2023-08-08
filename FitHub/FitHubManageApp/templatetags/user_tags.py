from django import template
from django.contrib.auth.models import Group

from FitHubManageApp.models import GymAdministator, GymTrainer, GymMember

register = template.Library()


# @register.filter(name='is_supervisor')
# def is_superuser(user):
#     return user.is_superuser

@register.filter(name='is_administrator')
def is_administrator(user):
    print("tag workd admin")
    return GymAdministator.objects.filter(user=user).exists()


@register.filter(name='is_trainer')
def is_trainer(user):
    print("tag workd trainer")
    return GymTrainer.objects.filter(user=user).exists()


@register.filter(name='is_normal_user')
def is_normal_user(user):
    print("tag workd normal")
    return GymMember.objects.filter(user=user, is_normal_user =True).first()

