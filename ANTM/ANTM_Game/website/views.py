from django.shortcuts import render, redirect
from .models import Contestants
from .forms import CycleForm
from django.forms import modelform_factory
import random

# ContForm = modelform_factory(Contestants, exclude=['name', 'age', 'hometown', 'elim'])

def redir_func(request, wordbank, id):
    if wordbank == 'False':
        wordbank = ''
    my_list =  [c.name for c in Contestants.objects.raw("select * from website_contestants where cycle = 'Cycle {}';".format(id))]
    random.shuffle(my_list)
    return render(request, 'website/redir.html', {"cyc_id":id, "wordbank":wordbank, "my_list":my_list})

# def index(request):
#     if request.method == 'POST':
#         form = ContForm(request.POST)
#         if form.is_valid():
#             cyc_id = form.cleaned_data['cycle']
#             return redirect('cycle/{0}'.format(cyc_id), {'cyc_id': cyc_id})
#         else:
#             return render(request, 'website/index.html', {"form":form})
#     else:
#         form = ContForm()
#         return render(request, 'website/index.html', {"form":form})

def index(request):
    context = {}
    if request.method == 'POST':
        form = CycleForm(request.POST)
        if form.is_valid():
            cyc_id = form.cleaned_data['cycle']
            wordbank = form.cleaned_data['wordbank']
            return redirect('cycle/{0}/{1}'.format(cyc_id, wordbank), {"cyc_id":cyc_id, "wordbank":wordbank})
        else:
            print('invalid')
            return render(request, 'website/index.html', {"form":form})
    else:
        form = CycleForm()
        return render(request, 'website/index.html', {"form":form})
