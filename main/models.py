from django.db import models

# contact yani murojat yollovchining malumotlarini saqlash uchun yaratilindi 
class Forms(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=14)
    email = models.EmailField(null=True)
    text = models.TextField()
    is_checked = models.BooleanField(default=False)
    
    
    class Meta():
        verbose_name = "Murojat"
        verbose_name_plural = "Murojatlar"
    
# blog malumotlarini saqlash uchun 
class Blog(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='blog/')
    body = models.TextField()
    
    def __str__(self):
        return self.title

# korxona haqida malumotlarni yangilab turish uchun
class About(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='about/')
    body = models.TextField()
    
    def __str__(self):
        return self.title


class StaffImg(models.Model):
    img = models.ImageField(upload_to='staffimg/')
    
    
    
    
    
