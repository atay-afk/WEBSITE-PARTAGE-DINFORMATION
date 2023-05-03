from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from  django.contrib.sessions.models import Session
from django.contrib.auth import authenticate,login,logout
from .forms import *
import datetime
from django.http import HttpResponseRedirect,HttpResponse
from .models import *
import csv
import xlwt

#Etudiant,Enseignant,Classe,Cours,Ressource,Filiere,Matiere,Module,Examen,Pfe,Salle


def redirectt(request):

    return redirect('sign')



def emploi_ens(request,classe):

    test = Classe.objects.filter(filiere_id = request.user.enseignant.filiere ).all()
    all_mat = Matiere.objects.filter(enseignant_id = request.user.enseignant.pk)
    #C=all_mat[0].nom_matiere
    all_matiere = []

    for x in all_mat:
        all_matiere.append(x.nom_matiere)


    print(all_matiere)
    A=test[0].nom_class
    B=test[1].nom_class

    if classe == test[0].nom_class:
        emploi = Emploi.objects.filter(classe = test[0] ).all()
        nom=test[0]
    if classe == test[1].nom_class:
        emploi = Emploi.objects.filter(classe = test[1] ).all()
        nom=test[1]
    filieree = Filiere.objects.get(pk = request.user.enseignant.filiere_id)

    return render(request,'emploi_ens.html',{'emploi': emploi,'nom': nom, 'A':A ,'B':B ,'all_matiere':all_matiere , 'filieree':filieree} )



#################################
def emploi(request):


    emploi = Emploi.objects.filter(classe = request.user.etudiant.classe ).all()
    classee = Classe.objects.get(pk = request.user.etudiant.classe_id)
    filieree = Filiere.objects.get(pk = classee.filiere_id)


    return render(request,'emploi.html',{'emploi': emploi,'classee':classee ,'filieree':filieree })

#################################
def matiere_info(request,name_mat):
    mat = Matiere.objects.get(nom_matiere = name_mat)

    return render(request,'matiere_info.html',{'mat': mat})


def matiere_ens_info(request,name_mat_ens):
    mat = Matiere.objects.get(nom_matiere = name_mat_ens)

    test = Classe.objects.filter(filiere_id = request.user.enseignant.filiere ).all()
    A=test[0].nom_class

    return render(request,'matiere_ens_info.html',{'mat': mat,'A':A})


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
                      return redirect('profile')
                           #return render(request, "profile.html")
                  if qui == tuple[1]:
                      return redirect('profil')
                           #return render(request, "profil.html")
    else:
      return render(request, "login.html")
######################################
def exam(request):
    classe=Classe.objects.get(pk = request.user.etudiant.classe_id )
    filiere = Filiere.objects.get(pk = classe.filiere_id)
    exam = Examen.objects.filter(classe_id=classe).all()
    all_matiere = []
    matiere = ""
    for x in exam:
        all_matiere.append(x.matiere.nom_matiere)
    all_mat = list(dict.fromkeys(all_matiere))
    if request.method == 'POST':
        mat = request.POST['mat']
        matiere = Matiere.objects.get(nom_matiere = mat)
        exam = Examen.objects.filter(matiere = matiere).all()

    return render(request,'exams.html',{'exam' : exam ,'classe':classe , 'filiere' : filiere , "all_mat" : all_mat ,"matiere" : matiere})



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
    if cne == request.user.etudiant.cne:
        Etudiant.objects.filter(cne=cne).update(email=email, tel=tel, nom=nom, prenom=prenom, cin=cin,
                                                   date_naissance=date_naiss,
                                                   sexe=sexe, lieu_naissance=lieu_naiss, cne=cne, photo=photo,
                                                   adr_act=adress, ville=ville)
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
    test = Classe.objects.filter(filiere_id = request.user.enseignant.filiere ).all()
    A=test[0].nom_class

    if request.method == 'POST':
        nom = request.POST["nom"]
        filiere = request.POST["n"]
        prenom = request.POST["prenom"]
        cin = request.POST["cin"]
        adress = request.POST["adress"]
        tel = request.POST["tel"]
        email = request.POST["email"]
        grade = request.POST["grade"]
        #if User.objects.filter(email=email).exists():
        if email == request.user.enseignant.email:
            if email == request.user.enseignant.email:
                  f = Filiere.objects.get(nom_filiere=filiere).pk
                  Enseignant.objects.filter(email=email).update(email=email, tel=tel, nom=nom, prenom=prenom, cin=cin,
                                                address_pro=adress, grade=grade, filiere_id=f)
            else:
                f = Filiere.objects.get(nom_filiere=filiere).pk
                ens=Enseignant.objects.create(email=email, tel=tel, nom=nom, prenom=prenom, cin=cin,
                                                              address_pro=adress, grade=grade, filiere_id=f)
                ens.save()


        return render(request, 'profil.html',{'A':A})
    fi = Filiere.objects.all()

    stu = {
        "f":fi,
        "A" : A
    }

    return render(request, 'profil.html' ,stu)

