from django.db import models
from django.core.urlresolvers import reverse

class Worker(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    position = models.CharField(max_length=100)
    seniority = models.IntegerField()

    def get_absolute_url(self):
        return reverse('worker-detail', kwargs={'pk': self.pk})
