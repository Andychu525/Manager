from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    kind = models.IntegerField(null=False)
    version = models.CharField(max_length=10, blank=False)
    desc = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
