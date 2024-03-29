from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Retailer(models.Model):
    name = models.CharField(max_length=200)
    vendors = models.ManyToManyField(Vendor, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Briefing(models.Model):
    name = models.CharField()
    retailer = models.OneToOneField(Retailer, models.DO_NOTHING, blank=True)
    responsible = models.CharField()
    category = models.OneToOneField(Category, models.DO_NOTHING, blank=True)
    release_date = models.CharField()
    available = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
