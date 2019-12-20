from django.contrib import admin
from user_app.models import UserModel
from photo_app.models import PhotoModel, CommentModel
# Register your models here.


admin.site.register(PhotoModel)
admin.site.register(CommentModel)