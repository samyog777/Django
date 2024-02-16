from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

#It is global list so any body can see lists
# tasks = []


class NewTask(forms.Form):
    task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(label="priority", min_value=1, max_value=5)
# Create your views here.

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        # "tasks": tasks # for global list
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = NewTask(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            # tasks.append(task) #if list is global
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return (request, "tasks/add.html", {
                "form": form
            })
        

    return render(request, "tasks/add.html", {
        "form": NewTask()
    })