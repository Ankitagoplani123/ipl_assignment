from django.shortcuts import redirect, render
from ipl_app.models import *
from django.db.models import *
from .forms import TempForm


def homepage(request):
    match = matches.objects.all()
    data = match.values("season").annotate(count=Count("season"))
    context = {'data': data}

    data = data.filter(result='normal')
    context['data0'] = data.filter(winner__in=['Sunrisers Hyderabad', 'Deccan Chargers'])
    context['data1'] = data.filter(winner__in=['Rising Pune Supergiant', 'Pune Warriors', 'Rising Pune Supergiants'])
    context['data2'] = data.filter(winner__in=['Royal Challengers Bangalore'])
    context['data3'] = data.filter(winner__in=['Kolkata Knight Riders'])
    context['data4'] = data.filter(winner__in=['Kings XI Punjab'])
    context['data5'] = data.filter(winner__in=['Mumbai Indians'])
    context['data6'] = data.filter(winner__in=['Delhi Daredevils'])
    context['data7'] = data.filter(winner__in=['Gujarat Lions'])
    context['data8'] = data.filter(winner__in=['Chennai Super Kings'])
    context['data9'] = data.filter(winner__in=['Rajasthan Royals'])
    context['data10'] = data.filter(winner__in=['Kochi Tuskers Kerala'])

    return render(request=request,
                  template_name='home.html',
                  context=context)


def extra_runs(request):
    if request.method == 'POST':
        form = TempForm(request.POST)
        if form.is_valid():
            form.save()
            year = form.cleaned_data.get('form')
            ids = matches.objects.filter(season=year).values('id').distinct()
            id_list = []
            for x in ids:
                id_list.append(x['id'])

            data = deliveries.objects.filter(match_id__in=id_list). \
                values('bowling_team').annotate(sum=Sum('extra_runs'))

            ins = temp_model.objects.filter(form=year).last()
            form = TempForm(instance=ins)
            temp_model.objects.all().delete()
            return render(request=request,
                          template_name='extra_runs.html', context={"form": form, "data": data})

    form = TempForm
    return render(request=request,
                  template_name='extra_runs.html', context={"form": form})
