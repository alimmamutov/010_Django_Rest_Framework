from ex import Author
from rest_framework import serializers


class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    birthday_year = serializers.IntegerField()

    def create(self, validated_data):
        return Author(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.birthday_year = validated_data.get('birthday_year', instance.birthday_year)
        return instance

data = {
    "name": 'Alex',
    'birthday_year': 1900
}

ser = AuthorSerializer(data=data)
ser.is_valid()
author = ser.save()

a = 0