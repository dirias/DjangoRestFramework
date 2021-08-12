from django.contrib import admin

from profiles_api import models

#Registrar el usuario para que aparezca en el management
admin.site.register(models.UserProfile)
# Register your models here.
