from django.shortcuts import render, redirect
import datetime
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Tracker, Evento, Tarea, Cumpleano
from .forms import TrackerForm, EventoForm, TareaForm, CumpleanoForm
from django.contrib.auth import logout
from datetime import date
import calendar

from django.shortcuts import get_object_or_404, redirect

# Create your views here.
def error404(request):
    return render(request,'calendario/error404.html')

def inicio(response):
    if not response.user.is_authenticated:
        return HttpResponseRedirect(reverse('error404'))
    
    evento = Evento.objects.filter(author_id=response.user.id)
    tarea = Tarea.objects.filter(author_id=response.user.id)
    cumpleano = Cumpleano.objects.filter(author_id=response.user.id)
    
    if response.method == "POST":
        form_evento = EventoForm(response.POST)
        form_tarea = TareaForm(response.POST)
        form_cumpleano = CumpleanoForm(response.POST)

        if form_evento.is_valid():
            titulo = form_evento.cleaned_data["title"]
            descripcion = form_evento.cleaned_data["description"]
            fecha = form_evento.cleaned_data["date"]
            hora = form_evento.cleaned_data["start_time"]
            t = Evento(title=titulo,description=descripcion, date=fecha, start_time=hora, author_id=response.user.id)
            t.save()

        if form_tarea.is_valid():
            titulo = form_tarea.cleaned_data["title"]
            descripcion = form_tarea.cleaned_data["description"]
            fecha = form_tarea.cleaned_data["exp_date"]
            prioridad = form_tarea.cleaned_data["priority"]
            t = Tarea(title=titulo,description=descripcion, exp_date=fecha, priority=prioridad, author_id=response.user.id)
            t.save()

        if form_cumpleano.is_valid():
            titulo = form_cumpleano.cleaned_data["name"]
            fecha = form_cumpleano.cleaned_data["date"]
            t = Cumpleano(name=titulo,date=fecha, author_id=response.user.id)
            t.save()

        return redirect(reverse('inicio'))

    else:
        form_evento = EventoForm()
        form_tarea = TareaForm()
        form_cumpleano = CumpleanoForm()
    
    fecha_actual0 = datetime.date.today()
    fecha_actual1 = datetime.date.today() + datetime.timedelta(days=1)
    fecha_actual2 = datetime.date.today() + datetime.timedelta(days=2)
    fecha_actual3 = datetime.date.today() + datetime.timedelta(days=3)
    fecha_actual4 = datetime.date.today() + datetime.timedelta(days=4)
    fecha_actual5 = datetime.date.today() + datetime.timedelta(days=5)
    fecha_actual6 = datetime.date.today() + datetime.timedelta(days=6)

    context = {
        'form_evento': form_evento,
        'form_tarea': form_tarea,
        'form_cumpleano': form_cumpleano,
        'evento': evento,
        'tarea': tarea,
        'cumpleano': cumpleano,
        'fecha_actual0': fecha_actual0,
        'fecha_actual1': fecha_actual1,
        'fecha_actual2': fecha_actual2,
        'fecha_actual3': fecha_actual3,
        'fecha_actual4': fecha_actual4,
        'fecha_actual5': fecha_actual5,
        'fecha_actual6': fecha_actual6,
    }
    # Resto de la lógica de la vista protegida
    return render(response, "calendario/index.html", context)

def ayuda(request):
    helpa = loader.get_template('calendario/ayuda.html')
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('error404'))
    # Resto de la lógica de la vista protegida
    return HttpResponse(helpa.render())

def vistamensual(request):
    mensual = loader.get_template('calendario/mensual.html')
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('error404'))
    # Resto de la lógica de la vista protegida
    return HttpResponse(mensual.render())

def vistatrackers(response):
    if not response.user.is_authenticated:
        return HttpResponseRedirect(reverse('error404'))
    
    trackers = Tracker.objects.filter(author_id=response.user.id)
    
    if response.method == "POST":
        form = TrackerForm(response.POST)
        if form.is_valid():
            titulo = form.cleaned_data["title"]
            nombreTrack = form.cleaned_data["track_name"]
            t = Tracker(title=titulo,track_name=nombreTrack, author_id=response.user.id)
            t.save()
        return redirect(reverse('vistatrackers'))
    else:
        form = TrackerForm()

    context = {
        'form': form,
        'trackers': trackers
    }
    # Resto de la lógica de la vista protegida
    return render(response, "calendario/trackers.html", context)

def actualizar_evento(response):
    if response.method == 'POST':
        evento_id = response.POST.get('evento_id')
        trackers = Tracker.objects.get(id_tracker=evento_id)
        if trackers.realizado == '0':
            trackers.realizado = '1'
        elif trackers.realizado == '1':
            trackers.realizado = '0'
        trackers.save()
        return JsonResponse({'message': 'Evento actualizado correctamente.'})
    return JsonResponse({'error': 'Solicitud no válida.'})

def borrar_elemento_tracker(request, id):
    elemento = get_object_or_404(Tracker, id_tracker=id)
    elemento.delete()
    return redirect(reverse('vistatrackers'))

def borrar_elemento_cumpleano(request, id):
    elemento = get_object_or_404(Cumpleano, id_bday=id)
    elemento.delete()
    return redirect(reverse('inicio'))

def borrar_elemento_tarea(request, id):
    elemento = get_object_or_404(Tarea, id_task=id)
    elemento.delete()
    return redirect(reverse('inicio'))

def borrar_elemento_evento(request, id):
    elemento = get_object_or_404(Evento, id_event=id)
    elemento.delete()
    return redirect(reverse('inicio'))

def logout_view(request):
    logout(request)
    return redirect('login')

def calendar_view(response):
    # Obtener el mes y el año actual
    today = date.today()
    current_month = today.month
    current_year = today.year

    # Obtener los eventos para el mes actual
    eventos = Evento.objects.filter(author_id=response.user.id)
    tareas = Tarea.objects.filter(author_id=response.user.id)
    cumpleanos = Cumpleano.objects.filter(author_id=response.user.id)

    # Generar la matriz del calendario
    calendar_matrix = calendar.monthcalendar(current_year, current_month)

    diaActual = datetime.date.today().day

    context = {
        'calendar_matrix': calendar_matrix,
        'eventos': eventos,
        'tareas': tareas,
        'cumpleanos': cumpleanos,
        'current_month': current_month,
        'current_year': current_year,
        'diaActual': diaActual, 
    }

    return render(response, "calendario/mensual.html", context)