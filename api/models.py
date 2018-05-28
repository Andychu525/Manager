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

    # def save(self, *args, **kwargs):
    #     super(Project, self).save(*args, **kwargs)
    #     ApiGroup(name=self.name, parent=0, level=0, project=self).save()

    def __str__(self):
        return self.name


class ApiGroup(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    parent = models.ForeignKey('self', default=0)
    level = models.IntegerField(default=0)
    project = models.ForeignKey(Project)


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
    status = models.BooleanField()
    desc = models.TextField(null=True, blank=True)
    version = models.CharField(max_length=10, null=True, blank=True)
    project = models.ForeignKey(Project)
    group = models.ForeignKey(ApiGroup)
    create_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now_add=True)


class Header(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    value = models.CharField(max_length=50)
    api = models.ForeignKey(Api, related_name='headers', on_delete=models.CASCADE)


class ApiParam(models.Model):
    key = models.CharField(max_length=20, null=False, blank=False)
    value = models.CharField(max_length=50, null=True, blank=True)
    desc = models.CharField(max_length=20, null=True, blank=True)
    type = models.IntegerField(null=False)  # 参数类型 string int ...
    kind = models.IntegerField(null=False)  # 0：请求参数 1：url参数  2：返回参数
    api = models.ForeignKey(Api, related_name='params', on_delete=models.CASCADE)
    required = models.BooleanField()  # 必填or必含
