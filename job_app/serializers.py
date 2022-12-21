from rest_framework import serializers

from .models import TaskModel, ExecutorModel


class ExecutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecutorModel
        fields = (
            '__all__'
        )


class TaskSerializer(serializers.ModelSerializer):
    # executor = ExecutorSerializer()

    class Meta:
        model = TaskModel
        fields = (
            '__all__'
        )
        depth = 1


class SingleTaskSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        TaskModel(**validated_data).save()
        return ''

    class Meta:
        model = TaskModel
        fields = (
            '__all__'
        )
