from django.shortcuts import render
from .models import User
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')

def insert(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        mobile = request.POST['mobile']

        insert_data = User.objects.create(name=name, email=email, password=password, mobile=mobile)

        # insert_data.save()
        # return HttpResponse("Form Successfully Submitted...!")
        user_data = User.objects.all()
        dict = {
            "user_data" : user_data
        } 
        return render(request, 'show.html', dict)
def update(request):
    if request.method == 'POST':
        id = request.POST['id']
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        mobile = request.POST['mobile']

        insert_data = User.objects.get(id=id)

        insert_data.name = name
        insert_data.email = email
        insert_data.password = password
        insert_data.mobile = mobile

        insert_data.save()

        user_data = User.objects.all()
        dict = {
            "user_data" : user_data
        } 
        return render(request, 'show.html', dict)
    
def delete(request):
    if request.method == 'POST':
        id = request.POST['id']

        insert_data = User.objects.get(id=id)
        insert_data.delete()

        user_data = User.objects.all()
        dict = {
            "user_data" : user_data
        } 
        return render(request, 'show.html', dict)
    





