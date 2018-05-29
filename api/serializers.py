from  rest_framework import serializers
from api.models import Project, Type, Api, ApiGroup, Header, ApiParam, ApiTestHistory


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
        fields = ('name', 'value')


class ApiParamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiParam
        fields = ('key', 'value', 'desc', 'kind', 'type', 'required')
        # extra_kwargs = {'api': {'write_only': True}}


class ApiSerializer(serializers.ModelSerializer):
    headers = HeaderSerializer(many=True)
    params = ApiParamSerializer(many=True)

    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = Api
        fields = ('id', 'name', 'url', 'status', 'protocol', 'method', 'version', 'desc', 'group', 'project',
                  'headers', 'params', 'update_time', 'create_time')

    def create(self, validated_data):
        headers = validated_data.pop('headers')
        params = validated_data.pop('params')
        api = Api.objects.create(**validated_data)
        for header in headers:
            Header.objects.create(api=api, **header)
        for param in params:
            ApiParam.objects.create(api=api, **param)
        return api


class ApiGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiGroup
        fields = '__all__'


class ApiTestHistorySerializer(serializers.ModelSerializer):
    request_info = serializers.CharField()
    response_info = serializers.CharField()

    class Meta:
        model = ApiTestHistory
        fields = '__all__'
