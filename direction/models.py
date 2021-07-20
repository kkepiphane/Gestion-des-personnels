from django.db import models
from datetime import datetime, date
# Create your models here.


class Utilisateur(models.Model):
    nom = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    telephone = models.CharField(max_length=200, null=True)
    date_create = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nom


class Service(models.Model):
    num_service = models.CharField(max_length=200, null=True)
    nom_service = models.CharField(max_length=200, null=True)
    date_create = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nom_service


class Poste(models.Model):
    type_service = models.ForeignKey(
        Service, on_delete=models.SET_NULL, null=True, blank=True)
    num_post = models.CharField(max_length=200, null=True)
    nom_post = models.CharField(max_length=200, null=True)
    date_create = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nom_post


class Personnel(models.Model):
    nom = models.CharField(max_length=200, null=True)
    prenom = models.CharField(max_length=200, null=True)
    date_naissance = models.DateField(
        auto_now_add=False, auto_now=False, blank=True, null=True)
    sexe = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    telephone = models.CharField(max_length=200, null=True)
    adresse = models.CharField(max_length=200, null=True)
    nationalite = models.CharField(max_length=200, null=True)
    situation_matrimonial = models.CharField(max_length=200, null=True)
    nombre_enfant = models.IntegerField(blank=True, null=True)
    contrat = models.CharField(max_length=200, null=True)
    date_debut = models.DateField(
        auto_now_add=False, auto_now=False, blank=True, null=True)
    date_fin = models.DateField(
        auto_now_add=False, auto_now=False, blank=True, null=True)
    personne_prevenir = models.CharField(max_length=200, null=True)
    telephone_prevenir = models.CharField(max_length=200, null=True)
    numero_bank = models.CharField(max_length=200, null=True)
    numero_cnss = models.CharField(max_length=200, null=True)
    personne_post = models.ForeignKey(
        Poste, on_delete=models.SET_NULL, null=True, blank=True)
    date_create = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nom+' '+self.prenom


class Doc(models.Model):
    image = models.ImageField(null=True, blank=True)
    pdf = models.FileField(null=True, blank=True)
    # document_pers
    personne_profil = models.ForeignKey(
        Personnel, on_delete=models.SET_NULL, null=True, blank=True)
    date_create = models.DateTimeField(auto_now_add=True, null=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Recette(models.Model):
    date_debut = models.DateField(
        auto_now_add=False, auto_now=False, blank=True, null=True)
    date_fin = models.DateField(
        auto_now_add=False, auto_now=False, blank=True, null=True)
    nc = models.FloatField(blank=True, null=True)
    ac = models.FloatField(blank=True, null=True)
    consulation = models.FloatField(blank=True, null=True)
    vente_pro = models.FloatField(blank=True, null=True)
    actes_soin = models.FloatField(blank=True, null=True)
    analyse = models.FloatField(blank=True, null=True)
    achats_pro = models.FloatField(blank=True, null=True)
    autre_pro = models.FloatField(blank=True, null=True)
    lunette = models.FloatField(blank=True, null=True)
    inam = models.FloatField(blank=True, null=True)
    date_create = models.DateTimeField(auto_now_add=True, null=True)

    @property
    def total_rectte_sortie(self):
        totalRecette = sum(self.nc, self.ac, self.consulation,
                           self.vente_pro, self.actes_soin, self.analyse)
        return totalRecette

    @property
    def total_depense_sortie(self):
        depenseRecette = sum(self.achats_pro, self.autre_pro)
        return depenseRecette

    @property
    def depenseRecetteSortie(self):
        depenseSortie = (self.total_rectte_sortie - self.total_depense_sortie)
        return depenseSortie


class Depense(models.Model):
    date_debut = models.DateField(
        auto_now_add=False, auto_now=False, blank=True, null=True)
    date_fin = models.DateField(
        auto_now_add=False, auto_now=False, blank=True, null=True)
    laboratoire = models.FloatField(blank=True, null=True)
    autre_achat = models.FloatField(blank=True, null=True)
    medicament = models.FloatField(blank=True, null=True)
    menage = models.FloatField(blank=True, null=True)
    deplacement = models.FloatField(blank=True, null=True)
    formation = models.FloatField(blank=True, null=True)
    salaire = models.FloatField(blank=True, null=True)
    cnss = models.FloatField(blank=True, null=True)
    telephone = models.FloatField(blank=True, null=True)
    entretien = models.FloatField(blank=True, null=True)
    ceet = models.FloatField(blank=True, null=True)
    papeterie = models.FloatField(blank=True, null=True)
    date_create = models.DateTimeField(auto_now_add=True, null=True)

    @property
    def sommeDepense(self):
        somDepense = sum(self.laboratoire, self.autre_achat, self.medicament, self.menage, self.deplacement,
                         self.formation, self.salaire, self.cnss, self.telephone, self.entretien, self.ceet, self.papeterie)
        return somDepense
