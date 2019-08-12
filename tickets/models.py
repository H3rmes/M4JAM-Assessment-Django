from django.db import models as m
from django.conf import settings

# Create your models here.
class Ticket(m.Model):
    subject = m.CharField(max_length=50)
    description = m.TextField()
    user_id = m.ForeignKey(settings.AUTH_USER_MODEL,on_delete=m.CASCADE)
    created_at = m.DateTimeField("Datetime created")