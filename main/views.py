from django.shortcuts import render, redirect
from . import models


# asosiy sahifadagi malumotlar bilan ishlash uchun

def index(request):
    about = models.About.objects.all()
    context = {'about':about}
    return render(request, 'index.html', context)

# servislar sahifasini ishga tushurish
def service(request):
    context = {}
    return render(request, 'service.html', context)

# blog sahifasidagi malumotlarni chiqarish uchun
def blog(request):
    blog = models.Blog.objects.all()
    context ={"blog":blog}
    return render (request,'blog.html',context) 

# contact sahifasi orqali bazaga malumotlar qoshish uchun
def create_contact(request):
    if request.method == 'POST':
        models.Forms.objects.create(
            name = request.POST['name'],
            phone = request.POST['phone'],
            email = request.POST['email'],
            text = request.POST['text']
        )
        return redirect('index')
    return render(request, 'contact.html')


def staff_img(request):
    img = models.StaffImg.objects.all()
    return render(request, 'service.html', {'img':img})