########################

def rc_ens(request):
    test = Classe.objects.filter(filiere_id = request.user.enseignant.filiere ).all()
    A=test[0].nom_class

    enseignant = request.user.enseignant.pk
    filiere = Filiere.objects.get(pk = request.user.enseignant.filiere_id)



    if request.method == 'POST':
        r = request.POST["r"]
        desc = request.POST["description"]
        matiere = request.POST["n"]
        classe= request.POST["c"]
        m= Matiere.objects.get(nom_matiere=matiere).pk
        c =Classe.objects.get(nom_class=classe).pk

        info = Ressource.objects.create(
         rc_fichier=r,
         matiere_id=m,
         enseignant_id=enseignant,
         filiere_id=filiere.pk,
         rc_desc=desc,
         classe_id=c
         )
        info.save()



    mat = Matiere.objects.filter(enseignant_id=enseignant).all()
    cls = Classe.objects.filter(filiere_id=filiere).all()



    return render(request, 'rc_ens.html',{"A":A , "mat":mat , "cls":cls})
#########################

def rc(request):
    classe = Classe.objects.get(pk = request.user.etudiant.classe_id )
    ressource = Ressource.objects.filter(classe_id = classe).all()
    all_matiere = []

    for x in ressource:
        all_matiere.append(x.matiere.nom_matiere)
    all_mat = list(dict.fromkeys(all_matiere))
    if request.method == 'POST':
        mat = request.POST['mat']
        matiere = Matiere.objects.get(nom_matiere = mat)
        ressource = Ressource.objects.filter(matiere = matiere).all()




    return render(request,'rc.html',{'ressource':ressource , 'all_mat':all_mat})

#####################
def ressource(request):
    test = Classe.objects.filter(filiere_id = request.user.enseignant.filiere ).all()
    A=test[0].nom_class

    all_mat = Matiere.objects.filter(enseignant_id = request.user.enseignant.id ).all()
    first = all_mat[0]
    print(first)
    filiere = Filiere.objects.get(pk = request.user.enseignant.filiere_id )
    ressource = Ressource.objects.filter(matiere = first).all()

    if request.method == 'POST':
        mat = request.POST['mat']
        matiere = Matiere.objects.get(nom_matiere = mat)
        ressource = Ressource.objects.filter(matiere = matiere).all()


    return render(request,'ressource.html',{'A':A , 'ressource':ressource , 'all_mat':all_mat})




def create_rc_ens(request):

    test = Classe.objects.filter(filiere_id = request.user.enseignant.filiere ).all()
    A=test[0].nom_class
    all_mat = Matiere.objects.filter(enseignant_id = request.user.enseignant.id ).all()
    classe = Classe.objects.filter(filiere_id = request.user.enseignant.filiere.id).all()

    form = CreateRcEns()
    if request.method == 'POST':
        form = CreateRcEns(request.POST  , request.FILES)
        if form.is_valid():
            print('hohoho')
            mat = request.POST['mat']
            clas = request.POST['clas']
            mati = Matiere.objects.get(nom_matiere = mat)
            classee = Classe.objects.get(nom_class = clas)
            fil = Filiere.objects.get(id = request.user.enseignant.filiere_id)
            enseignant = Enseignant.objects.get(id = request.user.enseignant.id)
            x = form.save(commit=False)
            x.matiere = mati
            x.enseignant = enseignant
            x.filiere = fil
            x.classe = classee
            x.save()
            return redirect('ressource' )



    return render(request,'create_rc_ens.html',{'form': form , "A":A ,  'all_mat' : all_mat , "classe" : classe})





def update_rc_ens(request,pk):
     test = Classe.objects.filter(filiere_id = request.user.enseignant.filiere ).all()
     A=test[0].nom_class
     all_mat = Matiere.objects.filter(enseignant_id = request.user.enseignant.id ).all()
     classe = Classe.objects.filter(filiere_id = request.user.enseignant.filiere.id).all()

     ressource = Ressource.objects.get(id=pk)
     form = CreateRcEns(instance = ressource)
     if request.method == 'POST':
         form  = CreateRcEns(request.POST, instance = ressource)
         if form.is_valid():
             print('hohoho')
             mat = request.POST['mat']
             clas = request.POST['clas']
             mati = Matiere.objects.get(nom_matiere = mat)
             classee = Classe.objects.get(nom_class = clas)
             fil = Filiere.objects.get(id = request.user.enseignant.filiere_id)
             enseignant = Enseignant.objects.get(id = request.user.enseignant.id)
             x = form.save(commit=False)
             x.matiere = mati
             x.enseignant = enseignant
             x.filiere = fil
             x.classe = classee
             x.save()
             return redirect('ressource' )



     return render(request,'create_rc_ens.html',{'form': form , "A":A ,  'all_mat' : all_mat , "classe" : classe})

def delete_rc_ens(request,pk):


    ressource = Ressource.objects.get(id=pk)
    ressource.delete()
    return redirect('ressource' )




