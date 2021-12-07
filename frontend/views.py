from django.shortcuts import render
from django.views.generic import TemplateView
from core.models import *
from myapp.models import *


class IndexView(TemplateView):
    model = Mascot, Service
    template_name ='index.html'

    def get_context_data(self, **kwargs):       
        context = super(IndexView,self).get_context_data(**kwargs)
        context['title'] ='Mascota'
        context['title'] = 'Servicio'
        context['listMascota'] = Mascot.objects.all()
        context['listServicios'] = Service.objects.all()
        return context
