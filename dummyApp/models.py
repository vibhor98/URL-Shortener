# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import random
import string

# Create your models here.

class KirrURL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    update = models.DateTimeField(auto_now=True)    #everytime model is saved
    timestamp = models.DateTimeField(auto_now_add=True)  #when creating the model

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = code_generator()
        super(KirrURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

def code_generator(size=6, chars=string.ascii_lowercase + string.digits):   #create random string
    new_code = ''
    for _ in range(size):
        new_code += random.choice(chars)
    return new_code

def create_shortcode(instance, size=6):     #check for existing shortcode in DB and if not exists new will be generated
    code = code_generator(size=size)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(shortcode=new_code).exists()
    if qs_exists:       #searching for whole DB if particular entry is present more than one time
        #print 'hi'
        #return
        return create_shortcode(size=size)
    return new_code

""" writing anything to this file, type-
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
"""
