from django.urls import path, include
from .views import CompanyViewSet, CustomAuthToken, FtpViewSet,AnswerViewSet, UserViewSet, PlanViewSet, QuestionViewSet,MonthViewSet, FileViewSet,UserCompanyViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views



router = DefaultRouter()
router.register('company', CompanyViewSet, basename='company')
router.register('list', UserCompanyViewSet, basename='company-user')
router.register(r'ftp', FtpViewSet, basename='ftp')
router.register('users', UserViewSet)
router.register('plan', PlanViewSet)
router.register('question', QuestionViewSet)
router.register('month', MonthViewSet)
router.register('files', FileViewSet)
router.register('answer', AnswerViewSet)

urlpatterns = [
    
    path('', include(router.urls)),
    path('api-token-auth/', CustomAuthToken.as_view()),
    # path('company/', CompanyViewSet.as_view())


] 