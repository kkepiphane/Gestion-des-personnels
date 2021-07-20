from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name="login"),
    path('deconnexion/', views.logoutUser, name="deconnexion"),
    path('register', views.registerPage, name="register"),

    path('index/', views.accueil, name="index"),
    # Lien des personnels
    path('personnel/', views.createPersonnel, name="personnel"),
    path('update_Personnel/<personnel_id>/',
         views.updatePersonnel, name="update_personnel"),
    path('delete_personnel/<personnel_id>/',
         views.deletePersonnel, name="delete_personnel"),
    path('list_personnel/', views.list_personnel, name="list_personnel"),
    path('info_personnel/<personnel_id>/',
         views.infoPersonnel, name="info_personnel"),

    # lien des postes
    path('postes/', views.createPoste, name="postes"),
    path('update_poste/<poste_id>/',
         views.updatePoste, name="update_poste"),
    path('delete_poste/<poste_id>/',
         views.deletePoste, name="delete_poste"),
    path('liste_poste/', views.list_postes, name="liste_poste"),

    # lien des service
    path('service/', views.createService, name="service"),
    path('update_service/<service_id>/',
         views.updateService, name="update_service"),
    path('delete_service/<service_id>/',
         views.deleteService, name="delete_service"),
    path('list_service/', views.list_service, name="list_service"),

    # lien des recettes
    path('recette/', views.createRecette, name="recette"),
    path('update_recette/<recette_id>/',
         views.updateRecette, name="update_recette"),
    path('delete_recette/<recette_id>/',
         views.deleteRecette, name="delete_recette"),

    # lien des depenses
    path('depense/', views.createDepense, name="depense"),
    path('update_depense/<depense_id>/',
         views.updateDepense, name="update_depense"),
    path('delete_depense/<depense_id>/',
         views.deleteDepense, name="delete_depense"),

    # Ajout d'une photo
    path('add_image/', views.addImage, name="add_image"),
    path('update_image/<doc_id>/',
         views.updateImage, name="update_image"),
    path('delete_image/<doc_id>/',
         views.deleteImage, name="delete_image"),

    # Etat
    path('etat/', views.etat, name="etat"),
]
