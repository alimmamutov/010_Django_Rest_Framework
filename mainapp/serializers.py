from rest_framework.serializers import ModelSerializer, StringRelatedField, PrimaryKeyRelatedField
from authapp.serializers import UserModelSerializer
from mainapp.models import Project


class ProjectModelSerializer(ModelSerializer):
    # users = StringRelatedField(many=True)
    users = PrimaryKeyRelatedField

    class Meta:
        model = Project
        fields = ['name', 'repository', 'users']