################################################
def sjpfe(request):
    test = Classe.objects.filter(filiere_id = request.user.enseignant.filiere ).all()
    A=test[0].nom_class

    filiere = Filiere.objects.get(pk = request.user.enseignant.filiere_id)
    pfe = Pfe.objects.filter(filiere_id=filiere).all()
    all_ensei = []
    enseignant = ""
    for x in pfe:
        all_ensei.append(x.encadrant)
    all_ens = list(dict.fromkeys(all_ensei))
    if request.method == 'POST':
        ens = request.POST['ens']
        if ens == 'x':
            pfe = Pfe.objects.filter(encadrant = request.user.enseignant ).all()
            enseignant = ens
        else:
            enseignant = Enseignant.objects.get(nom = ens)
            pfe = Pfe.objects.filter(encadrant = enseignant).all()




    return render(request, 'sjpfe.html',{'pfe': pfe , 'A':A , "all_ens" : all_ens ,"enseignant" :enseignant })



def create_pfe_ens(request):

    test = Classe.objects.filter(filiere_id = request.user.enseignant.filiere ).all()
    A=test[0].nom_class

    form = CreatePfeEns()
    if request.method == 'POST':
        form = CreatePfeEns(request.POST  , request.FILES)
        if form.is_valid():
            print('hohoho')
            fil = Filiere.objects.get(id = request.user.enseignant.filiere_id)
            enseignant = Enseignant.objects.get(id = request.user.enseignant.id)
            x = form.save(commit=False)
            x.encadrant = enseignant
            x.filiere = fil
            x.save()
            return redirect('sjpfe' )



    return render(request,'create_pfe_ens.html',{'form': form , "A":A })





def update_pfe_ens(request,pk):
     test = Classe.objects.filter(filiere_id = request.user.enseignant.filiere ).all()
     A=test[0].nom_class

     pfe = Pfe.objects.get(id=pk)
     form = CreatePfeEns(instance = pfe)
     if request.method == 'POST':
         form  = CreatePfeEns(request.POST, instance = pfe)
         if form.is_valid():
             fil = Filiere.objects.get(id = request.user.enseignant.filiere_id)
             enseignant = Enseignant.objects.get(id = request.user.enseignant.id)
             x = form.save(commit=False)
             x.encadrant = enseignant
             x.filiere = fil
             x.save()
             return redirect('sjpfe' )



     return render(request,'create_pfe_ens.html',{'form': form , "A":A })

def delete_pfe_ens(request,pk):

     pfe = Pfe.objects.get(id=pk)
     pfe.delete()
     return redirect('sjpfe' )





################################################
def pfe_etd(request):
    filiere = Filiere.objects.get(pk = request.user.etudiant.classe.filiere_id )
    pfe = Pfe.objects.filter(filiere_id=filiere).all()
    all_ensei = []
    enseignant = ""
    for x in pfe:
        all_ensei.append(x.encadrant)
    all_ens = list(dict.fromkeys(all_ensei))
    if request.method == 'POST':
        ens = request.POST['ens']
        enseignant = Enseignant.objects.get(nom = ens)
        pfe = Pfe.objects.filter(encadrant = enseignant).all()




    return render(request,'pfe_etd.html',{'filiere':filiere , 'pfe':pfe , "all_ens": all_ens , "enseignant" : enseignant})


###########################################
# def pfe(request):
#     test = Classe.objects.filter(filiere_id = request.user.enseignant.filiere ).all()
#     A=test[0].nom_class
#
#     enseignant = request.user.enseignant.pk
#     filiere = Filiere.objects.get(pk = request.user.enseignant.filiere_id)
#     print(filiere.pk)
#
#     if request.method == 'POST':
#         sujet = request.POST["sujet"]
#         delai = request.POST["delai"]
#         cahier_charg = request.POST["cahier_charg"]
#         info = Pfe.objects.create(sujet=sujet, delai=delai, cahier_charg=cahier_charg, encadrant_id=enseignant,filiere_id=filiere.pk)
#         info.save()
#
#     return render(request, 'pfe.html',{'A':A})
###########################################

def cours(request):
    classe = Classe.objects.get(pk = request.user.etudiant.classe_id)
    filiere = Filiere.objects.get(pk = classe.filiere_id)
    print(filiere)

    cours = Cours.objects.filter(classe_id = classe).all()



    return render(request,'cours.html',{'cours':cours,'filiere':filiere , 'classe':classe })

#########################################
def logout(request):
    auth.logout(request)
    return redirect('/sign')
####################

def examen(request):
    test = Classe.objects.filter(filiere_id = request.user.enseignant.filiere ).all()
    A=test[0].nom_class

    filiere = Filiere.objects.get(pk = request.user.enseignant.filiere_id)

    exam = Examen.objects.filter(filiere_id=filiere).all()
    all_matiere = []
    matiere = ""
    for x in exam:
        all_matiere.append(x.matiere.nom_matiere)
    all_mat = list(dict.fromkeys(all_matiere))
    if request.method == 'POST':
        mat = request.POST['mat']
        if mat == 'x':
            exam = Examen.objects.filter(enseignant = request.user.enseignant ).all()
            matiere = mat
        else:
            matiere = Matiere.objects.get(nom_matiere = mat)
            exam = Examen.objects.filter(matiere = matiere).all()


    return render(request, 'examen.html', { 'exam' : exam , 'filiere':filiere , 'A':A , "all_mat" : all_mat ,"matiere" : matiere})




