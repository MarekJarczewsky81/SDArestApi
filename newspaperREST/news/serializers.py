from .models import Article
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, EmailField
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import exceptions
from rest_framework.validators import UniqueValidator


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'text', 'owner', 'date')


class UserSerializer(ModelSerializer):
    articles = PrimaryKeyRelatedField(
        queryset=Article.objects.all(), many=True)

    email = EmailField(
        required=False,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message=[
                    "A user with that email already exists."
                ]
            )
        ]
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'articles')

    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')

        try:
            validate_password(password)
        except ValidationError as e:
            raise exceptions.ValidationError({'password': e.messages})
        user = User.objects.create_user(username, email, password)

        return user
    
    # username wolny - ModelField (IntegrityError)✅
    # walidacja maila - ModelField (ValidationError)✅
    # email wolny (unikatowy) - SerializerField (my)✅
    # walidacja hasla✅
    # opcjonalny email - SerializerField (my)✅
