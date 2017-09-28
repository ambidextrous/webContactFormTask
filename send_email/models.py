# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Post(models.Model):
    """
    Model for contact form
    """
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name