def create_examen_ens(request):

    test = Classe.objects.filter(filiere_id = request.user.enseignant.filiere ).all()
    A=test[0].nom_class
    all_mat = Matiere.objects.filter(enseignant_id = request.user.enseignant.id ).all()


    form = CreateExamEns()
    if request.method == 'POST':
        form = CreateExamEns(request.POST)
        if form.is_valid():
            print("hohoho")
            mat = request.POST['mat']
            mati = Matiere.objects.get(nom_matiere = mat)
            classee = Classe.objects.get(nom_class = mati.classe)
            fil = Filiere.objects.get(id = request.user.enseignant.filiere_id)
            print(mati)
            x = form.save(commit=False)
            x.matiere = mati
            x.filiere = fil
            x.enseignant = mati.enseignant
            x.classe = classee
            x.save()
            return redirect('examen' )



    return render(request,'create_examen_ens.html',{'form': form , "A":A , 'all_mat' : all_mat})





def update_examen_ens(request,pk):
     test = Classe.objects.filter(filiere_id = request.user.enseignant.filiere ).all()
     A=test[0].nom_class
     all_mat = Matiere.objects.filter(enseignant_id = request.user.enseignant.id ).all()
     classe = Classe.objects.filter(filiere_id = request.user.enseignant.filiere.id).all()



     exam = Examen.objects.get(id=pk)
     form = CreateExamEns(instance = exam)
     if request.method == 'POST':
         form  = CreateExamEns(request.POST, instance = exam)
         if form.is_valid():
             print("hohoho")
             mat = request.POST['mat']
             mati = Matiere.objects.get(nom_matiere = mat)
             classee = Classe.objects.get(nom_class = mati.classe)
             fil = Filiere.objects.get(id = request.user.enseignant.filiere_id)
             print(mati)
             x = form.save(commit=False)
             x.matiere = mati
             x.filiere = fil
             x.enseignant = mati.enseignant
             x.classe = classee
             x.save()
             return redirect('examen' )


     return render(request,'create_examen_ens.html',{'form': form , "A":A , 'all_mat' : all_mat})


def delete_examen_ens(request,pk):

     exam = Examen.objects.get(id=pk)
     exam.delete()
     return redirect('examen' )







#############################################

def cours_ens(request):
    test = Classe.objects.filter(filiere_id = request.user.enseignant.filiere ).all()
    A=test[0].nom_class

    filiere = Filiere.objects.get(pk = request.user.enseignant.filiere_id)

    cours = Cours.objects.filter(filiere_id = filiere).all()

    return render(request,'cour_ens.html',{'cours':cours,'filiere':filiere ,"A":A })



def create_cours_ens(request):

    test = Classe.objects.filter(filiere_id = request.user.enseignant.filiere ).all()
    A=test[0].nom_class
    all_mat = Matiere.objects.filter(enseignant_id = request.user.enseignant.id ).all()
    classe = Classe.objects.filter(filiere_id = request.user.enseignant.filiere.id).all()

    form = CreateCoursEns()
    if request.method == 'POST':
        form = CreateCoursEns(request.POST)
        if form.is_valid():
            clas = request.POST['clas']
            mat = request.POST['mat']
            mati = Matiere.objects.get(nom_matiere = mat)
            classee = Classe.objects.get(nom_class = clas)
            print(mati)
            x = form.save(commit=False)
            x.matiere = mati
            x.classe = classee
            x.save()
            return redirect('cour_ens' )



    return render(request,'create_cours_ens.html',{'form': form , "A":A , 'all_mat' : all_mat , "classe" : classe})


def update_cours_ens(request,pk):
     test = Classe.objects.filter(filiere_id = request.user.enseignant.filiere ).all()
     A=test[0].nom_class
     all_mat = Matiere.objects.filter(enseignant_id = request.user.enseignant.id ).all()
     classe = Classe.objects.filter(filiere_id = request.user.enseignant.filiere.id).all()


     cours = Cours.objects.get(id=pk)
     form = CreateCoursEns(instance = cours)
     if request.method == 'POST':
         form  = CreateCoursEns(request.POST, instance = cours)
         if form.is_valid():
             clas = request.POST['clas']
             mat = request.POST['mat']
             mati = Matiere.objects.get(nom_matiere = mat)
             classee = Classe.objects.get(nom_class = clas)
             print(mati)
             x = form.save(commit=False)
             x.matiere = mati
             x.classe = classee
             x.save()
             return redirect('cour_ens' )


     return render(request,'create_cours_ens.html',{'form': form , "A":A , 'all_mat' : all_mat , "classe" : classe})


