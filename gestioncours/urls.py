from django.urls import path

from . import views

urlpatterns = (
    path('', views.redirectt, name="redirectt"),
    path('useradmin/student/upload/', views.upload_etudiant, name="upload_etudiant"),
    path('useradmin/teacher/upload/', views.upload_enseignant, name="upload_enseignant"),
    path('useradmin/student/export/', views.export_etudiant, name="export_etudiant"),
    path('useradmin/teacher/export/', views.export_enseignant, name="export_enseignant"),
    path('login/', views.userlogin, name="userlogin"),
    path('useradmin/', views.useradmin , name="useradmin"),
    path('useradmin/emploi/<pk>',views.adminemploi, name="adminemploi"),
    path('useradmin/emploi/update/<pk>/',views.update, name="update"),
    path('useradmin/emploi/delete/<pk>/',views.delete, name="delete"),
    path('useradmin/users/', views.users, name="users"),
    path('useradmin/users/create/', views.create_user, name="create_user"),
    path('useradmin/student/', views.etudiant, name="etudiant"),
    path('useradmin/student/create/', views.create_etudiant, name="create_etudiant"),
    path('useradmin/student/update/<pk>', views.update_etudiant, name="update_etudiant"),
    path('useradmin/student/delete/<pk>', views.delete_etudiant, name="delete_etudiant"),
    path('useradmin/teacher/', views.enseignant, name="enseignant"),
    path('useradmin/teacher/create/', views.create_enseignant, name="create_enseignant"),
    path('useradmin/teacher/update/<pk>', views.update_enseignant, name="update_enseignant"),
    path('useradmin/teacher/delete/<pk>', views.delete_enseignant, name="delete_enseignant"),
    path('useradmin/filiere/', views.filiere, name="filiere"),
    path('useradmin/filiere/create/', views.create_filiere, name="create_filiere"),
    path('useradmin/filiere/update/<pk>', views.update_filiere, name="update_filiere"),
    path('useradmin/filiere/delete/<pk>', views.delete_filiere, name="delete_filiere"),
    path('useradmin/classe/', views.classe, name="classe"),
    path('useradmin/classe/create/', views.create_classe, name="create_classe"),
    path('useradmin/classe/update/<pk>', views.update_classe, name="update_classe"),
    path('useradmin/classe/delete/<pk>', views.delete_classe, name="delete_classe"),
    path('useradmin/matiere/', views.matiere, name="matiere"),
    path('useradmin/matiere/create/', views.create_matiere, name="create_matiere"),
    path('useradmin/matiere/update/<pk>', views.update_matiere, name="update_matiere"),
    path('useradmin/matiere/delete/<pk>', views.delete_matiere, name="delete_matiere"),
        path('useradmin/module/', views.module, name="module"),
        path('useradmin/module/create/', views.create_module, name="create_module"),
        path('useradmin/module/update/<pk>', views.update_module, name="update_module"),
        path('useradmin/module/delete/<pk>', views.delete_module, name="delete_module"),
            path('useradmin/salle/', views.salle, name="salle"),
            path('useradmin/salle/create/', views.create_salle, name="create_salle"),
            path('useradmin/salle/update/<pk>', views.update_salle, name="update_salle"),
            path('useradmin/salle/delete/<pk>', views.delete_salle, name="delete_salle"),

    path('useradmin/cours/', views.cours_admin, name="cours_admin"),
    path('useradmin/cours/create/', views.create_cours, name="create_cours"),
    path('useradmin/cours/update/<pk>', views.update_cours, name="update_cours"),
    path('useradmin/cours/delete/<pk>', views.delete_cours, name="delete_cours"),


        path('useradmin/ressource/', views.ressource_admin, name="ressource_admin"),
        path('useradmin/ressource/create/<pk>', views.create_ressource, name="create_ressource"),
        path('useradmin/ressource/update/<pk>/<pk_up>/', views.update_ressource, name="update_ressource"),
        path('useradmin/ressource/delete/<pk>/', views.delete_ressource, name="delete_ressource"),


    path('useradmin/exam/', views.exam_admin, name="exam_admin"),
    path('useradmin/exam/create/<pk>', views.create_exam, name="create_exam"),
    path('useradmin/exam/update/<pk>/<pk_up>/', views.update_exam, name="update_exam"),
    path('useradmin/exam/delete/<pk>', views.delete_exam, name="delete_exam"),

    path('useradmin/pfe/', views.pfe_admin, name="pfe_admin"),
    path('useradmin/pfe/create/<pk>', views.create_pfe, name="create_pfe"),
    path('useradmin/pfe/update/<pk>/<pk_up>/', views.update_pfe, name="update_pfe"),
    path('useradmin/pfe/delete/<pk>', views.delete_pfe, name="delete_pfe"),


    path('emploi/', views.emploi, name="emploi"),
    path('emploi_ens/<classe>/',views.emploi_ens, name="emploi_ens"),
    path('emploi/<name_mat>/',views.matiere_info, name="matiere_info"),
    path('emploi_ens/<name_mat_ens>',views.matiere_ens_info, name="matiere_ens_info"),
    # path('table', views.table, name='table'),
    path('profile', views.profile, name='profile'),
    path('profil', views.profil, name='profil'),
    path('sign', views.sign, name='sign'),
    path('exam', views.exam, name='exam'),

    path('examen', views.examen, name='examen'),
    path('examen/create/', views.create_examen_ens, name="create_examen_ens"),
    path('examen/update/<pk>', views.update_examen_ens, name="update_examen_ens"),
    path('examen/delete/<pk>', views.delete_examen_ens, name="delete_examen_ens"),

    path('cours', views.cours, name='cours'),
    path('cour_ens', views.cours_ens, name='cour_ens'),
    path('cour_ens/create/', views.create_cours_ens, name="create_cours_ens"),
    path('cour_ens/update/<pk>', views.update_cours_ens, name="update_cours_ens"),
    path('cour_ens/delete/<pk>', views.delete_cours_ens, name="delete_cours_ens"),

    path('sjpfe', views.sjpfe, name='sjpfe'),
    path('sjpfe/create/', views.create_pfe_ens, name='pfe'),
    path('sjpfe/update/<pk>', views.update_pfe_ens, name='update_pfe_ens'),
    path('sjpfe/delete/<pk>', views.delete_pfe_ens, name='delete_pfe_ens'),

    path('rc', views.rc, name='rc'),
    path('pfe_etd', views.pfe_etd, name='pfe_etd'),

    path('ressource', views.ressource, name='ressource'),
    path('ressource/create/', views.create_rc_ens, name='rc_ens'),
    path('ressource/update/<pk>', views.update_rc_ens, name='update_rc_ens'),
    path('ressource/delete/<pk>', views.delete_rc_ens, name='delete_rc_ens'),




    path('logout', views.logout, name='logout'),

)
