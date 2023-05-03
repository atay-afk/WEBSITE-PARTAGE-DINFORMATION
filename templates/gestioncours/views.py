from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from  django.contrib.sessions.models import Session

from django.http import HttpResponseRedirect

from .models import *

#Etudiant,Enseignant,Classe,Cours,Ressource,Filiere,Matiere,Module,Examen,Pfe,Salle



def teacher(request):
    test = Classe.objects.filter(filiere_id = request.user.enseignant.filiere ).all()

    A=test[0].nom_class

    return render(request,'teacher.html',{'A': A})


def emploi_ens(request,classe):

    test = Classe.objects.filter(filiere_id = request.user.enseignant.filiere ).all()

    A=test[0].nom_class
    B=test[1].nom_class

    if classe == test[0].nom_class:
        emploi = Emploi.objects.filter(classe = test[0] ).all()
        nom=test[0]
    if classe == test[1].nom_class:
        emploi = Emploi.objects.filter(classe = test[1] ).all()
        nom=test[1]

    return render(request,'emploi_ens.html',{'emploi': emploi,'nom': nom, 'A':A ,'B':B } )



#################################
def emploi(request):


    emploi = Emploi.objects.filter(classe = request.user.etudiant.classe ).all()

    return render(request,'emploi.html',{'emploi': emploi})

#################################
def matiere_info(request,name_mat):
    mat = Matiere.objects.get(nom_matiere = name_mat)

    return render(request,'matiere_info.html',{'mat': mat})


def matiere_ens_info(request,name_mat_ens):
    mat = Matiere.objects.get(nom_matiere = name_mat_ens)

    test = Classe.objects.filter(filiere_id = request.user.enseignant.filiere ).all()
    A=test[0].nom_class

    return render(request,'matiere_ens_info.html',{'mat': mat,'A':A})




################################
def table(request):
    return render(request, 'table.html')


#################################
def sign(request):
    if request.method == 'POST':
      email = request.POST['em']
      password = request.POST['pass']
      qui=request.POST['qui']
      tuple = ("1", "2")
      if User.objects.filter(username=email).exists():
              user = auth.authenticate(username=email, password=password)
              if user is not None:
                  auth.login(request, user)
                  if qui == tuple[0]:
                           return render(request, "profile.html")
                  if qui == tuple[1]:
                           return render(request, "profil.html")
    else:
      return render(request, "login.html")
######################################
def exam(request):
    current_user = request.user
    cne= current_user.username
    classe=Etudiant.objects.get(cne=cne).classe_id
    print(classe)
    tab_salle= []
    tab_matiere = []
    tab_module = []
    i = 0
    exam=Examen.objects.all().filter(classe_id=classe)
    for e in exam:
        tab_salle.append(1)
        tab_matiere.append(1)
        tab_module.append(1)
        tab_salle[i] =Salle.objects.get(id=e.salle_id)
        tab_matiere[i] =Matiere.objects.get(id=e.matiere_id)
        m = Matiere.objects.get(id=e.matiere_id).module_id
        tab_module[i] = Module.objects.get(id=m)
        i -= -1
    c=Classe.objects.get(id=classe).filiere_id
    v= Classe.objects.get(id=classe).nom_class
    f=Filiere.objects.get(id=c)
    tab = zip( tab_module,tab_matiere, tab_salle,exam )
    return render(request, 'exams.html', {'tab': tab,'f':f,'v':v})

#################################
def profile(request):
  if request.method == 'POST':
    nom = request.POST["nom"]
    prenom = request.POST["prenom"]
    date_naiss = request.POST["date_naiss"]
    sexe = request.POST["sexe"]
    lieu_naiss = request.POST["lieu_naiss"]
    cin = request.POST["cin"]
    cne = request.POST["cne"]
    photo = request.POST["photo"]
    adress = request.POST["adress"]
    ville = request.POST["ville"]
    tel = request.POST["tel"]
    email = request.POST["email"]
    classe = request.POST["classe"]
    if User.objects.filter(email=email).exists():
       if Etudiant.objects.filter(cne=cne).exists():
           clas = Classe.objects.get(nom_class=classe)
           Etudiant.objects.filter(cne=cne).update(email=email, tel=tel, nom=nom, prenom=prenom, cin=cin,
                                                   date_naissance=date_naiss,
                                                   sexe=sexe, lieu_naissance=lieu_naiss, cne=cne, photo=photo,
                                                   adr_act=adress, ville=ville, classe=clas)
       else:
           clas = Classe.objects.get(nom_class=classe)
           oct = Etudiant.objects.create(email=email, tel=tel, nom=nom, prenom=prenom, cin=cin,
                                       date_naissance=date_naiss, sexe=sexe, lieu_naissance=lieu_naiss,
                                         cne=cne, photo=photo, adr_act=adress, ville=ville, classe=clas)
           oct.save()

  fi = Classe.objects.all()
  stu = {
      "f": fi
  }
  return render(request, 'profile.html', stu)



