from django.db import models
import os
from django.core.exceptions import ValidationError

def validate_svg(value):
    ext = os.path.splitext(value.name)[1].lower()
    if ext != '.svg':
        raise ValidationError('Only SVG files are allowed.')
    
class Welcome(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    phrase = models.CharField(max_length=100, null=False, blank=False)
    sub_phrase = models.CharField(max_length=100, null=False, blank=False)
    created_at =  models.DateTimeField(auto_now_add=True, null=False,blank=False)
    middle_phrase = models.CharField(max_length=50, null=False, blank=False)
    desc_phrase = models.CharField(max_length=200, null=False, blank=False)
    img = models.FileField(upload_to='images/', validators=[validate_svg])
    def __str__(self):
        return self.phrase
    
class Idea(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    title = models.CharField(max_length=550, null=False, blank=False)
    msg = models.CharField(max_length=550, null=False, blank=False)
    desc = models.CharField(max_length=550, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    def __str__(self):
        return self.title 

class Portfolio(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    title = models.CharField(max_length=380, null=False, blank=False)
    desc = models.CharField(max_length=8880, null=False, blank=False)
    img = models.ImageField(upload_to='images-portfolio/')
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    specs = models.CharField(max_length=280, null=False, blank=False)
    def __str__(self):
        return self.title

class ClientArchives(models.Model):
    id = models.AutoField(primary_key=True,null=False, blank=False)
    email = models.CharField(max_length=180, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    title = models.CharField(max_length=400, null=False, blank=False)
    description = models.CharField(max_length=4000, null=False, blank=False)
    specifications = models.CharField(max_length=4000, null=False, blank=False)
    archive = models.CharField(max_length=280, null=False, blank=False)