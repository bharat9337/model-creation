from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.functions import Length
from django.db.models import Q

# Create your views here.
from app.models import *

def display_State(request):
    #QLSO=State.objects.all() 
    QLSO=State.objects.all().order_by('State_name')
    QLSO=State.objects.all().order_by(Length('Capital'))
    #QLSO=State.objects.filter(State_name__startswith="o")
   #QLSO=State.objects.filter(Q(State_name__startswith="K") & Q(Capital__startswith="B"))
    d={'State':QLSO}
    return render(request,'display_State.html',d)


def display_Capital(request):
   #QLCO=Capital.objects.all()
   QLCO=Capital.objects.all().order_by('-Cno')
   QLCO=Capital.objects.all().order_by(Length('Sname'))
   d={'Capital':QLCO}
   return render(request,'display_Capital.html',d)


def insert_state(request):
    sn=input("Enter State no::")
    s_name=input("Enter state name::")
    cn=input("Enter capital name::")
    NSO=State.objects.get_or_create(Sno=sn,State_name=s_name,Capital=cn)[0]
    NSO.save()
    return HttpResponse("state created successfully")




def update_State(request):
    State.objects.filter(State_name='Odisha').update(Capital='Bhadrak')
    QLSO=State.objects.all() 
    d={'State':QLSO}
    return render (request,'display_State.html',d)