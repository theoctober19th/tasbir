from django.db import models
from user_app.models import UserModel

# Create your models here.

class PhotoModel(models.Model):
    likes = models.PositiveIntegerField(default=0)
    photo = models.ImageField(upload_to='uploads')
    location = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Photos'