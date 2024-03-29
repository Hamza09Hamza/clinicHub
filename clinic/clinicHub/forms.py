from django import forms
from .models import Patient,Medecin,Rendez_Vous,DossierMedical,ProcessusSpecific,Observation,Departement

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        
        
class DoctorForm(forms.ModelForm):
    class Meta:
        model = Medecin
        fields = '__all__'
        
        
class Rendez_VousForm(forms.ModelForm):
    class Meta:
        model = Rendez_Vous
        fields = '__all__'

class DossierMedicalForm(forms.ModelForm):
    class Meta:
        model = DossierMedical
        fields = '__all__'

      # Disable the patient field for editing
    def clean(self):
        cleaned_data = super().clean()
        patient = cleaned_data.get('Patient')
        observations = cleaned_data.get('Observations')

        # Ensure that all observations belong to the selected patient's rendezvous
        for observation in observations.all():
            if observation.Rendez_Vous.Patient != patient:
                raise forms.ValidationError("Observations must belong to the selected patient's rendezvous.")

        return cleaned_data




class ProcessusSpecificForm(forms.ModelForm):
    class Meta:
        model = ProcessusSpecific
        fields = '__all__'


class ObservationForm(forms.ModelForm):
    class Meta:
        model = Observation
        fields = '__all__'
        


class DepartementForm(forms.ModelForm):
    class Meta:
        model = Departement
        fields = '__all__'
