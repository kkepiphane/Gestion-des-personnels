from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from datetime import datetime, date
from .models import *
from .forms import *
from .filters import *

# Methode de connexion au compte


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            nom = request.POST.get('username')
            passwd = request.POST.get('password')

            user = authenticate(request, username=nom, password=passwd)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Nom ou Mot de passe incorrect')
        context = {}
        return render(request, 'directions/login.html', context)

# Methode de deconnexion


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = UserCreationForm()
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Le compte de ' +
                                 user+' est bien créer')
                return redirect('login')
        context = {'form': form}
        return render(request, 'directions/register.html', context)


#
# Accueils
#

@login_required(login_url='login')
def accueil(request):
    nbrePers = Personnel.objects.all()
    nbrePost = Poste.objects.all()
    nbreServ = Service.objects.all()

    totalPers = nbrePers.count()
    totalPost = nbrePost.count()
    totalServ = nbreServ.count()

    context = {'totalPers': totalPers,
               'totalPost': totalPost, 'totalServ': totalServ}
    return render(request, 'directions/index.html', context)


#
# Ajout, modification, supression et quelques methodes pour les personnels
#

@login_required(login_url='login')
def createPersonnel(request):
    submitted = False
    if request.method == 'POST':
        form = PersonneForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/personnel?submitted=True')
    else:
        form = PersonneForm
        if 'submitted' in request.GET:
            submitted = True
    context = {'form': form, 'submitted': submitted}
    return render(request, 'directions/personnel.html', context)

# Modification


@login_required(login_url='login')
def updatePersonnel(request, personnel_id):
    personnel = Personnel.objects.get(pk=personnel_id)
    form = PersonneForm(request.POST or None, instance=personnel)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('list_personnel')

    context = {'form': form, 'personnel': personnel}
    return render(request, 'directions/update_personnel.html', context)


@login_required(login_url='login')
def deletePersonnel(request, personnel_id):
    personnel = Personnel.objects.get(pk=personnel_id)
    personnel.delete()
    return redirect('list_personnel')


@login_required(login_url='login')
def list_personnel(request):
    if request.method == "POST":
        search = request.POST.get('recherche', False)
        personnel = Personnel.objects.filter(
            nom__contains=search).order_by('nom')
        context = {'personnel': personnel}
    else:
        personnel = Personnel.objects.all().order_by('nom')
        context = {'personnel': personnel}
    return render(request, 'directions/list_personnel.html', context)


@login_required(login_url='login')
def infoPersonnel(request, personnel_id):
    idPersonnel = Personnel.objects.get(id=personnel_id)
    idDoc = idPersonnel.doc_set.all()

    lirePost = Poste.objects.filter(nom_post=idPersonnel.personne_post)
    context = {'infosPersonnel': idPersonnel,
               'idDoc': idDoc, 'lirePost': lirePost}
    return render(request, 'directions/infoPersonnel.html', context)


#
# Ajout, modification, supression et quelques methodes pour les Services
#


@login_required(login_url='login')
def createService(request):
    submitted = False
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/service?submitted=True')
    else:
        form = ServiceForm
        if 'submitted' in request.GET:
            submitted = True
    context = {'form': form, 'submitted': submitted}
    return render(request, 'directions/service.html', context)


# Modification d'une information dans la base de données
@login_required(login_url='login')
def updateService(request, service_id):
    service = Service.objects.get(pk=service_id)
    form = ServiceForm(request.POST or None, instance=service)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('list_service')

    context = {'form': form, 'service': service}
    return render(request, 'directions/update_service.html', context)


# Suppression d'une Service
@login_required(login_url='login')
def deleteService(request, service_id):
    service = Service.objects.get(pk=service_id)
    service.delete()
    return redirect('list_service')


@login_required(login_url='login')
def list_service(request):
    if request.method == "POST":
        search = request.POST.get('recherche', False)
        services = Poste.objects.filter(
            nom_service__contains=search).order_by('nom_service')
    else:
        services = Poste.objects.all().order_by('nom_service')
    context = {'services': services}
    return render(request, 'directions/list_service.html', context)


#
# Ajout, modification, supression et quelques methodes pour les Posts
#

