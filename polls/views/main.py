from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
from polls.models import *
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)

__all__ = (
    'index',
    'results',
)


def index(request, template='internal/index.html'):

    symptoms = Symptom.objects.all()
    levels = (
        (0, 'Bajo'),
        (1, 'Medio'),
        (2, 'Alto'),
    )
    context = {
        'symptoms': symptoms,
        'levels_symps':levels,
    }

    return render(request, template, context)



def results(request,symptoms_levels,template):
    foods = Food.objects.all()
    i=symptoms_levels
    context = {
        'foods':foods,
        'portions': portions
    }
    return render(request, template, context)

