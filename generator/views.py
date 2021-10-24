from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request,'generator/home.html')




def password(request):

    
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.POST.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.POST.get('Special'):
        characters.extend(list('!@#$%^&*()'))

    if request.POST.get('numbers'):
        characters.extend(list('0123456789'))  

    #print("password-length-get",request.GET.get("password_length"))
    data = request.POST.get('password_length')
    #print(f"password-length-get{data}")

    lenght = int(request.POST.get('lenght',data))

    thepassword = ''

    for x in range(lenght):
        thepassword += random.choice(characters)


    return render(request,'generator/password.html', {'password':thepassword})