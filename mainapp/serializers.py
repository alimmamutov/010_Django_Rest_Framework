from rest_framework.serializers import ModelSerializer, StringRelatedField, PrimaryKeyRelatedField,HyperlinkedModelSerializer
from authapp.serializers import UserModelSerializer
from mainapp.models import Project, ToDo


class ProjectModelSerializer(HyperlinkedModelSerializer):
    # users = StringRelatedField(many=True)
    # users = PrimaryKeyRelatedField
    uid = StringRelatedField(many=False)
    users = UserModelSerializer

    class Meta:
        model = Project
        fields = ['uid', 'name', 'repository', 'users']


class ToDoModelSerializer(HyperlinkedModelSerializer):
    user = UserModelSerializer
    project = ProjectModelSerializer

    class Meta:
        model = ToDo
        fields = '__all__'