def delete_cours_ens(request,pk):

     cours = Cours.objects.get(id=pk)
     cours.delete()
     return redirect('cour_ens' )






###############################
def useradmin(request):


    return render(request, 'useradmin.html')

############################



def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if request.user.is_superuser:
                return redirect('useradmin')




    return render(request,'userlogin.html')

####################################

def adminemploi(request,pk):

    classe= Classe.objects.all()
    emploi = Emploi.objects.filter(classe_id = pk).all()
    classee = Classe.objects.get(id = pk)

    if request.method == 'POST':
        c = request.POST["laclasse"]
        print(c)

        classee = Classe.objects.get(nom_class = c)
        empl = Emploi.objects.filter(classe_id = classee.pk).all()
        if len(empl) == 0:
            for i in range(20):
                cls = Emploi.objects.create( classe_id = classee.pk)
                cls.save()
        emploi = Emploi.objects.filter(classe_id = classee).all()

    return render(request,'adminemploi.html',{'emploi': emploi , "classe":classe, "classee":classee})

####################################
def update(request,pk):
    emploi = Emploi.objects.get(id = pk )
    form  = Emploiform(instance = emploi)
    if request.method == 'POST':
        form  = Emploiform(request.POST, instance = emploi)
        if form.is_valid():
            form.save()
            return redirect('adminemploi', pk=emploi.classe_id )


    return render(request ,'update.html' ,{"form" : form})


def delete(request,pk):

    Emploi.objects.filter(id = pk).update( matiere = None , cours_type = None , salle = None)
    emploi = Emploi.objects.get(id = pk )
    return redirect('adminemploi', pk=emploi.classe_id )

#####################################


def users(request):

    users = User.objects.all()

    return render(request,'users.html',{'users' : users})


def create_user(request):

    form = CreateUser()
    if request.method == 'POST':
        form  = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users' )



    return render(request,'create_user.html',{'form': form})

#########################################

def etudiant(request):

    etudiant = Etudiant.objects.all()

    return render(request,'etudiant.html',{'etudiant' : etudiant})


def create_etudiant(request):

    form = CreateUser()
    etudiant_form = CreateStudent()
    if request.method == 'POST':
        form  = CreateUser(request.POST)
        etudiant_form  = CreateStudent(request.POST)
        if form.is_valid() and etudiant_form.is_valid():
            user = form.save()
            etudiant = etudiant_form.save(commit=False)
            etudiant.user = user
            etudiant.save()
            return redirect('etudiant')


    return render(request,'create_etudiant.html',{'form': form , 'etudiant_form': etudiant_form})


def update_etudiant(request,pk):

    etudiant = Etudiant.objects.get(id=pk)
    form = CreateUser(instance = etudiant.user)
    etudiant_form = CreateStudent(instance = etudiant)
    if request.method == 'POST':
        form = CreateUser(request.POST, instance = etudiant.user)
        etudiant_form  = CreateStudent(request.POST, instance = etudiant)
        if form.is_valid() and etudiant_form.is_valid():
            user = form.save()
            etudiant = etudiant_form.save(commit=False)
            etudiant.user = user
            etudiant.save()
            return redirect('etudiant')



    return render(request,'create_etudiant.html',{'form': form , 'etudiant_form': etudiant_form})


def delete_etudiant(request,pk):

    etudiant = Etudiant.objects.get(id=pk)
    user = User.objects.get(id = etudiant.user_id)
    user.delete()
    return redirect('etudiant' )


#########################################

def enseignant(request):

    enseignant = Enseignant.objects.all()

    return render(request,'enseignant.html',{'enseignant' : enseignant})


def create_enseignant(request):

    form = CreateUser()
    enseignant_form = CreateTeacher()
    if request.method == 'POST':
        form  = CreateUser(request.POST)
        enseignant_form = CreateTeacher(request.POST)
        if form.is_valid() and enseignant_form.is_valid():
            user = form.save()
            enseignant = enseignant_form.save(commit=False)
            enseignant.user = user
            enseignant.save()
            return redirect('enseignant')



    return render(request,'create_enseignant.html',{'form': form, 'enseignant_form': enseignant_form})


def update_enseignant(request,pk):

    enseignant = Enseignant.objects.get(id=pk)
    form = CreateUser(instance = enseignant.user)
    enseignant_form = CreateTeacher(instance = enseignant)
    if request.method == 'POST':
        form  = CreateUser(request.POST, instance = enseignant.user)
        enseignant_form = CreateTeacher(request.POST , instance = enseignant)
        if form.is_valid() and enseignant_form.is_valid():
            user = form.save()
            enseignant = enseignant_form.save(commit=False)
            enseignant.user = user
            enseignant.save()
            return redirect('enseignant' )



    return render(request,'create_enseignant.html',{'form': form ,'enseignant_form': enseignant_form})


def delete_enseignant(request,pk):

    enseignant = Enseignant.objects.get(id=pk)
    user = User.objects.get(id = enseignant.user_id)
    user.delete()
    return redirect('enseignant' )