###########################
def profil(request):
    if request.method == 'POST':
        nom = request.POST["nom"]
        filiere = request.POST["n"]
        prenom = request.POST["prenom"]
        cin = request.POST["cin"]
        adress = request.POST["adress"]
        tel = request.POST["tel"]
        email = request.POST["email"]
        grade = request.POST["grade"]
        if User.objects.filter(email=email).exists():
            if User.objects.filter(email=email).exists():
                  f = Filiere.objects.get(nom_filiere=filiere).pk
                  Enseignant.objects.filter(email=email).update(email=email, tel=tel, nom=nom, prenom=prenom, cin=cin,
                                                address_pro=adress, grade=grade, filiere_id=f)
            else:
                f = Filiere.objects.get(nom_filiere=filiere).pk
                ens=Enseignant.objects.create(email=email, tel=tel, nom=nom, prenom=prenom, cin=cin,
                                                              address_pro=adress, grade=grade, filiere_id=f)
                ens.save()


        return render(request, 'profil.html')
    fi = Filiere.objects.all()
    stu = {
        "f":fi
    }
    return render(request, 'profil.html',stu)

########################
def rc_ens(request):
    current_user = request.user
    emai = current_user.username
    e = Enseignant.objects.get(email=emai).pk
    f = Enseignant.objects.get(email=emai).filiere_id
    if request.method == 'POST':
        r = request.POST["r"]
        desc = request.POST["description"]
        matiere = request.POST["n"]
        classe= request.POST["c"]
        m= Matiere.objects.get(nom_matiere=matiere).pk
        c =Classe.objects.get(nom_class=classe).pk
        info = Ressource.objects.create(rc_fichier=r,  matiere_id=m,enseignant_id=e,filiere_id=f,  rc_desc=desc,classe_id=c)
        info.save()
    m = Matiere.objects.all().filter(enseignant_id=e)
    c= Classe.objects.all().filter(filiere_id=f)
    stu = {
        "m": m,
        "c": c
    }

    return render(request, 'rc_ens.html', stu)

##################
def rc(request):
    current_user = request.user
    emai = current_user.username
    print(emai)
    pk = Etudiant.objects.get(cne=emai).classe_id
    ressource = Ressource.objects.all().filter(classe_id=pk)
    tab_m = []
    i = 0
    for r in ressource:
        tab_m.append(1)
        tab_m[i] = Matiere.objects.get(id=r.matiere_id)
        i -= -1
    tab = zip(ressource, tab_m)
    return render(request, 'rc.html', {'tab': tab})
##################
def ressource(request):
    current_user = request.user
    emai= current_user.username
    e = Enseignant.objects.get(email=emai).pk
    tab_m = []
    i = 0
    ressource = Ressource.objects.all().filter(enseignant=e)
    for r in ressource:
        tab_m.append(1)
        tab_m[i] =Matiere.objects.get(id=r.matiere_id)
        i -= -1
    tab = zip(ressource, tab_m)
    return render(request, 'ressource.html', {'tab':tab})
#####################
def sjpfe(request):
    current_user = request.user
    emai= current_user.username
    print(emai)

    f=Enseignant.objects.get(email=emai).filiere_id
    tab_enc = []
    i = 0
    pfe = Pfe.objects.all().filter(filiere_id=f)
    for p in pfe:
        tab_enc.append(1)
        tab_enc[i] = Enseignant.objects.get(id=p.encadrant_id)

        i -= -1

    tab = zip(pfe,tab_enc)
    return render(request, 'sjpfe.html',{'tab': tab})

################################################

