from django.db import models
from django.conf import settings

# Create your models here.
class Parfume(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    imageLink = models.TextField()
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Parfume'
        verbose_name_plural = 'Parfumes'

class Comment(models.Model):
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    parfume = models.ForeignKey(Parfume, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'