#########################################

def filiere(request):

    filiere = Filiere.objects.all()

    return render(request,'filiere.html',{'filiere' : filiere})


def create_filiere(request):

    form = CreateFiliere()
    if request.method == 'POST':
        form  = CreateFiliere(request.POST)
        if form.is_valid():
            form.save()
            return redirect('filiere' )



    return render(request,'create_filiere.html',{'form': form})


def update_filiere(request,pk):

    filiere = Filiere.objects.get(id=pk)
    form = CreateFiliere(instance = filiere)
    if request.method == 'POST':
        form  = CreateFiliere(request.POST, instance = filiere)
        if form.is_valid():
            form.save()
            return redirect('filiere' )



    return render(request,'create_filiere.html',{'form': form})


def delete_filiere(request,pk):

    filiere = Filiere.objects.get(id=pk)
    filiere.delete()
    return redirect('filiere' )



########################################

def classe(request):

    classe = Classe.objects.all()

    return render(request,'classe.html',{'classe' : classe})


def create_classe(request):

    form = CreateClasse()
    if request.method == 'POST':
        form  = CreateClasse(request.POST)
        if form.is_valid():
            form.save()
            return redirect('classe' )



    return render(request,'create_classe.html',{'form': form})


def update_classe(request,pk):

    classe = Classe.objects.get(id=pk)
    form = CreateClasse(instance = classe)
    if request.method == 'POST':
        form  = CreateClasse(request.POST, instance = classe)
        if form.is_valid():
            form.save()
            return redirect('classe' )



    return render(request,'create_classe.html',{'form': form})


def delete_classe(request,pk):

    classe = Classe.objects.get(id=pk)
    classe.delete()
    return redirect('classe' )


########################################

def matiere(request):

    matiere = Matiere.objects.all()

    return render(request,'matiere.html',{'matiere' : matiere})


def create_matiere(request):

    form = CreateMatiere()
    if request.method == 'POST':
        form  = CreateMatiere(request.POST)
        if form.is_valid():
            form.save()
            return redirect('matiere' )



    return render(request,'create_matiere.html',{'form': form})


def update_matiere(request,pk):

    matiere = Matiere.objects.get(id=pk)
    form = CreateMatiere(instance = matiere)
    if request.method == 'POST':
        form  = CreateMatiere(request.POST, instance = matiere)
        if form.is_valid():
            form.save()
            return redirect('matiere' )



    return render(request,'create_matiere.html',{'form': form})


def delete_matiere(request,pk):

    matiere = Matiere.objects.get(id=pk)
    matiere.delete()
    return redirect('matiere' )


########################################

def module(request):

    module = Module.objects.all()

    return render(request,'module.html',{'module' : module})


def create_module(request):

    form = CreateModule()
    if request.method == 'POST':
        form  = CreateModule(request.POST)
        if form.is_valid():
            form.save()
            return redirect('module' )



    return render(request,'create_module.html',{'form': form})


def update_module(request,pk):

    module = Module.objects.get(id=pk)
    form = CreateModule(instance = module)
    if request.method == 'POST':
        form  = CreateModule(request.POST, instance = module)
        if form.is_valid():
            form.save()
            return redirect('module' )



    return render(request,'create_module.html',{'form': form})


def delete_module(request,pk):

    module = Module.objects.get(id=pk)
    module.delete()
    return redirect('module' )




########################################

def salle(request):

    salle = Salle.objects.all()

    return render(request,'salle.html',{'salle' : salle})


def create_salle(request):

    form = CreateSalle()
    if request.method == 'POST':
        form  = CreateSalle(request.POST)
        if form.is_valid():
            form.save()
            return redirect('salle' )



    return render(request,'create_salle.html',{'form': form})


def update_salle(request,pk):

    salle = Salle.objects.get(id=pk)
    form = CreateSalle(instance = salle)
    if request.method == 'POST':
        form  = CreateSalle(request.POST, instance = salle)
        if form.is_valid():
            form.save()
            return redirect('salle' )



    return render(request,'create_salle.html',{'form': form})


def delete_salle(request,pk):

    salle = Salle.objects.get(id=pk)
    salle.delete()
    return redirect('salle' )



########################################

def cours_admin(request):

    cours = Cours.objects.all()

    return render(request,'cours_admin.html',{'cours' : cours})


