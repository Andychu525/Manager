"""Manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^types/$', views.TypeList.as_view()),
    url(r'^types/(?P<pk>[0-9]+)/$', views.TypeDetail.as_view()),
    url(r'^projects/$', views.ProjectList.as_view()),
    url(r'^projects/(?P<pk>[0-9]+)/$', views.ProjectDetail.as_view()),
    url(r'^apis/$', views.ApiList.as_view()),
    url(r'^apis/(?P<pk>[0-9]+)/$', views.ApiDetail.as_view()),
    url(r'^apis/(?P<api_id>[0-9]+)/headers/$', views.HeaderList.as_view()),
    url(r'^api/groups/$', views.ApiGroupList.as_view()),
    url(r'^api/groups/(?P<pk>[0-9]+)/$', views.ApiGroupDetail.as_view()),
    url(r'^group/tree/$', views.group_tree),

]

urlpatterns = format_suffix_patterns(urlpatterns)
