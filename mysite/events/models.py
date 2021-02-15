from django.db import models

# Create your models here.

class Venue(models.Model):
    name= models.CharField('Venue Name',max_length=120)
    address = models.CharField(max_length=300)
    phone = models.CharField('Contact Phone',max_length=30)
    web = models.URLField('Website Address')
    email_address = models.EmailField('Email Address')

    def __str__(self):
        return self.name

class ClubUser(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.name



class Event(models.Model):
    name = models.CharField('Event Name',max_length=120)
    event_date = models.DateTimeField('Event Date')
    #venue = models.CharField(max_length=120)
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.CharField('manager',max_length=120)
    description = models.TextField(blank =True)
    attendees = models.ManyToManyField(ClubUser, blank=True)

    def __str__(self):
        return self.name
    