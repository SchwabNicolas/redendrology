from django.db import models
from django.db.models import Model


class Tree(models.Model):
    invasive_choices = [
        ('NIN', 'Non invasif'),
        ('INV', 'Néophyte invasif')
    ]

    edibility_choices = [
        ('EDI', 'Comestible'),
        ('NED', 'Non comestible'),
        ('SUS', 'Suspect'),
        ('TOX', 'Toxique'),
        ('MOR', 'Mortel')
    ]

    scientific_name = models.CharField(max_length=100)
    authors = models.CharField(max_length=200)
    family = models.CharField(max_length=100)
    common_name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='trees')
    invasive = models.CharField(max_length=3, choices=invasive_choices, default='NIN')
    edibility = models.CharField(max_length=3, choices=edibility_choices, default='NED')
