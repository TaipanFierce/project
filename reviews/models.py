from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.utils import timezone
# Create your models here.


@python_2_unicode_compatible
class Reviews(models.Model):
    customer = models.CharField(max_length=100)
    review_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return "{customer} {text}".format(customer=self.customer, text=self.review_text)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now