from django.shortcuts import render, redirect
from .models import Contestants, Results
from .forms import CycleForm
from django.forms import modelform_factory
import random
import json
import sqlite3

def del_results():
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute("DELETE FROM website_results;")
    conn.commit()
    conn.close()


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
    del_results()
    if wordbank == 'False':
        wordbank = ''

    my_list_shuff =  [c.name for c in Contestants.objects.raw("select * from website_contestants where cycle = 'Cycle {}';".format(id))]
    my_list = my_list_shuff.copy()
    random.shuffle(my_list_shuff)

    if request.method == 'POST':
        result_list = []
        for f in my_list:
            form = request.POST.get(f)
            member = Results(entry=form)
            member.save()
        res_list = zip(Results.objects.all(), my_list)
        return render(request, 'website/results.html', {'results':res_list})

    else:
        options_list = ['option{}'.format(num) for num in range(len(my_list))]
        opt_list = zip(my_list, options_list)
        return render(request, 'website/redir.html', {"cyc_id":id, "wordbank":wordbank,
                                                      "opt_list": opt_list,
                                                      'my_list':my_list, "my_list_shuff":my_list_shuff,
                                                      'options_list':options_list})


# def results_func(request, res):
#     return render(request, 'website/results.html', res)
