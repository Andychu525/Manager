from  rest_framework import serializers
from api.models import Project, Type, Api, ApiGroup, ApiHeader, ApiBodyParam, ApiResponseParam, ApiUrlParam, ApiTestHistory, ApiEnv, ApiEnvHeader, \
    ApiEnvParam


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
        model = ApiHeader
        fields = ('key', 'value')


class ApiBodyParamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiBodyParam
        fields = ('key', 'exam', 'desc', 'type', 'required')


class ApiUrlParamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiUrlParam
        fields = ('key', 'exam', 'desc', 'required')


class ApiResponseParamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiBodyParam
        fields = ('key', 'desc', 'type', 'required')


class ApiSerializer(serializers.ModelSerializer):
    headers = HeaderSerializer(many=True)
    url_params = ApiUrlParamSerializer(many=True)
    body_params = ApiBodyParamSerializer(many=True)
    response_params = ApiResponseParamSerializer(many=True)

    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = Api
        fields = ('id', 'name', 'url', 'status', 'protocol', 'method', 'desc', 'group', 'project', 'headers',
                  'url_params', 'body_params', 'response_params', 'update_time', 'create_time')

    def create(self, validated_data):
        headers = validated_data.pop('headers')
        url_params = validated_data.pop('url_params')
        body_params = validated_data.pop('body_params')
        response_params = validated_data.pop('response_params')
        api = Api.objects.create(**validated_data)

        for header in headers:
            ApiHeader.objects.create(api=api, **header)
        for param in url_params:
            ApiUrlParam.objects.create(api=api, **param)
        for param in body_params:
            ApiBodyParam.objects.create(api=api, **param)
        for param in response_params:
            ApiResponseParam.objects.create(api=api, **param)

        return api

    def update(self, instance, validated_data):

        headers = validated_data.pop('headers')
        url_params = validated_data.pop('url_params')
        body_params = validated_data.pop('body_params')
        response_params = validated_data.pop('response_params')

        instance = super().update(instance, validated_data)

        ApiHeader.objects.filter(api=instance).delete()
        ApiUrlParam.objects.filter(api=instance).delete()
        ApiBodyParam.objects.filter(api=instance).delete()
        ApiResponseParam.objects.filter(api=instance).delete()

        for header in headers:
            ApiHeader.objects.create(api=instance, **header)
        for param in url_params:
            ApiUrlParam.objects.create(api=instance, **param)
        for param in body_params:
            ApiBodyParam.objects.create(api=instance, **param)
        for param in response_params:
            ApiResponseParam.objects.create(api=instance, **param)

        return instance


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


class ApiEnvHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiEnvHeader
        fields = '__all__'


class ApiEnvParamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiEnvParam
        fields = '__all__'


class ApiEnvSerializer(serializers.ModelSerializer):
    env_headers = ApiEnvHeaderSerializer(many=True)
    env_params = ApiEnvParamSerializer(many=True)

    class Meta:
        model = ApiEnv
        fields = ('id', 'name', 'desc', 'prefix_url', 'project', 'env_headers', 'env_params')
