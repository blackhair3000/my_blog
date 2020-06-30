from django.db import models
import jsonfield

class ArticleContent(models.Model):
    content = jsonfield.JSONField(null=True, blank=True)
