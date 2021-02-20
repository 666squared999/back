from django.contrib.auth.password_validation import validate_password
from django.core.validators import EmailValidator, RegexValidator
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=15,
        min_length=8,
        write_only=True,
        style={"input_type": "password"},
        validators=[
            RegexValidator(
                "^[a-zA-Z0-9-_']*.{0,1}[a-zA-Z0-9-_']*$",
                message="Wrong username. Invalid symbols used.",
            )
        ],
    )

    confirmPassword = serializers.CharField(
        max_length=15,
        min_length=8,
        write_only=True,
        style={"input_type": "password"},
        validators=[
            RegexValidator(
                "^[a-zA-Z0-9-_']*.{0,1}[a-zA-Z0-9-_']*$",
                message="Wrong username. Invalid symbols used.",
            )
        ],
    )

    email = serializers.CharField(
        required=True,
        allow_blank=False,
        validators=[
            UniqueValidator(queryset=User.objects.all()),
            EmailValidator(message="Wrong email. Invalid symbols used."),
        ],
    )

    username = serializers.CharField(
        max_length=20,
        min_length=3,
        required=True,
        allow_blank=False,
        validators=[
            UniqueValidator(queryset=User.objects.all()),
            RegexValidator(
                "^[a-zA-Z0-9-_']*.{0,1}[a-zA-Z0-9-_']*$",
                message="Wrong username. Invalid symbols used.",
            ),
        ],
    )

    def create(self, validated_data):

        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

    def validate_pass_matching(self, data):
        if data["password"] != data["confirmPassword"]:
            raise serializers.ValidationError(
                {"error": "Passwords do not match"}
            )
        else:
            return data

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "password",
            "confirmPassword",
        )