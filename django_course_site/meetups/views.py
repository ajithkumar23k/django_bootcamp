from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm
from .models import Meetup
# Create your views here.

def index(request):
    meetups =Meetup.objects.all()
    return  render( request,'meetups/index.html',{'meetups':meetups})


def meetup_details(request,meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registration_form=RegistrationForm()
            return render(request,'meetups/meetup-details.html',{
                'meetup_found':True,
                'meetup': selected_meetup,
                'form': registration_form
            })
        else:
            registration_form=RegistrationForm(request.POST)
            if registration_form.is_valid():
                participant=registration_form.save()
                selected_meetup.participants.add(participant)


    except Exception as exc:
        return render(request, 'meetups/meetup-details.html',{
            'meetup_found' : False})


