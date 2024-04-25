from django.db import models




class Trainer(models.Model):
    full_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="Trainer/")
    facebook = models.CharField(max_length=70)
    instagram = models.CharField(max_length=70)
    twitter = models.CharField(max_length=70)


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    description = models.TextField()
    
    def __str__(self):
        return self.name