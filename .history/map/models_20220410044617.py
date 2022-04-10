from django.db import models


class Search(models.Model):
    address = models.CharField(max_length = 200, null=True)
    date = models.DateTimeField(auto_now_add)