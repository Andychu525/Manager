import json

from django.http import JsonResponse
from rest_framework import generics, status, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from  api.models import Project, Type, Api, ApiGroup, Header
from api.serializers import ProjectSerializer, TypeSerializer, ApiSerializer, ApiGroupSerializer, HeaderSerializer


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

    def create(self, request, *args, **kwargs):
        data = request.data.dict()
        data['headers'] = json.loads(data['headers'])
        data['params'] = json.loads(data['params'])
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ApiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Api.objects.all()
    serializer_class = ApiSerializer


class ApiGroupList(generics.ListCreateAPIView):
    queryset = ApiGroup.objects.all()
    serializer_class = ApiGroupSerializer


class ApiGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ApiGroup.objects.all()
    serializer_class = ApiGroupSerializer


class HeaderList(generics.ListCreateAPIView):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer

    def get_queryset(self):
        queryset = Header.objects.all().filter(api=self.kwargs['api_id'])
        return queryset

    def perform_create(self, serializer):
        api_id = self.kwargs['api_id']
        serializer.validated_data['api'] = Api.objects.get(id=api_id)
        serializer.save()


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
