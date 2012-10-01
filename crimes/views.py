from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from crimes.models import Crime
from django.template import Context, loader
from datetime import datetime


def index(request):
    latest_crimes = Crime.objects.all().order_by('date')[:5]
    t = loader.get_template('crimes/index.html')
    c = Context({
        'latest_crimes' : latest_crimes,
        })
    return HttpResponse(t.render(c))


def map(request):
    if not request.POST:
        summer = datetime(2012, 6, 1)
        crimes = prep_crimes(Crime.objects.all().filter(latitude__gte=41.78).filter(latitude__lte=41.80).filter(longitude__lte=-87.501).filter(longitude__gte=-87.607))
        c = {
            'crimes' : crimes,
            }
        c.update(csrf(request))
        return render_to_response('crimes/map.html', c)
    else:
        crimes = []
        if request.POST.get('hyde-park'):
            crimes = crimes + prep_crimes(Crime.objects.all().filter(latitude__gte=41.78).filter(latitude__lte=41.80).filter(longitude__lte=-87.501).filter(longitude__gte=-87.607))
        if request.POST.get('woodlawn'):
            crimes = crimes + prep_crimes(Crime.objects.all().filter(latitude__gte=41.773).filter(latitude__lte=41.800).filter(longitude__lte=-87.501).filter(longitude__gte=-87.607))
        if request.POST.get('kenwood'):
            crimes = crimes + prep_crimes(Crime.objects.all().filter(latitude__gte=41.80).filter(latitude__lte=41.816).filter(longitude__lte=-87.501).filter(longitude__gte=-87.607))
        if request.POST.get('wash-park'):
            crimes = crimes + prep_crimes(Crime.objects.all().filter(latitude__gte=41.78).filter(latitude__lte=41.802101).filter(longitude__lte=-87.607).filter(longitude__gte=-87.630))

        c = {
            'filter' : True,
            'crimes' : crimes,
            'time' : request.POST.get('time'),
            'max' : request.POST.get('max'),
            'radius' : request.POST.get('radius'),
            }
        c.update(csrf(request))
        return render_to_response('crimes/map.html', c)


def prep_crimes(model_crimes):
    crimes = []
    for model_crime in model_crimes:
        crime = { 
                'crime_type' : model_crime.crime_type,
                'case_num' : model_crime.case_num,
                'date' : model_crime.date,
                'latitude' : model_crime.latitude,
                'longitude' : model_crime.longitude,
                'description' : model_crime.description,
                }
        crimes.append(crime)
    return crimes
