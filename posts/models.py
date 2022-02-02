from django.db import models

class Post(models.Model):
    tittle = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.tittle