from django.shortcuts import render, redirect
from .models import Contestants, Results
from .forms import CycleForm
from django.forms import modelform_factory
import random
import json



def index(request):
    context = {}
    if request.method == 'POST':
        form = CycleForm(request.POST)
        if form.is_valid():
            cyc_id = form.cleaned_data['cycle']
            wordbank = form.cleaned_data['wordbank']
            return redirect('/cycle/{0}/{1}/'.format(cyc_id, wordbank), {"cyc_id":cyc_id, "wordbank":wordbank})
        else:
            print('invalid')
            return render(request, 'website/index.html', {"form":form})
    else:
        form = CycleForm()
        return render(request, 'website/index.html', {"form":form})


def redir_func(request, wordbank, id):
    if wordbank == 'False':
        wordbank = ''
    my_list_shuff =  [c.name for c in Contestants.objects.raw("select * from website_contestants where cycle = 'Cycle {}';".format(id))]
    my_list = my_list_shuff.copy()
    options_list = ['option{}'.format(num) for num in range(len(my_list))]
    random.shuffle(my_list_shuff)
    opt_list = zip(my_list, options_list)

    if request.method == 'POST':
        result_list = []
        for f in my_list:
            form = request.POST.get(f)
            member = Results(entry=form)
            member.save()
        print(Results.objects.all().values())
        return redirect('/results', {'my_list': my_list, 'options_list':options_list,
                                     'result_list':result_list})


    else:
        return render(request, 'website/redir.html', {"cyc_id":id, "wordbank":wordbank,
                                                      "opt_list": opt_list,
                                                      'my_list':my_list, "my_list_shuff":my_list_shuff,
                                                      'options_list':options_list})


def results_func(request):
    return render(request, 'website/results.html')
