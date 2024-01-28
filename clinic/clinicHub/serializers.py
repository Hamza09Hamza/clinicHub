# serializers.py in yourapp
from rest_framework import serializers
from .models import Departement, Person, Patient, Medecin, ProcessusSpecific, Rendez_Vous, Observation, DossierMedical

class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departement
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class MedecinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medecin
        fields = '__all__'

class ProcessusSpecificSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessusSpecific
        fields = '__all__'

class Rendez_VousSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rendez_Vous
        fields = '__all__'

class ObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observation
        fields = '__all__'

class DossierMedicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DossierMedical
        fields = '__all__'
