from django.contrib import admin
from . import models


# admin paneli uchun registratsiyadan otish 
admin.site.register(models.Forms)
admin.site.register(models.Blog)
admin.site.register(models.StaffImg)
admin.site.register(models.About)

# Register your models here.
