

from api.models import Allftp, Company, Plan, Question, CustomUser, Month, Files, Answers
from .serializers import CompanySerializer, FtpSerializer, UserSerializer, PlanSerializer, QuestionSerializer,MonthSerializer, FileSerializer, AnswerSerializer
from rest_framework import viewsets
from rest_framework import status

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# from django.contrib.auth.models import User

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend





class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    
    
        
    # permission_classes = [IsAuthenticated]
    # authentication_classes= (TokenAuthentication,)
    # def get(self, format=None):
      
  
class UserCompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['atama', ]

    
    


class FtpViewSet(viewsets.ModelViewSet):
    queryset = Allftp.objects.all()
    serializer_class = FtpSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes= (TokenAuthentication,)


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes= (TokenAuthentication,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username', ]



class MonthViewSet(viewsets.ModelViewSet):
    queryset = Month.objects.all()
    serializer_class = MonthSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answers.objects.all()
    serializer_class = AnswerSerializer
    
class FileViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FileSerializer


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        print(serializer)
        serializer.is_valid(raise_exception=True)
        print("dsadasda", serializer.is_valid(raise_exception=True))
        user = serializer.validated_data['user']
        print(user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
        })
