from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm



# class studentprofil(ModelForm):
#     class Meta:
#         model = Student
#         fields = ['classe']


class UploadList(ModelForm):
    class Meta:
        model = Csv
        fields = ['file_name']

        widgets = {
            'file_name' : forms.FileInput(attrs = {'class' : 'form-control'}),

        }




class Emploiform(ModelForm):
    class Meta:
        model = Emploi
        fields = ['matiere','cours_type','salle','enseignant']

        widgets = {
            'matiere' : forms.Select(attrs = {'class' : 'form-control'}),
            'cours_type' : forms.Select(attrs = {'class' : 'form-control'}),
            'salle' :  forms.Select(attrs = {'class' : 'form-control'}),
            'enseignant' :  forms.Select(attrs = {'class' : 'form-control'}),



        }

class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1', 'password2']

        widgets = {
            'username' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'password1' : forms.PasswordInput(attrs = {'class' : 'form-control'}),
            'password2' : forms.PasswordInput(attrs = {'class' : 'form-control'}),

        }


class CreateStudent(ModelForm):
    class Meta:
        model = Etudiant
        fields = ['classe']

        widgets = {

            'classe' : forms.Select(attrs = {'class' : 'form-control'}),

        }


class CreateTeacher(ModelForm):
    class Meta:
        model = Enseignant
        fields = ['filiere']

        widgets = {

            'filiere' : forms.Select(attrs = {'class' : 'form-control'}),

        }


class CreateFiliere(ModelForm):
    class Meta:
        model = Filiere
        fields = ['nom_filiere','responsable']

        widgets = {
            'nom_filiere' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'responsable' : forms.TextInput(attrs = {'class' : 'form-control'}),

        }



class CreateClasse(ModelForm):
    class Meta:
        model = Classe
        fields = ['nom_class','delegue','filiere']

        widgets = {
            'nom_class' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'delegue' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'filiere' : forms.Select(attrs = {'class' : 'form-control'}),

        }




class CreateMatiere(ModelForm):
    class Meta:
        model = Matiere
        fields = ['nom_matiere','description','module','enseignant','classe']

        widgets = {
            'nom_matiere' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'description' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'module' : forms.Select(attrs = {'class' : 'form-control'}),
            'enseignant' : forms.Select(attrs = {'class' : 'form-control'}),
            'classe' : forms.Select(attrs = {'class' : 'form-control'}),

        }



class CreateModule(ModelForm):
    class Meta:
        model = Module
        fields = ['nom_module','porcentage','classe']

        widgets = {
            'nom_module' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'porcentage' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'classe' : forms.Select(attrs = {'class' : 'form-control'}),

        }



class CreateSalle(ModelForm):
    class Meta:
        model = Salle
        fields = ['nom_salle']

        widgets = {
            'nom_salle' : forms.TextInput(attrs = {'class' : 'form-control'}),


        }


class CreateCours(ModelForm):
    class Meta:
        model = Cours
        fields = ['cours_type','matiere','salle','classe','groupe','filiere','seance','date']

        widgets = {

            'cours_type' : forms.Select(attrs = {'class' : 'form-control'}),
            'matiere' : forms.Select(attrs = {'class' : 'form-control'}),
            'salle' : forms.Select(attrs = {'class' : 'form-control'}),
            'classe' : forms.Select(attrs = {'class' : 'form-control'}),
            'groupe' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'filiere' : forms.Select(attrs = {'class' : 'form-control'}),
            'seance' : forms.TimeInput(attrs = {'class' : 'form-control'}),
            'date' : forms.DateInput(attrs = {'class' : 'form-control'}),


        }

class CreateCoursEns(ModelForm):
    class Meta:
        model = Cours
        fields = ['cours_type','salle','classe','groupe','filiere','seance','date']

        widgets = {

            'cours_type' : forms.Select(attrs = {'class' : 'form-control'}),
            'salle' : forms.Select(attrs = {'class' : 'form-control'}),
            'classe' : forms.Select(attrs = {'class' : 'form-control'}),
            'groupe' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'filiere' : forms.Select(attrs = {'class' : 'form-control'}),
            'seance' : forms.TimeInput(attrs = {'class' : 'form-control'}),
            'date' : forms.DateInput(attrs = {'class' : 'form-control'}),


        }



class CreateExam(ModelForm):
    class Meta:
        model = Examen
        fields = ['salle','seance','date','duree']

        widgets = {


            'salle' : forms.Select(attrs = {'class' : 'form-control'}),
            'duree' : forms.TextInput(attrs = {'class' : 'form-control'}),

            'seance' : forms.TimeInput(attrs = {'class' : 'form-control'}),
            'date' : forms.DateInput(attrs = {'class' : 'form-control'}),


        }


class CreateExamEns(ModelForm):
    class Meta:
        model = Examen
        fields = ['salle','seance','date','duree']

        widgets = {


            'salle' : forms.Select(attrs = {'class' : 'form-control'}),
            'duree' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'seance' : forms.TimeInput(attrs = {'class' : 'form-control'}),
            'date' : forms.DateInput(attrs = {'class' : 'form-control'}),


        }



class CreatePfe(ModelForm):
    class Meta:
        model = Pfe
        fields = ['sujet','cahier_charg','delai']

        widgets = {

            'sujet' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'cahier_charg' : forms.FileInput(attrs = {'class' : 'form-control'}),
            'delai' : forms.DateInput(attrs = {'class' : 'form-control'}),


        }




class CreatePfeEns(ModelForm):
    class Meta:
        model = Pfe
        fields = ['sujet','cahier_charg','delai']

        widgets = {

            'sujet' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'cahier_charg' : forms.FileInput(attrs = {'class' : 'form-control'}),
            'delai' : forms.DateInput(attrs = {'class' : 'form-control'}),


        }



class CreateRcEns(ModelForm):
    class Meta:
        model = Ressource
        fields = ['rc_fichier','rc_desc']

        widgets = {

            'rc_fichier' : forms.FileInput(attrs = {'class' : 'form-control'}),
            'rc_desc' : forms.TextInput(attrs = {'class' : 'form-control'}),



        }




class CreateRcAdmin(ModelForm):
    class Meta:
        model = Ressource
        fields = ['rc_fichier','rc_desc','enseignant']

        widgets = {

            'rc_fichier' : forms.FileInput(attrs = {'class' : 'form-control'}),
            'rc_desc' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'enseignant' : forms.Select(attrs = {'class' : 'form-control'}),



        }
