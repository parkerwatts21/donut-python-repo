# In this file we registered our Model, MissingPerson, so that we could 
# make changes and add data in the admin interface

from django.contrib import admin
from .models import Doughnut
# Register your models here.
admin.site.register(Doughnut)