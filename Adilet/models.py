from django.db import models

class Rezume(models.Model):

    name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    description = models.TextField()
    email = models.EmailField()
    phone1 = models.CharField(max_length=250)
    phone2 = models.CharField(max_length=250)
    Address = models.CharField(max_length=250, default="Kyrgyzstan")
    profession = models.CharField(max_length=250)

    image = models.ImageField(upload_to="images")

    # def get_absolute_url(self):
    #     return self.name

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

