from django.http import HttpResponse
from django.shortcuts import render
from mywebsite.models import signupform

def homepg(request):
    return render(request,'homepg.html')

def ananyapg(request):
    return render(request,'ananyapg.html')

def vaibhavpg(request):
    return render(request,'vaibhavpg.html')

def pravinpg(request):
    return render(request,'pravinpg.html')

def buzzinga(request):
    return render(request,'buzzinga.html')

def signupforms(request):
    if request.method=="POST":
        username = request.POST['username']
        email = request.POST['user_email']
        password = request.POST['user_password']
        print(username, email, password)
        print("data saved")
        signupform(username=username ,user_email=email, user_password=password).save()
        return render(request,'tileslide.html')
    else:
        return render(request,'signupforms.html')

def team(request):
    return render(request,'team.html')



def tictac(request):
    return render(request,'tictac.html')

def blogwrite(request):
    return render(request,'blogwrite.html')

def after(request):
    return render(request,'after.html')

def tileslide(request):
    return render(request,'tileslide.html')

def services(request):
    return render(request,'services.html')

def loginform(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['user_password']
        print(username, password)
        print("data saved")
        userinfo=signupform.objects.filter(username=username , user_password=password)
        if (userinfo):
            return render(request,'tileslide.html')
        else:
            raise forms.ValidationError()
            return render(request,'loginform.html')
        
    else:
        return render(request,'loginform.html')
    
def games(request):
        return render(request,'games.html')

    
def contact(request):
    return render(request,'contact.html')

def quiz(request):
    if request.method=="POST":
        communityname = request.POST['yourgroup']
        
    return render(request,'quiz.html')

def community(request):
    return render(request,'community.html')


def covidquiz(request):
    return render(request,'covidquiz.html')
   

def cause(request):
    return render(request,'cause.html')
   




