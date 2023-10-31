from django.contrib import admin
from api.models import Allftp, Company, Plan, Question, CustomUser, Month, Files



@admin.register(Company)
class ArticleModel(admin.ModelAdmin):
    list_filter = ('name',)
@admin.register(Allftp)
class ArticleModel(admin.ModelAdmin):
    list_filter = ('companyName',)
@admin.register(Plan)
class ArticleModel(admin.ModelAdmin):
    list_filter = ('title',)
@admin.register(Question)
class ArticModel(admin.ModelAdmin):
    list_filter = ('questionText',)
@admin.register(Month)
class ArticModel(admin.ModelAdmin):
    list_filter = ('months',)
@admin.register(CustomUser)
class ArticleModel(admin.ModelAdmin):
    list_filter = ('username',)
@admin.register(Files)
class ArticleModel(admin.ModelAdmin):
    list_filter = ('company_name',)
