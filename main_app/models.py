from smtplib import SMTPRecipientsRefused
from django.db import models
from django.urls import reverse

# Create your models here.

class Predator(models.Model):
    commonName = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.commonName
    
    def get_absolute_url(self):
        return reverse('predators_detail', kwargs={'pk': self.id})

class Finch(models.Model):
    commonName = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    iocSequence = models.IntegerField()
    # Adding M:M relationship
    predators = models.ManyToManyField(Predator)

    def __str__(self):
        return f'{self.commonName} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})

class Sighting(models.Model):
    date = models.DateField('sighting date')
    location = models.CharField(max_length=50)

    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.location} on {self.date}"
    
    class Meta:
        ordering = ['-date']