def create_cours(request):

    form = CreateCours()
    if request.method == 'POST':
        form  = CreateCours(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cours_admin' )



    return render(request,'create_cours.html',{'form': form})


def update_cours(request,pk):

    cours = Cours.objects.get(id=pk)
    form = CreateCours(instance = cours)
    if request.method == 'POST':
        form  = CreateCours(request.POST, instance = cours)
        if form.is_valid():
            form.save()
            return redirect('cours_admin' )



    return render(request,'create_cours.html',{'form': form})


def delete_cours(request,pk):

    cours = Cours.objects.get(id=pk)
    cours.delete()
    return redirect('cours_admin' )




########################################

def exam_admin(request):
    classe = Classe.objects.all()
    classee = classe[0]
    exam = Examen.objects.filter(classe = classe[0]).all()
    if request.method == 'POST':
        cls = request.POST['cls']
        classee = Classe.objects.get(nom_class = cls)
        exam = Examen.objects.filter(classe = classee).all()

    return render(request,'exam_admin.html',{'exam' : exam ,'classe':classe , 'classee': classee })


def create_exam(request,pk):
    matiere = Matiere.objects.filter(classe_id = pk).all()
    form = CreateExam()
    if request.method == 'POST':
        form  = CreateExam(request.POST)
        if form.is_valid():
            mat = request.POST['mat']
            matiere = Matiere.objects.get(nom_matiere = mat)
            classe = Classe.objects.get(id=pk)
            filiere = Filiere.objects.get(id = classe.filiere_id)
            x=form.save(commit= False)
            x.matiere = matiere
            x.enseignant = matiere.enseignant
            x.classe = classe
            x.filiere = filiere
            x.save()
            return redirect('exam_admin' )



    return render(request,'create_exam.html',{'form': form , 'matiere' : matiere})


def update_exam(request,pk,pk_up):
    matiere = Matiere.objects.filter(classe_id = pk).all()
    exam = Examen.objects.get(id=pk_up)
    form = CreateExam(instance = exam)
    if request.method == 'POST':
        form  = CreateExam(request.POST, instance = exam)
        if form.is_valid():
            mat = request.POST['mat']
            matiere = Matiere.objects.get(nom_matiere = mat)
            classe = Classe.objects.get(id=pk)
            filiere = Filiere.objects.get(id = classe.filiere_id)
            x=form.save(commit= False)
            x.matiere = matiere
            x.enseignant = matiere.enseignant
            x.classe = classe
            x.filiere = filiere
            x.save()
            return redirect('exam_admin' )


    return render(request,'create_exam.html',{'form': form , 'matiere' : matiere})


def delete_exam(request,pk):

        exam = Examen.objects.get(id=pk)
        exam.delete()
        return redirect('exam_admin' )


########################################

def pfe_admin(request):
    filiere = Filiere.objects.all()
    filieree=filiere[0]
    pfe = Pfe.objects.filter(filiere = filieree).all()
    if request.method == 'POST':
        fill = request.POST['fill']
        filieree = Filiere.objects.get(nom_filiere = fill)
        pfe = Pfe.objects.filter(filiere = filieree).all()


    return render(request,'pfe_admin.html',{'pfe' : pfe , "filiere": filiere , "filieree":filieree})


def create_pfe(request,pk):
    enseignant = Enseignant.objects.filter(filiere_id = pk).all()

    form = CreatePfe()
    if request.method == 'POST':
        form  = CreatePfe(request.POST ,  request.FILES)
        if form.is_valid():
            ens = request.POST['ens']
            ensei = Enseignant.objects.get(nom = ens)
            filiere = Filiere.objects.get(id = pk)

            x=form.save(commit =False)
            x.encadrant = ensei
            x.filiere = filiere
            x.save()
            return redirect('pfe_admin' )



    return render(request,'create_pfe.html',{'form': form , "enseignant" : enseignant})


def update_pfe(request,pk,pk_up):

    enseignant = Enseignant.objects.filter(filiere_id = pk).all()
    pfe = Pfe.objects.get(id=pk_up)
    form = CreatePfe(instance = pfe)
    if request.method == 'POST':
        form  = CreatePfe(request.POST, instance = pfe )
        if form.is_valid():
            ens = request.POST['ens']
            ensei = Enseignant.objects.get(nom = ens)
            filiere = Filiere.objects.get(id = pk)

            x=form.save(commit =False)
            x.encadrant = ensei
            x.filiere = filiere
            x.save()
            return redirect('pfe_admin' )



    return render(request,'create_pfe.html',{'form': form , "enseignant" : enseignant})


def delete_pfe(request,pk):

        pfe = Pfe.objects.get(id=pk)
        pfe.delete()
        return redirect('pfe_admin' )



################################
def ressource_admin(request):
    classe = Classe.objects.all()
    classee = classe[0]
    ressource = Ressource.objects.filter(classe = classe[0]).all()
    if request.method == 'POST':
        cls = request.POST['cls']
        classee = Classe.objects.get(nom_class = cls)
        ressource = Ressource.objects.filter(classe = classee).all()


    return render(request,'ressource_admin.html',{'ressource':ressource , 'classe':classe , 'classee': classee})




def create_ressource(request,pk):
    matiere = Matiere.objects.filter(classe_id = pk).all()
    form = CreateRcAdmin()
    if request.method == 'POST':
        form  = CreateRcAdmin(request.POST ,  request.FILES)
        if form.is_valid():
            mat = request.POST['mat']
            matiere = Matiere.objects.get(nom_matiere = mat)
            classe = Classe.objects.get(id=pk)
            filiere = Filiere.objects.get(id = classe.filiere_id)
            rc = form.save(commit =False)
            rc.matiere = matiere
            rc.classe = classe
            rc.filiere = filiere
            rc.save()
            return redirect('ressource_admin' )



    return render(request,'create_ressource.html',{'form': form , 'matiere' : matiere})



def update_ressource(request,pk,pk_up):
    matiere = Matiere.objects.filter(classe_id = pk).all()
    ressource = Ressource.objects.get(id = pk_up)
    form = CreateRcAdmin(instance = ressource)
    if request.method == 'POST':
        form  = CreateRcAdmin(request.POST ,instance = ressource )
        if form.is_valid():
            mat = request.POST['mat']
            matiere = Matiere.objects.get(nom_matiere = mat)
            classe = Classe.objects.get(id=pk)
            filiere = Filiere.objects.get(id = classe.filiere_id)
            rc = form.save(commit =False)
            rc.matiere = matiere
            rc.classe = classe
            rc.filiere = filiere
            rc.save()
            return redirect('ressource_admin' )



    return render(request,'create_ressource.html',{'form': form , 'matiere' : matiere})


def delete_ressource(request,pk):

        ressource = Ressource.objects.get(id=pk)
        ressource.delete()
        return redirect('ressource_admin' )

###############################







def upload_etudiant(request):
    classe = Classe.objects.all()
    form = UploadList()
    if request.method == 'POST':
        cls = request.POST['cls']
        classee = Classe.objects.get(nom_class = cls).id
        form = UploadList(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            obj = Csv.objects.get(activated=False)
            with open(obj.file_name.path , 'r') as x:
                reader = csv.reader(x)

                for i, row in enumerate(reader):
                    if i==0:
                        pass
                    else:
                        row = "".join(row)
                        row = row.replace(";"," ")
                        row = row.split()
                        name = row[0]
                        nom = row[1]
                        prenom = row[2]


                        user = User.objects.create_user(username=name,password=name)
                        Etudiant.objects.create(user = user , nom = nom , prenom = prenom , cne = name , classe_id = classee)




                obj.activated = True
                obj.save()
                return redirect('etudiant')


    return render(request, 'upload_etudiant.html',{"classe" : classe , "form" : form })







def upload_enseignant(request):
    filiere = Filiere.objects.all()
    form = UploadList()
    if request.method == 'POST':
        fill = request.POST['fill']
        filieree = Filiere.objects.get(nom_filiere = fill).id
        form = UploadList(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            obj = Csv.objects.get(activated=False)
            with open(obj.file_name.path , 'r') as x:
                reader = csv.reader(x)

                for i, row in enumerate(reader):
                    if i==0:
                        pass
                    else:
                        row = "".join(row)
                        row = row.replace(";"," ")
                        row = row.split()
                        name = row[0]
                        nom = row[1]
                        prenom = row[2]


                        user = User.objects.create_user(username=name,password=name)
                        Enseignant.objects.create(user = user , nom = nom , prenom = prenom , email = name ,filiere_id = filieree)




                obj.activated = True
                obj.save()
                return redirect('enseignant')


    return render(request, 'upload_enseignant.html',{"filiere" : filiere , "form" : form })



def export_etudiant(request):
    classe = Classe.objects.all()
    if request.method == 'POST':
        cls = request.POST['cls']
        classee = Classe.objects.get(nom_class = cls).id

        response=HttpResponse(content_type='application/ms-excel')
        response['content-Disposition'] = 'attachment; filename = Etudiants-' +\
            str(cls)+'.xls'
        wb = xlwt.Workbook(encoding='utf-8')
        ws=wb.add_sheet('Etudiants')
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['cne', 'nom','prenom']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num],font_style)

        font_style = xlwt.XFStyle()

        rows = Etudiant.objects.filter(classe_id = classee).values_list('cne','nom','prenom')

        for row in rows:
            row_num+=1

            for col_num in range(len(row)):
                ws.write(row_num, col_num, str(row[col_num]), font_style)
        wb.save(response)

        return response

    return render(request,'student-export.html', {"classe" : classe})







def export_enseignant(request):
    filiere = Filiere.objects.all()
    if request.method == 'POST':
        fill = request.POST['fill']
        filieree = Filiere.objects.get(nom_filiere = fill).id

        response=HttpResponse(content_type='application/ms-excel')
        response['content-Disposition'] = 'attachment; filename = Enseignants-' +\
            str(fill)+'.xls'
        wb = xlwt.Workbook(encoding='utf-8')
        ws=wb.add_sheet('Enseignants')
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['email', 'nom','prenom']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num],font_style)

        font_style = xlwt.XFStyle()

        rows = Enseignant.objects.filter(filiere_id = filieree).values_list('email','nom','prenom')

        for row in rows:
            row_num+=1

            for col_num in range(len(row)):
                ws.write(row_num, col_num, str(row[col_num]), font_style)
        wb.save(response)

        return response

    return render(request,'teacher-export.html', {"filiere" : filiere})







##############
