from django.shortcuts import render

def index(request):
    return render(request, 'myadmin/index.html')


def show_user_form(request):
    return render(request, 'myadmin/add_user.html')

def show_event_form(request):
    return render(request, 'myadmin/add_event.html')

def show_squad_form(request):
    return render(request, 'myadmin/add_squad.html')

def show_camp_form(request):
    return render(request, 'myadmin/add_camp.html')
