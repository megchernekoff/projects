from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Contestants
from django.forms import modelform_factory
import random

ContForm = modelform_factory(Contestants, exclude=['name', 'age', 'hometown', 'elim'])

def redir_func(request, id):
    my_list =  [c.name for c in Contestants.objects.raw("select * from website_contestants where cycle = 'Cycle {}';".format(id))]
    random.shuffle(my_list)
    print(my_list)
    return render(request, 'website/redir.html', {"cyc_id":id, "my_list":my_list})

def index(request):
    if request.method == 'POST':
        form = ContForm(request.POST)
        if form.is_valid():
            cyc_id = form.cleaned_data['cycle']
            return redirect('cycle/{0}'.format(cyc_id), {'cyc_id': cyc_id})
        else:
            return render(request, 'website/index.html', {"form":form})
    else:
        form = ContForm()
        return render(request, 'website/index.html', {"form":form})
