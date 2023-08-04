from django import template
from django.contrib.auth.models import Group

register = template.Library()


@register.filter(name='is_supervisor')
def is_supervisor(user):
    return user.groups.filter(name='Supervisor').exists()

@register.filter(name='is_administrator')
def is_administrator(user):
    return user.groups.filter(name='Administrator').exists()
