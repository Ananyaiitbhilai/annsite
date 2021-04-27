from django.http import HttpResponse
from django.shortcuts import render

from mywebsite.models import mywebsite_signupform
from mywebsite.models import communities
from mywebsite.models import cquiz
import sys
from subprocess import run,PIPE

def homepg(request):
    request.session['sname'] = ''
    request.session['spassword'] = ''
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
        request.session['sname'] = username
        request.session['spassword'] = password
        
        
       mywebsite_signupform(username=username ,user_email=email, user_password=password).save()
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
        request.session['sname'] = username
        request.session['spassword'] = password
        
        print("data saved")
        userinfo=mywebsite_signupform.objects.filter(username=username , user_password=password)
        if (userinfo):
            return render(request,'logintile.html')
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
        comm_assign = request.POST['yourgroup']
        susername=request.session.get('sname')
        print(comm_assign)
        print(susername)
       
        setcomm=signupform.objects.get(username=susername)
        
        print(setcomm.user_id)
        commrec = communities.objects.get(name=comm_assign)
        commid=commrec.comm_id
        setcomm.community=commid
        setcomm.save()
        print(commid)
        print(setcomm.community)
        if (commid==1):
            return render(request,'social.html')
        else:
            return render(request,'neon.html')
        
    else:
        return render(request,'quiz.html')

def community(request):
    return render(request,'community.html')


def covidquizt(request):
    if request.method=="POST":
        location = request.POST['location_1']
        name = request.POST['name_1']
        age = request.POST['age_1']
        gender = request.POST['gender_1']
        print(name, location, age, gender)
        print("data saved")
        cquiz(name_1=name, age_1=age, location_1=location, gender_1=gender).save()
        return render(request,'covidquiz.html')
    else:
        return render(request,'covidquizt.html')
    
    
   


def cause(request):
    return render(request,'cause.html')

def social(request):
    return render(request,'social.html')

def neon(request):
    return render(request,'neon.html')
   
def Flappybird(request):
    return render(request,'Flappybird.html')
   
    
def covidquiz(request):
    return render(request,'covidquiz.html')

def err404(request):
    return render(request,'err404.html')

def logout(request):
    request.session['sname'] = ''
    request.session['spassword'] = ''
    try:
        del request.session['sname']
        del request.session['spassword']
    except:
         return render(request,'homepg.html')
    return render(request,'homepg.html')    

def logintile(request):
    return render(request,'logintile.html')

def pythontweet(request):
    return render(request,'pythontweet.html')

def twitter_home(request):
    return render(request,'twitter_home.html')


def external(request):
    inp= request.POST.get('tweet')
    out= run([sys.executable,'\\Users\\aruny\\mywebsite\\test.py',inp],shell=False,stdout=PIPE)
    print(out)
    return render(request,'pythontweet.html',{'data1':out.stdout})






