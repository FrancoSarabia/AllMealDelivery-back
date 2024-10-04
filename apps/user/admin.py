from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from ..user.models.client import Client
from ..user.models.employee import Employee
from ..user.models.person import Person
from ..user.models.profile import Profile
from ..user.models.user import User

# Register your models here.
admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(Person)
admin.site.register(Profile)
admin.site.register(User)