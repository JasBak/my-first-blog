from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author= models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    # zasto mi je ovde dao notification 'missing white space around operator jer nisam stavila
    # space oko znaka jednakosti a gore u zagradi kod max length = 200 nije
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date= models.DateTimeField(
        blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titlegit