def pfe_etd(request):
    current_user = request.user
    emai= current_user.username
    print(emai)
    pk=Etudiant.objects.get(cne=emai).classe_id
    f=Classe.objects.get(id=pk).filiere_id
    tab_enc = []
    i = 0
    pfe = Pfe.objects.all().filter(filiere_id=f)
    for p in pfe:
        tab_enc.append(1)
        tab_enc[i] = Enseignant.objects.get(id=p.encadrant_id)

        i -= -1
    tab = zip(pfe,tab_enc)
    return render(request, 'pfe_etd.html',{'tab': tab})

################################################
def pfe(request):
    current_user = request.user
    emai= current_user.username
    print(emai)
    pk=Enseignant.objects.get(email=emai).pk
    f=Enseignant.objects.get(id=pk).filiere_id

    if request.method == 'POST':
        sujet = request.POST["sujet"]
        delai = request.POST["delai"]
        cahier_charg = request.POST["cahier_charg"]
        info = Pfe.objects.create(sujet=sujet, delai=delai, cahier_charg=cahier_charg, encadrant_id=pk,filiere_id=f)
        info.save()
    return render(request, 'pfe.html')

###########################################
def cours(request):
    current_user = request.user
    cne= current_user.username
    classe=Etudiant.objects.get(cne=cne).classe_id
    c=Classe.objects.get(id=classe)
    tab_salle= []
    tab_matiere = []
    tab_en = []
    tab_ens = []
    tab_module= []
    tab_filiere = []
    i = 0
    cour=Cours.objects.all().filter(classe_id=classe)
    for c in cour:
        tab_salle.append(1)

        tab_matiere.append(1)
        tab_ens.append(1)
        tab_module.append(1)
        tab_salle[i] =Salle.objects.get(id=c.salle_id)
        tab_matiere[i] =Matiere.objects.get(id=c.matiere_id)
        en=Matiere.objects.get(id=c.matiere_id).enseignant_id
        tab_ens[i] =Enseignant.objects.get(id=en)
        m = Matiere.objects.get(id=c.matiere_id).module_id
        tab_module[i] =Module.objects.get(id=m)
        print(en)
        i -= -1

    tab = zip(cour,tab_module, tab_matiere,tab_salle,tab_ens)
    c = Classe.objects.get(id=classe).filiere_id
    v = Classe.objects.get(id=classe).nom_class
    f = Filiere.objects.get(id=c)
    return render(request, 'cours.html', {'tab': tab,'f':f,'v':v})

#########################################
def logout(request):
    auth.logout(request)
    return redirect('/sign')
####################
def examen(request):
    current_user = request.user
    cne= current_user.username
    classe=Enseignant.objects.get(email=cne).filiere_id
    tab_salle= []
    tab_matiere = []
    tab_classe = []

    i = 0
    exam=Examen.objects.all().filter(filiere_id=classe)
    for e in exam:
        tab_salle.append(1)
        tab_matiere.append(1)
        tab_classe.append(1)
        tab_salle[i] =Salle.objects.get(id=e.salle_id)
        tab_matiere[i] =Matiere.objects.get(id=e.matiere_id)
        tab_classe[i] = Classe.objects.get(id=e.classe_id)
        i -= -1
    f = Filiere.objects.get(id=classe)
    tab = zip(tab_classe,tab_matiere, tab_salle,exam )
    return render(request, 'examen.html', {'tab': tab,'f':f})
#####################################
def cours_ens(request):
    current_user = request.user
    cne= current_user.username
    classe=Enseignant.objects.get(email=cne).filiere_id
    f = Filiere.objects.get(id=classe)
    tab_salle= []
    tab_matiere = []
    tab_en = []
    tab_ens = []
    tab_classe= []
    tab_filiere = []
    i = 0
    cour=Cours.objects.all().filter(filiere_id=classe)
    for c in cour:
        tab_classe.append(1)
        tab_salle.append(1)
        tab_matiere.append(1)
        tab_ens.append(1)
        tab_classe[i] = Classe.objects.get(id=c.classe_id)
        tab_salle[i] =Salle.objects.get(id=c.salle_id)
        tab_matiere[i] =Matiere.objects.get(id=c.matiere_id)
        en=Matiere.objects.get(id=c.matiere_id).enseignant_id
        tab_ens[i] =Enseignant.objects.get(id=en)

        print(en)
        i -= -1
    tab = zip(cour,tab_classe, tab_matiere,tab_salle,tab_ens)
    return render(request, 'cour_ens.html', {'tab': tab,'f':f})
