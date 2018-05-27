from  rest_framework import serializers
from api.models import Project, Type, Api, ApiGroup, Header, ApiParam


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    type_name = serializers.CharField(source='type.name', read_only=True)
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'


class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = '__all__'
        extra_kwargs = {'api': {'write_only': True}}


class ApiParamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiParam
        fields = '__all__'
        extra_kwargs = {'api': {'write_only': True}}


class ApiSerializer(serializers.ModelSerializer):
    headers = HeaderSerializer(many=True)
    params = HeaderSerializer(many=True)

    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = Api
        fields = ('id', 'name', 'status', 'protocol', 'method', 'version', 'desc', 'group',
                  'headers', 'params', 'update_time', 'create_time')


class ApiGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiGroup
        fields = '__all__'
