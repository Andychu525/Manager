from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    type = models.ForeignKey(Type)
    version = models.CharField(max_length=10, blank=False)
    desc = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Api(models.Model):
    Method_CHOICES = (
        ('get', 'get'),
        ('post', 'post'),
        ('put', 'put'),
        ('delete', 'delete')
    )
    name = models.CharField(max_length=20, null=False, blank=False)
    url = models.CharField(max_length=50, null=False, blank=False)
    protocol = models.CharField(max_length=10, default='http://')
    method = models.CharField(max_length=6, choices=Method_CHOICES, null=False)
    desc = models.TextField()
    version = models.CharField(max_length=10, blank=False)
    project = models.ForeignKey(Project)
    create_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now_add=True)
