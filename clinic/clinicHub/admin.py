from django.contrib import admin
from .models import Departement, Person, Patient, Medecin, ProcessusSpecific, Rendez_Vous, Observation, DossierMedical

# Register models with the Django admin site
admin.site.register(Departement)
admin.site.register(Person)
admin.site.register(Patient)
admin.site.register(Medecin)
admin.site.register(ProcessusSpecific)
admin.site.register(Rendez_Vous)
admin.site.register(Observation)
admin.site.register(DossierMedical)
