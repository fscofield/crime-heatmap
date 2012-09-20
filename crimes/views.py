from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from crimes.models import Crime
from django.template import Context, loader


def index(request):
    latest_crimes = Crime.objects.all().order_by('date')[:5]
    t = loader.get_template('crimes/index.html')
    c = Context({
        'latest_crimes' : latest_crimes,
        })
    return HttpResponse(t.render(c))


def map(request):
    if not request.POST:
        crimes_in_hydep =Crime.objects.all().filter(latitude__gte=41.78).filter(latitude__lte=41.80).filter(longitude__lte=-87.501).filter(longitude__gte=-87.607)
        c = {
            'crimes_in_hydep' : crimes_in_hydep,
            }
        c.update(csrf(request))
        return render_to_response('crimes/map.html', c)
    else:
        time = request.POST.get('time')
        crimes_in_hydep =Crime.objects.all().filter(latitude__gte=41.78).filter(latitude__lte=41.80).filter(longitude__lte=-87.501).filter(longitude__gte=-87.607)
        c = {
            'crimes_in_hydep' : crimes_in_hydep,
            }
        c.update(csrf(request))
        return render_to_response('crimes/map.html', c)


