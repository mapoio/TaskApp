from django.db import models


# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=16,
                            unique=True,
                            db_index=True,
                            verbose_name=u'组织名字',
                            help_text=u'必须是独一无二的'
                            )

    created = models.DateField(auto_now_add=True,)

    info = models.TextField(max_length=200,
                            blank=True,
                            verbose_name=u'组织简介',
                            help_text=u'这个还是要选的'
                            )

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
