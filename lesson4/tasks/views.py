from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create a global variable list with the tasks
#tasks = []

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")


# Create your views here.
def index(request):
    if "tasks" not in request.session: # Est-ce que c'est toujours une liste de tache dans cette session
        request.session["tasks"] = [] # Créer une liste vide pour cette session
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })


def add(request):
    if request.method == "POST": # On test si la method request est bien POST (Pour envoyer des données au serveur)
        form = NewTaskForm(request.POST) # Tous ce qui est écrit est gardé dans la variable form
        if form.is_valid(): #On vérifie si les données fournies dans form sont valides (est-ce ça respecte tous les pré-requis)
            task = form.cleaned_data["task"] #On recup la task dans la variable "task"
            request.session["tasks"] += [task] # On ajoute la task dans la liste des task
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })

    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
