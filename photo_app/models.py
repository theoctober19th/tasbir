from django.db import models
from user_app.models import UserModel

# Create your models here.

class PhotoModel(models.Model):
    photo = models.ImageField(upload_to='uploads')
    location = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='uploaded_photos')
    likes = models.ManyToManyField(UserModel, related_name='liked_photos')

    class Meta:
        verbose_name_plural = 'Photos'

class CommentModel(models.Model):
    commented_by = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='user_comments')
    text = models.TextField()
    parent_post = models.ForeignKey(PhotoModel, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.text if len(self.text) < 22 else self.text[:20]

    class Meta:
        verbose_name_plural = 'Comments'