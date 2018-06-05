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
    status = models.IntegerField()
    desc = models.TextField(null=True, blank=True)
    version = models.CharField(max_length=10, null=True, blank=True)
    project = models.ForeignKey(Project)
    group = models.ForeignKey(ApiGroup)
    create_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now_add=True)


class ApiHeader(models.Model):
    key = models.CharField(max_length=20, null=False, blank=False)
    value = models.CharField(max_length=50)
    api = models.ForeignKey(Api, related_name='headers', on_delete=models.CASCADE)


class ApiBodyParam(models.Model):
    key = models.CharField(max_length=20, null=False, blank=False)
    exam = models.CharField(max_length=50, null=True, blank=True)
    desc = models.CharField(max_length=50, null=True, blank=True)
    type = models.IntegerField(null=True, default=0)  # 参数类型 string int ...
    required = models.BooleanField()
    api = models.ForeignKey(Api, related_name='body_params', on_delete=models.CASCADE)


class ApiUrlParam(models.Model):
    key = models.CharField(max_length=20, null=False, blank=False)
    exam = models.CharField(max_length=50, null=True, blank=True)
    desc = models.CharField(max_length=20, null=True, blank=True)
    required = models.BooleanField()
    api = models.ForeignKey(Api, related_name='url_params', on_delete=models.CASCADE)


class ApiResponseParam(models.Model):
    key = models.CharField(max_length=20, null=False, blank=False)
    desc = models.CharField(max_length=50, null=True, blank=True)
    type = models.IntegerField(null=True, default=0)
    required = models.BooleanField()
    api = models.ForeignKey(Api, related_name='response_params', on_delete=models.CASCADE)


class ApiEnv(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    desc = models.CharField(max_length=50, null=True, blank=True)
    prefix_url = models.CharField(max_length=20, null=True, blank=True)
    project = models.ForeignKey(Project)


class ApiEnvHeader(models.Model):
    key = models.CharField(max_length=20, null=False, blank=False)
    value = models.CharField(max_length=50)
    env = models.ForeignKey(ApiEnv, related_name='env_headers', on_delete=models.CASCADE)


class ApiEnvParam(models.Model):
    key = models.CharField(max_length=20, null=False, blank=False)
    value = models.CharField(max_length=50)
    env = models.ForeignKey(ApiEnv, related_name='env_params', on_delete=models.CASCADE)


class ApiTestHistory(models.Model):
    """
    request_info:{"apiProtocol":"0","method":"GET","URL":"192.168.32.108:8002\/api\/pt\/activity\/e8%2Fme0MDpK8%3D\/1","headers":[],"requestType":0,"params":[]}
    """
    api = models.ForeignKey(Api, null=True, blank=True)
    request_info = models.TextField()
    response_info = models.TextField()
    create_time = models.DateTimeField(auto_now=True)
