from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from Base import models
from Base.models import Contact

# def home(request):
#     return render(request,'home.html')
def contact(request):
    if request.method=="POST":
        print('post')
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        content=request.POST.get('content')

        print(name,email,number,content)

        if len(name)>1 and len(name)<30:
            pass
        else:
            messages.error(request,'length of the name should be greater than 1 and less than 30')
            return render(request,'home.html')
        
        if len(email)>1 and len(email)<30:
            pass
        else:
            messages.error(request,'length of the email should be greater than 1 and less than 30')
            return render(request,'home.html')
        
        if len(number)>1 and len(number)<12:
            pass
        else:
            messages.error(request,'length of the number should be greater than 1 and less than 12')
            return render(request,'home.html')
        
        ins=models.Contact(name=name,email=email,number=number,content=content)

        ins.save()

        messages.success(request,'Thank you for contacting me || Your response has been saved')

        print('data has been saved into database')
    return render(request,'home.html')