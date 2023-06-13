from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('vistamensual',views.calendar_view,name='calendar_view'),
    path('vistatrackers',views.vistatrackers,name='vistatrackers'),
    path('ayuda',views.ayuda,name='ayuda'),
    path('error404',views.error404,name='error404'),
    path('borrarTracker/<int:id>/', views.borrar_elemento_tracker, name='borrar_elemento_tracker'),
    path('borrarCumpleano/<int:id>/', views.borrar_elemento_cumpleano, name='borrar_elemento_cumpleano'),
    path('borrarTarea/<int:id>/', views.borrar_elemento_tarea, name='borrar_elemento_tarea'),
    path('borrarEvento/<int:id>/', views.borrar_elemento_evento, name='borrar_elemento_evento'),
    path('logout/', views.logout_view, name='logout'),
    path('actualizar-evento/', views.actualizar_evento, name='actualizar_evento'),

]