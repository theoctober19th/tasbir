from django.contrib import admin
from user_app.models import UserModel
from photo_app.models import PhotoModel
# Register your models here.

admin.site.register(UserModel)
admin.site.register(PhotoModel)