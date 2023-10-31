from rest_framework import serializers
from .models import Allftp, Company, Plan, Question, CustomUser, Month, Files, Answers
# from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token
from django.contrib.contenttypes.models import ContentType
from drf_writable_nested import WritableNestedModelSerializer





class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Files
        fields = "__all__"
         
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'email', 'first_name',
                  'last_name', "is_staff", "is_superuser", "is_active", "group_name", "bolge"]

        extra_kwargs = {'password': {
            'write_only': True,
            'required': True
        }}

    def create(self, validated_data):

        user = CustomUser.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
    

class CompanySerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    
    files = FileSerializer(many=False)


    class Meta:
        model = Company
        fields = "__all__"

class AnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Answers
        fields = "__all__"

class QuestionSerializer(serializers.ModelSerializer):
    # company = CompanySerializer( many=True )
    
    
    class Meta:
        model = Question
        fields = "__all__"



class FtpSerializer(serializers.ModelSerializer):

    class Meta:
        model = Allftp
        fields = ['id', 'companyName', "tarih", "katilimci",
                  "cevapA", "cevapB", "author", "onay"]


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ["title", "start", "end", "author", "id", "ziyaretarih",
                  "allDay", "backgroundColor", "desc", "companyName"]


        
class MonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Month
        fields = "__all__"



