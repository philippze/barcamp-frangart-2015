from django.db import models

from cms.models import CMSPlugin


class IframePluginModel(CMSPlugin):
    url = models.URLField()
