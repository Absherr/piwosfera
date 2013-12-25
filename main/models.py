from django.contrib import admin
from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=50)
    address = models.URLField()
    rss_address = models.URLField()

    def __unicode__(self):
        return self.name

class Entry(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    address = models.URLField()
    blog = models.ForeignKey(Blog)


    def __unicode__(self):
        return str(self.blog) + ": " + self.title

    class Meta:
        ordering = ['-date']

admin.site.register(Blog)
admin.site.register(Entry)