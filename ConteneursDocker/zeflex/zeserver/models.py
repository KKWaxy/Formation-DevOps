from django.db import models
from django.utils.translation import gettext_lazy as _
from uuid import uuid1

class Participant(models.Model):

    # id = models.UUIDField(primary_key=True, default=uuid1.)
    nom  = models.CharField(_())
