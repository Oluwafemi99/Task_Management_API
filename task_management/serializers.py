from rest_framework import serializers
from .models import Tasks
from django.contrib.auth import get_user_model
from datetime import date

Users = get_user_model()


class UsersSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Users
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']

    # creating uder with validated_data
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Users.objects.create(**validated_data)
        user.set_password(password)  # set password for user
        user.save()
        return user


class Taskserializers(serializers.ModelSerializer):
    Priority_Level = serializers.ChoiceField(choices=['LOW', 'MEDIUM', 'HIGH'])
    Status = serializers.ChoiceField(choices=['PENDING', 'COMPLETED'])

    class Meta:
        model = Tasks
        fields = '__all__'

    def validate_Due_Date(self, value):
        if value < date.today():
            raise serializers.ValidationError('Due date must be in the future')
        return value

    def validate_Priority_Level(self, value):

        if value == 'LOW':
            message = 'is a low priority task with a deadline. consider scheduling time for it.'

        elif value == 'MEDIUM':
            message = 'is a medium priority task with a deadline. plan accodingly!'

        elif value == 'HIGH':
            message = 'is a high priority task that requires immediate attention'

        else:
            raise serializers.ValidationError('invalid Priority_level')

        # add result to the validated data
        self.context['priority_message'] = message
        return value

    def validate_Status(self, value):

        if value == 'PENDING':
            message = 'The task is currently pending.'

        elif value == 'COMPLETED':
            message = 'The task has been completed.'

        else:
            raise serializers.ValidationError('Invalid Status')

        self.context['status_massage'] = message
        return value

    def validate(self, data):
        Status = data.get('Status')

        if Status == 'COMPLETED' and Status != 'PENDING':
            raise serializers.ValidationError('Completed tasks cannot be edited unless reverted to incomplete.')

        return data
