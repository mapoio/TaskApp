from django.db import models


# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=16, unique=True, db_index=True)
    created = models.DateField(auto_now_add=True)
    info = models.TextField(max_length=200, blank=True)

    class Meta:
        ordering = ('created',)
        get_latest_by = 'created'

    def __str__(self):
        return '%d - %s' % (self.id, self.name)


class Department(models.Model):
    name = models.CharField(max_length=16, unique=True, db_index=True)
    created = models.DateField(auto_now_add=True)
    info = models.TextField(max_length=200, blank=True)
    company = models.ForeignKey(Company, related_name='department')

    class Meta:
        ordering = ('created',)
        get_latest_by = 'created'

    def __str__(self):
        return '%d - %s' % (self.id, self.name)
