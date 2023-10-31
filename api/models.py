
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


def upload_path(instance, filename):
    return "/".join( [filename])


class CustomUser(AbstractUser):
    group_name = models.CharField(max_length=50)
    bolge = models.CharField(max_length=70,  null=True, blank=True)




class Files(models.Model):
    id = models.AutoField(blank=False, primary_key=True)
    company_name =  models.CharField(max_length=500, default="None", null=True, blank=True)
    tmfb_belgesi = models.FileField(upload_to=upload_path, null=True, blank=True, default=None)
    yetki_belgesi = models.FileField(upload_to=upload_path, null=True, blank=True, default=None)
    yillik_rapor = models.FileField(upload_to=upload_path, null=True, blank=True, default=None)
    tml = models.FileField(upload_to=upload_path, null=True, blank=True, default=None)
    logo =  models.ImageField(blank=True, null=True, upload_to=upload_path, default=None)

class Month(models.Model):
    months = models.CharField(max_length=500,null=True,blank=True)   
    month_no= models.CharField(max_length=500,null=True,blank=True)   
    def __str__(self):
        return self.months
    
 

class Company(models.Model):
    id = models.AutoField(blank=False, primary_key=True)
    name = models.CharField(max_length=100)    
    user = models.ManyToManyField(CustomUser,  related_name='user',  blank=True)
    atama = models.ManyToManyField(CustomUser,  related_name='atama',  blank=True)
    firmauser = models.OneToOneField(CustomUser, on_delete=models.CASCADE,null=True,  blank=True)
    files = models.OneToOneField(Files, on_delete=models.CASCADE, null=True, blank=True)
    tmfb = models.CharField(max_length=500, null=True, blank=True)
    adres= models.CharField(max_length=500, null=True, blank=True)
    tmfbbit = models.CharField(max_length=500, null=True, blank=True)
    firmayet = models.CharField(max_length=500, null=True, blank=True)
    lokasyon=models.CharField(max_length=70,  null=True, blank=True)
    bolge = models.CharField(max_length=70,  null=True, blank=True)
    gonderen = models.BooleanField(null=True, blank=True, default=False)
    alici = models.BooleanField(null=True, blank=True, default=False)
    bosaltan = models.BooleanField(null=True, blank=True, default=False)
    yukleyen = models.BooleanField(null=True, blank=True, default=False)
    dolduran = models.BooleanField(null=True, blank=True, default=False)
    paketleyen = models.BooleanField(null=True, blank=True, default=False)
    tasimaci = models.BooleanField(null=True, blank=True, default=False)
    atik_alan = models.BooleanField(null=True, blank=True, default=False)
    gaz_tup = models.BooleanField(null=True, blank=True, default=False)
    stok_alan = models.BooleanField(null=True, blank=True, default=False)
    stok_tank = models.BooleanField(null=True, blank=True, default=False)
    paketleme = models.BooleanField(null=True, blank=True, default=False)
    tasima = models.BooleanField(null=True, blank=True, default=False)
    mainCategory= models.CharField(max_length=50, null=True, blank=True)
    # questions = models.ManyToManyField(Question,related_name="question", blank=True )


    def __str__ (self):
        return f" {self.name}"
    
   

 
class Question(models.Model):

    
    id = models.AutoField(blank=False, primary_key=True)
    company = models.ManyToManyField(Company, related_name="company",  blank=True)
    questionText =  models.CharField(max_length=500)
    answerA =  models.CharField(max_length=500)
    answerB =  models.CharField(max_length=500)
    answerC =  models.CharField(max_length=500)
    # answers =  models.ForeignKey(Answers,on_delete=models.CASCADE, null=True,blank=True)
    planAnswer =  models.CharField(max_length=500)
    currect =  models.CharField(max_length=500)
    currectAnswer =  models.CharField(max_length=500)
    unCurrectAnswer =  models.CharField(max_length=500)
    allYear = models.BooleanField(null=True, blank=True)
    subCategory =  models.CharField(max_length=500)
    spesificMonth = models.ManyToManyField(Month, related_name="month", blank=True)  
    
    def __str__ (self):
        return f" {self.questionText} "


class Answers(models.Model):
    company = models.CharField(max_length=500,null=True,blank=True)   
    takedAnswer = models.CharField(max_length=500,null=True,blank=True) 
    question = models.ForeignKey(Question,  on_delete=models.CASCADE)
    def __str__(self):
        return self.takedAnswer





class Allftp(models.Model):
    id = models.AutoField(blank=False, primary_key=True)
    companyName = models.CharField(max_length=500)
    tarih = models.DateField(auto_now_add=True)
    katilimci = models.CharField(max_length=500)
    cevapA = models.TextField(max_length=500)
    cevapB = models.TextField(max_length=500)
    author = models.ManyToManyField(CustomUser)
    onay = models.BooleanField(null=True, blank=True)

    def __str__ (self):
        return f" {self.companyName} {self.tarih}"


class Plan(models.Model):
    id = models.AutoField(blank=False, primary_key=True)
    title = models.CharField(max_length=500)
    start = models.CharField(max_length=500)
    end = models.CharField(max_length=500)
    author = models.ManyToManyField(CustomUser)
    ziyaretarih = models.CharField(max_length=500)
    allDay = models.BooleanField(null=True, blank=True)
    backgroundColor = models.CharField(max_length=500)
    desc = models.CharField(max_length=500, null=True, blank=True)
    companyName = models.CharField(max_length=500)
    
    






 

  
    

    
  