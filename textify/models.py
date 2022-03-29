from django.db import models

# Create your models here.


class Textify(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()
    image = models.URLField(default="https://image.zmenu.com/menupic/4612715/072d7a11-2c4d-4d2d-bd6b-7b32b10d9721.jpg")
    def _str_(self):
        return self.title
