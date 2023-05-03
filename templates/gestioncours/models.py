
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import ModelForm


class Filiere(models.Model):
   nom_filiere = models.TextField()
   responsable = models.TextField()
   def __str__(self):
        return self.  nom_filiere

class Classe(models.Model):
  nom_class= models.TextField()
  delegue = models.TextField()
  filiere=models.ForeignKey(Filiere,on_delete=models.CASCADE)
  def __str__(self):
        return self.nom_class


class Module(models.Model):
    nom_module= models.TextField()
    porcentage = models.IntegerField()
    classe = models.ForeignKey(Classe , on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_module



class Enseignant(models.Model):
    user = models.OneToOneField(User, null=True ,on_delete = models.CASCADE)
    nom = models.CharField(max_length=60,default="null")
    prenom = models.CharField(max_length=60,default="null")
    cin = models.CharField(max_length=10,default="null")
    tel = models.IntegerField(default=0)
    email = models.CharField(max_length=25,default="null")
    grade = models.TextField(default="null")
    address_pro = models.TextField(default='null')
    filiere= models.ForeignKey(Filiere, on_delete=models.CASCADE,blank="true")
    def __str__(self):
        return self.nom


class Pfe(models.Model):
    sujet = models.CharField(max_length=50)
    cahier_charg = models.FileField(upload_to='file')
    delai = models.DateField(max_length=100)
    encadrant= models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE, blank="true")
    def __str__(self):
        return self.sujet




class Matiere(models.Model):
   nom_matiere = models.TextField(default="null")
   description =  models.TextField(default="null")
   module= models.ForeignKey(Module, on_delete=models.CASCADE)
   enseignant=models.ForeignKey(Enseignant, on_delete=models.CASCADE,blank="true")

   def __str__(self):
        return self.nom_matiere


class Salle(models.Model):
        type = (
        ( 'Amphi', 'Amphi'),
        ( 'Salle', 'Salle'),
        ( 'A','A'),
       )
        salle_type = models.CharField(max_length=20, choices=type, default='')
        num_salle=models.IntegerField()
        seance = models.TimeField(max_length=150)
        date = models.DateField(max_length=150)
        def __str__(self):
            return self.salle_type

class Cours(models.Model):
    cours = models.FileField(upload_to='file',blank='true')
    type = (
        ( 'CM', 'CM'),
        ( 'TD', 'TD'),
        ( 'TP','TP'),
       )
    cours_type = models.CharField(max_length=20, choices=type, default='')
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE,blank='true')
    groupe=models.CharField(max_length=20,  blank="true")
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE,blank='true')

    def __str__(self):
        return self.cours_type


class Etudiant(models.Model):
    user = models.OneToOneField(User, null=True ,on_delete = models.CASCADE)
    nom = models.CharField(max_length=60,default="null")
    prenom = models.CharField(max_length=60,default="null")
    cin = models.CharField(max_length=10,default="null")
    tel = models.IntegerField(default=0)
    email = models.CharField(max_length=25,default="null")
    cne = models.CharField(max_length=10,default="null")
    date_naissance = models.DateField(blank='True')
    lieu_naissance = models.CharField(max_length=25,default="null")
    adr_act = models.CharField(max_length=50,default="null")
    sexe = models.CharField(max_length=15,default="null")
    ville = models.CharField(max_length=25,default="null")
    photo = models.ImageField(upload_to='file',blank='True')
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    def __str__(self):
        return self.cne



class Examen(models.Model):
    matiere= models.ForeignKey(Matiere, on_delete=models.CASCADE)
    salle= models.ForeignKey(Salle, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)



class Ressource(models.Model):
    rc_fichier = models.FileField(upload_to='file')
    rc_desc= models.TextField(default="null",blank="true")
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE, blank="true")
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE, blank="true")
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, blank="true")

    def __str__(self):
        return self.rc_desc





class Emploi(models.Model):
    jour = models.CharField(max_length=20)
    A = models.CharField(max_length=100)
    B = models.CharField(max_length=100)
    C = models.CharField(max_length=100)
    D = models.CharField(max_length=100)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.name
