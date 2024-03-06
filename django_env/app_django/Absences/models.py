from django.db import models

# Create your models here.
class Etudiant(models.Model):
    nom=models.CharField()
    prenom=models.CharField()
    niveau=models.CharField()
class Cours(models.Model):
    nom=models.CharField()
    date=models.DateField()
    heure_debut=models.TimeField()
    heure_fin=models.TimeField()
class Absence(models.Model):
    etudiant=models.ForeignKey(Etudiant,on_delete=models.CASCADE)
    cours=models.ForeignKey(Cours,on_delete=models.CASCADE)
    justifiee=models.BooleanField(default=False)

    