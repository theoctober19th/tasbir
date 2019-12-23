from django.db import models

# Create your models here.

class UserModel(models.Model):
    display_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255, blank=False)
    email = models.EmailField()
    website = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    profile_pic = models.ImageField(upload_to='profile_pics')
    bio = models.TextField(blank=True, null=True)
    followers = models.ManyToManyField('UserModel', related_name='followings', blank=True, symmetrical=False)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'AppUsers'