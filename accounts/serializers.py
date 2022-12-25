from rest_framework import serializers

from leave.models import LeaveReportEmployee
from .models import *
from django.contrib.auth import authenticate
from managements.models import *


class LeaveEmployeeSerializer(serializers.ModelSerializer):
    """
    LEAVE FOR EMPLOYEE SERIALIZER
    """

    class Meta:
        model = LeaveReportEmployee
        fields = "__all__"
        read_only_fields = ("employee",)


class EmployeeSerializer(serializers.ModelSerializer):
    """
    EMPLOYEE MODEL SERIALIZERS
    """

    # leave = LeaveEmployeeSerializer(many=True)

    class Meta:
        model = Employee
        fields = ("user", "profile_pic")
        depth = 2

    def create(self, validated_data):
        leave = validated_data.pop("leave")
        employee = Employee.objects.create(**validated_data)
        for x in leave:
            LeaveReportEmployee.objects.create(**x, employee=employee)

        return employee

    def update(self, instance, validated_data):
        leave = validated_data.pop("leave")
        instance.user = validated_data.get("user", instance.user)
        instance.save()
        keep_leave = []
        existing_ids = [x.id for x in instance.leave]
        for x in leave:
            if "id" in x.keys():
                if LeaveReportEmployee.objects.filter(id=x["id"]).exists():
                    x = LeaveReportEmployee.objects.get(id=x["id"])
                    x.leave_reason = x.get("leave_reason", x.leave_reason)
                    x.save()
                    keep_leave.append(x.id)
                else:
                    continue

            else:
                x = LeaveReportEmployee.objects.create(**x, employee=instance)
                keep_leave.append(x.id)

        for x in instance.leave:
            if x.id not in keep_leave:
                x.delete()

        return instance


class UserSerializer(serializers.ModelSerializer):
    """
    USER MODELS SERIALIZERS
    """
    # employee = EmployeeSerializer()
    # leave = LeaveEmployeeSerializer()
    class Meta:
        model = User
        # fields = "__all__"
        fields = ("id","username","email","first_name", "last_name","is_active","is_admin","user_type","is_superadmin")


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    data["user"] = user

                else:
                    msg = "User is deactivated"
                    raise Exception.ValidationError(msg)

        else:
            msg = "Must provide username and password both"
            raise Exception.ValidationError(msg)
        return super().validate(data)
