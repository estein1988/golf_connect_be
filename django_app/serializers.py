from rest_framework import serializers
from .models import User, Course, Foursome
from django.contrib.auth.hashers import make_password

class CourseObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'course_name', 'address', 'city', 'state', 'zip_code', 'lat', 'lon', 'description', 'notes', 'thumbnail', 'url', 'price')

class UserObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'age', 'city', 'description', 'experience', 'handicap')

class FoursomeObjectSerializer(serializers.ModelSerializer):
    course = CourseObjectSerializer(many=False)
    user = UserObjectSerializer(many=False)
    
    class Meta:
        model = Foursome
        fields = ('id', 'course', 'user', 'day', 'date', 'time')


class UserSerializer(serializers.ModelSerializer):
    foursomes = FoursomeObjectSerializer(many=True, required=False)
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'age', 'city', 'description', 'experience', 'handicap', 'foursomes')

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            password = make_password(validated_data['password']),
            email = validated_data['email'],
            full_name = validated_data['full_name'],
            age = validated_data['age'],
            city = validated_data['city'],
            description = validated_data['description'],
            experience = validated_data['experience'],
            handicap = validated_data['handicap'],
        )

        user.save()

        return user

class CourseSerializer(serializers.ModelSerializer):
    users = UserObjectSerializer(many=True)
    foursomes = FoursomeObjectSerializer(many=True)

    class Meta:
        model = Course
        fields = ('id', 'course_name', 'address', 'city', 'state', 'zip_code', 'lat', 'lon', 'description', 'notes', 'thumbnail', 'url', 'price', 'users', 'foursomes')

class FoursomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foursome
        fields = ('id', 'day', 'date', 'time', 'course', 'user')