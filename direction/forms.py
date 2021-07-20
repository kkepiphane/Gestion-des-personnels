from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import datetime, date
from django import forms
from .models import *


class forms_DateInput(forms.DateInput):
    input_type = "date"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        # kwargs["format"] = '%d/%m/%Y'
        super().__init__(**kwargs)


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ('num_service', 'nom_service')
        widgets = {
            'num_service': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Num Service...'}),
            'nom_service': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom Service...'}),
        }


class PostForm(ModelForm):
    class Meta:
        model = Poste
        fields = ('type_service', 'num_post', 'nom_post')
        widgets = {
            'type_service': forms.Select(attrs={'class': 'form-select form-select-xl mb-3'}),
            'num_post': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Num Post...'}),
            'nom_post': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom Post...'}),
        }


class PersonneForm(forms.ModelForm):
    class Meta:
        SEXE_CHOICES = (
            ("Masculin", "Masculin"),
            ("Feminin", "Feminin"),
        )
        CONTRAT_CHOICES = (
            ("CDD", "CDD"),
            ("CDI", "CDI"),
        )
        SITUARION_CHOISE = (
            ("", "...Situation Matrimnial..."),
            ("Célibataire", "Célibataire"),
            ("Marie avec enfant", "Marie avec enfant"),
            ("Marie sans enfant", "Marie sans enfant")
        )
        model = Personnel
        fields = ('nom', 'prenom', 'date_naissance', 'sexe', 'email', 'telephone', 'adresse', 'nationalite', 'situation_matrimonial',
                  'nombre_enfant', 'contrat', 'date_debut', 'date_fin', 'personne_prevenir', 'telephone_prevenir', 'numero_bank', 'numero_cnss', 'personne_post')
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom...'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom...'}),
            'date_naissance': forms_DateInput(format=('%d-%m-%Y'), attrs={'class': 'myDateClass', 'placeholder': 'Select a date', 'class': 'form-control'}),
            'sexe': forms.RadioSelect(attrs={'class': 'form'}, choices=SEXE_CHOICES),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email@...'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone...'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresse...'}),
            'nationalite': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nationalité...'}),
            'situation_matrimonial': forms.Select(attrs={'class': 'form-select form-select-xl mb-3'}, choices=SITUARION_CHOISE),
            'nombre_enfant': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre enfant...'}),
            'contrat': forms.RadioSelect(attrs={'class': 'form'}, choices=CONTRAT_CHOICES),
            'date_debut': forms_DateInput(format=('%d-%m-%Y'), attrs={'class': 'datetimeshortcuts', 'placeholder': 'Select a date', 'class': 'form-control'}),
            'date_fin': forms_DateInput(format=('%d-%m-%Y'), attrs={'class': 'datetimeshortcuts', 'placeholder': 'Select a date', 'class': 'form-control'}),
            'personne_prevenir': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Personne à prevenir'}),
            'telephone_prevenir': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone personne à prevenir...'}),
            'numero_bank': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'numero_bank...'}),
            'numero_cnss': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'numero_cnss...'}),
            'personne_post': forms.Select(attrs={'class': 'form-select form-select-xl mb-3'}),
        }


class ImageForm(forms.ModelForm):
    class Meta:
        model = Doc
        fields = ('image', 'pdf', 'personne_profil')
        widgets = {
            'image': forms.ClearableFileInput(),
            'pdf': forms.ClearableFileInput(),
            'personne_profil': forms.Select(attrs={'class': 'form-select form-select-xl mb-3', 'placeholder': '...Selectioné nom du Personnel...'}),
        }


class RecetteForm(forms.ModelForm):
    class Meta:
        model = Recette
        fields = ('date_debut', 'date_fin', 'nc',
                  'ac', 'consulation', 'vente_pro', 'actes_soin', 'analyse', 'achats_pro', 'autre_pro', 'lunette', 'inam')
        widgets = {
            'date_debut': forms_DateInput(attrs={'class': 'datetimeshortcuts', 'placeholder': 'Select a date', 'class': 'form-control'}),
            'date_fin': forms_DateInput(attrs={'class': 'datetimeshortcuts', 'placeholder': 'Select a date', 'class': 'form-control'}),
            'nc': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'NC...'}),
            'ac': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'AC...'}),
            'consulation': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Consulation...'}),
            'vente_pro': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Vente Produit...'}),
            'actes_soin': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Actes Soins...'}),
            'analyse': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Analyse...'}),
            'achats_pro': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Achats Produits...'}),
            'autre_pro': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Autres Produits...'}),
            'lunette': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Lunette...'}),
            'inam': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Inam...'}),
        }


class DepenseForm(forms.ModelForm):
    class Meta:
        model = Depense
        fields = ('date_debut', 'date_fin', 'laboratoire',
                  'autre_achat', 'medicament', 'menage', 'deplacement', 'formation', 'salaire', 'cnss', 'telephone', 'entretien', 'ceet', 'papeterie')
        widgets = {
            'date_debut': forms_DateInput(format=('%d-%m-%Y'), attrs={'class': 'datetimeshortcuts', 'placeholder': 'Select a date', 'class': 'form-control'}),
            'date_fin': forms_DateInput(format=('%d-%m-%Y'), attrs={'class': 'datetimeshortcuts', 'placeholder': 'Select a date', 'class': 'form-control'}),
            'laboratoire': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Laboratoire...'}),
            'autre_achat': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Autre Achats...'}),
            'medicament': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Médicament...'}),
            'menage': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ménage...'}),
            'deplacement': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Deplacement...'}),
            'formation': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Formation...'}),
            'salaire': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Salaire...'}),
            'cnss': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'CNSS...'}),
            'telephone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone...'}),
            'entretien': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Entretien...'}),
            'ceet': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'CEET...'}),
            'papeterie': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Papeterie...'}),
        }


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
