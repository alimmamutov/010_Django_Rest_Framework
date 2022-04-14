from rest_framework.serializers import ModelSerializer, StringRelatedField, PrimaryKeyRelatedField,HyperlinkedModelSerializer
from authapp.serializers import UserModelSerializer
from mainapp.models import Project


class ProjectModelSerializer(HyperlinkedModelSerializer):
    users = StringRelatedField(many=True)
    # users = PrimaryKeyRelatedField
    # id = PrimaryKeyRelatedField()

    class Meta:
        model = Project
        fields = ['id', 'name', 'repository', 'users']
