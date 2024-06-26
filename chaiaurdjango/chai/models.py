from django.db import models
from django.utils import timezone
# Create your models here.


class ChaiVarity(models.Model):

    CHAI_TYPE_CHOICES = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
        ('EL', 'ELAICHI'),
    ]
    name = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to="chais/", height_field=None, width_field=None, max_length=None)
    date_added = models.DateTimeField(default=timezone.now)

    type = models.CharField(
        max_length=2, choices=CHAI_TYPE_CHOICES, default='ML')
    description = models.TextField(default='')
    price = models.TextField(default=10)

    def __str__(self):
        return self.name