@login_required(login_url='login')
def createPoste(request):
    submitted = False
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/postes?submitted=True')
    else:
        form = PostForm
        if 'submitted' in request.GET:
            submitted = True
    context = {'form': form, 'submitted': submitted}
    return render(request, 'directions/post.html', context)

# Modification


@login_required(login_url='login')
def updatePoste(request, poste_id):
    poste = Poste.objects.get(pk=poste_id)
    form = PostForm(request.POST or None, instance=poste)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('liste_poste')

    context = {'form': form, 'poste': poste}
    return render(request, 'directions/update_poste.html', context)

# Suppression


@login_required(login_url='login')
def deletePoste(request, poste_id):
    poste = Poste.objects.get(pk=poste_id)
    poste.delete()
    return redirect('liste_poste')


@login_required(login_url='login')
def list_postes(request):
    if request.method == "POST":
        search = request.POST.get('recherche', False)
        posts = Poste.objects.filter(
            nom_post__contains=search).order_by('nom_post')
    else:
        posts = Poste.objects.all().order_by('nom_post')

    context = {'list_posts': posts}
    return render(request, 'directions/list_post.html', context)

#
# Ajout, modification, supression et quelques methodes pour les recettes
#


@login_required(login_url='login')
def createRecette(request):
    submitted = False
    if request.method == 'POST':
        form = RecetteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/recette?submitted=True')
    else:
        form = RecetteForm
        if 'submitted' in request.GET:
            submitted = True
    context = {'form': form, 'submitted': submitted}
    return render(request, 'directions/recette.html', context)

# Modification


@login_required(login_url='login')
def updateRecette(request, recette_id):
    recette = Recette.objects.get(pk=recette_id)
    form = RecetteForm(request.POST or None, instance=recette)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('list_recette')

    context = {'form': form, 'recette': recette}
    return render(request, 'directions/update_recette.html', context)
# suppression


@login_required(login_url='login')
def deleteRecette(request, recette_id):
    recette = Recette.objects.get(pk=recette_id)
    recette.delete()
    return redirect('list_recette')


#
# Ajout, modification, supression et quelques methodes pour les depenses
#


@login_required(login_url='login')
def createDepense(request):
    submitted = False
    if request.method == 'POST':
        form = DepenseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/depense?submitted=True')
    else:
        form = DepenseForm
        if 'submitted' in request.GET:
            submitted = True
    context = {'form': form, 'submitted': submitted}
    return render(request, 'directions/depense.html', context)

# Modification


@login_required(login_url='login')
def updateDepense(request, depense_id):
    depense = Depense.objects.get(pk=depense_id)
    form = DepenseForm(request.POST or None, instance=depense)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('list_depense')

    context = {'form': form, 'depense': depense}
    return render(request, 'directions/update_depense.html', context)

# suppression


@login_required(login_url='login')
def deleteDepense(request, depense_id):
    depense = Depense.objects.get(pk=depense_id)
    depense.delete()
    return redirect('list_depense')

#
# Ajout d'une Photo
#


@login_required(login_url='login')
def addImage(request):
    submitted = False
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_image?submitted=True')
    else:
        form = ImageForm
        if 'submitted' in request.GET:
            submitted = True
    listDoc = Doc.objects.all()
    context = {'form': form, 'submitted': submitted, 'listDoc': listDoc}
    return render(request, 'directions/add_image.html', context)


@login_required(login_url='login')
def updateImage(request, doc_id):
    img = Doc.objects.get(pk=doc_id)
    data_post = request.POST or None
    data_file = request.FILES or None
    form = ImageForm(data_post, data_file, instance=img)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('add_image')

    context = {'form': form, 'img': img}
    return render(request, 'directions/update_image.html', context)

# Suppression


@login_required(login_url='login')
def deleteImage(request, doc_id):
    img = Doc.objects.get(pk=doc_id)
    img.delete()
    return redirect('add_image')


@login_required(login_url='login')
def etat(request):
    listRectte = Recette.objects.all()
    listDepense = Depense.objects.all()
    filters = RecetteFilter(request.GET, queryset=listRectte)
    context = {'listRectte': listRectte,
               'listDepense': listDepense, 'filters': filters}
    return render(request, 'directions/etat.html', context)
