from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Company(models.Model):
    class Meta:
        verbose_name_plural = 'companies'

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class JobApplication(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    notes = models.CharField(max_length=400, blank=True)
    STATUSES = (
            (0, 'deadline passed'),
            (1, 'followup'),
            (2, 'successful'),
            (3, 'interviewing'),
            (4, 'post interview'),
            (5, 'rejected'),
            (6, 'todo'),
            (7, 'waiting'),
            )
    status = models.IntegerField(choices=STATUSES, default=6)

    def __str__(self):
        return str(self.company)

class Link(models.Model):
    URL_TYPES = (
            (0, 'internship'),
            (1, 'full time'),
            )
    created_at = models.DateTimeField(editable=False)
    modified_at = models.DateTimeField()
    url_type = models.IntegerField(choices=URL_TYPES, default=1)
    url = models.CharField(max_length=500)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.url

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(Link, self).save(*args, **kwargs)
