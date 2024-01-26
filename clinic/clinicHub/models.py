from django.db import models
# Create your models here.

class Departement(models.Model):
    ID_Departement = models.AutoField(primary_key=True)
    NomDepartement = models.CharField(max_length=(50))
    def __str__(self):
        return  'Departement de '+self.NomDepartement

class Person(models.Model):
    ID_Person = models.AutoField(primary_key=True)
    Nom = models.CharField(max_length=(50))
    Prenom = models.CharField(max_length=(50))
    DateNaissance = models.DateField(default='2000-01-01')
    sexe = models.CharField(max_length=(50))
    Adresse = models.CharField(max_length=(50))
    num_tel = models.IntegerField(default=0)
    email = models.EmailField(default="test@domain.com")
    def __str__(self):
        return   self.Nom +' '+self.Prenom
        
class Patient(Person):
    ID_Patient = models.AutoField(primary_key=True)
    def __str__(self):
        return 'Patient '+self.Nom +' '+self.Prenom

    
class Medecin(Person):
    ID_Medecin= models.AutoField(primary_key=True)
    Departement = models.ForeignKey(Departement,on_delete=models.CASCADE)
    def __str__(self):
        return 'Dr.'+self.Nom +' '+self.Prenom



class ProcessusSpecific(models.Model):
    ID_Processus = models.AutoField(primary_key=True)
    Titre= models.CharField(max_length=(50))
    Description=models.CharField(max_length=(250))
    Departement = models.ForeignKey(Departement,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return 'Processus :'+self.Titre

    

class Rendez_Vous(models.Model):
    ID_RDV = models.AutoField(primary_key=True)
    Date = models.DateField(default='2000-01-01')
    Heure = models.TimeField(default='00:00:00')
    Patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    Medecin = models.ForeignKey(Medecin,on_delete=models.CASCADE)
    Titre = models.CharField(max_length=(50),default="Consultation")
    def __str__(self):
        return self.Titre +' du Patient: '+self.Patient.Nom+' avec Dr.'+self.Medecin.Nom
    
class Observation(models.Model):
        ID_Observation = models.AutoField(primary_key=True)
        Description=models.CharField(max_length=(50))
        Rendez_Vous = models.ForeignKey(Rendez_Vous, on_delete=models.CASCADE)
        def __str__(self):
            return ' Observation du Rendez_Vous: '+self.Rendez_Vous.Titre+' avec Dr.'+self.Rendez_Vous.Medecin.Nom
    
        
class DossierMedical(models.Model):
    ID_Dossier = models.AutoField(primary_key=True)
    Patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    DateCreation = models.DateField(auto_now_add=True, null=True, blank=True)
    Observations = models.ManyToManyField(Observation, blank=True)
    def __str__(self):
        return  'Dossier Medical du '+self.Patient.Nom +' '+self.Patient.Prenom

