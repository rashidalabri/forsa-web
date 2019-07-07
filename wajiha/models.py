from django.db import models
from django.utils import timezone

class OpportunityCategory(models.Model):
    name = models.CharField(max_length=250)

class Opportunity(models.Model):
    slug = models.SlugField()

    title = models.CharField(max_length=250)
    description = models.TextField()

    category = models.ForeignKey(OpportunityCategory, models.SET_NULL)

    start_at = models.DateField(blank=True)
    end_at = models.DateField(blank=True)

    website = models.URLField(blank=True)
    phone_number = models.IntegerField(blank=True)
    email = models.EmailField(blank=True)

    age_min = models.IntegerField(blank=True)
    age_max = models.IntegerField(blank=True)

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

