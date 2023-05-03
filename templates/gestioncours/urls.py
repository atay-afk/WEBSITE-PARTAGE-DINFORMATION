from django.urls import path

from . import views

urlpatterns = (


    path('emploi/',views.emploi, name="emploi"),
    path('teacher/',views.teacher, name="teacher"),
    path('emploi_ens/<classe>/',views.emploi_ens, name="emploi_ens"),
    path('emploi/<name_mat>',views.matiere_info, name="matiere_info"),
    path('emploi_ens/<name_mat_ens>',views.matiere_ens_info, name="matiere_ens_info"),
    path('table', views.table, name='table'),
    path('profile', views.profile, name='profile'),
    path('profil', views.profil, name='profil'),
    path('sign', views.sign, name='sign'),
    path('exam', views.exam, name='exam'),
    path('examen', views.examen, name='examen'),
    path('cours', views.cours, name='cours'),
    path('cour_ens', views.cours_ens, name='cour_ens'),
    path('pfe', views.pfe, name='pfe'),
    path('sjpfe', views.sjpfe, name='sjpfe'),
    path('pfe_etd', views.pfe_etd, name='pfe_etd'),
    path('ressource', views.ressource, name='ressource'),
    path('rc', views.rc, name='rc'),
    path('rc_ens', views.rc_ens, name='rc_ens'),
    path('logout', views.logout, name='logout'),

)
