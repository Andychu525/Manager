from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from  api.models import Project, Type, Api, ApiGroup
from api.serializers import ProjectSerializer, TypeSerializer, ApiSerializer, ApiGroupSerializer


class TypeList(generics.ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class TypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ApiList(generics.ListCreateAPIView):
    queryset = Api.objects.all()
    serializer_class = ApiSerializer


class ApiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Api.objects.all()
    serializer_class = ApiSerializer


class ApiGroupList(generics.ListCreateAPIView):
    queryset = ApiGroup.objects.all()
    serializer_class = ApiGroupSerializer


class ApiGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ApiGroup.objects.all()
    serializer_class = ApiGroupSerializer


@api_view(['GET'])
def group_tree(request):
    if request.method == 'GET':
        project = request.GET['project']
        groups = ApiGroup.objects.filter(project=project).filter(parent=0)
        return JsonResponse(get_group_tree(groups), safe=False)
    return Response(status=status.HTTP_400_BAD_REQUEST)


def get_group_tree(groups):
    l = []
    for group in groups:
        id = group.id
        name = group.name
        leaf = False
        apis = Api.objects.filter(group=id)
        sub_apis = [{'ID': api.id, 'label': api.name, 'leaf': True} for api in apis]
        sub_groups = get_group_tree(ApiGroup.objects.filter(parent=id))

        children = sub_apis + sub_groups
        l.append({'ID': id, 'label': name, 'leaf': leaf, 'children': children})
    return l
