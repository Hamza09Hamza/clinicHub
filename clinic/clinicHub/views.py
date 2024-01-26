from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PatientSerializer,MedecinSerializer,Rendez_VousSerializer,DossierMedicalSerializer,ProcessusSpecificSerializer,ObservationSerializer
from .models import Patient,Medecin,Rendez_Vous,DossierMedical,ProcessusSpecific
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

class ObservationView(viewsets.ModelViewSet):
    serializer_class = ObservationSerializer
    queryset = Rendez_Vous.objects.all()
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    def perform_create(self, serializer):
        serializer.save()
        
    def update(self, request, pk=None):
        Obs = self.get_object()
        serializer = self.get_serializer(Obs, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        Obs = self.get_object()
        serializer = self.get_serializer(Obs, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def perform_update(self, serializer):
        serializer.save()

class RendezVousView(viewsets.ModelViewSet):
    serializer_class = Rendez_VousSerializer
    queryset = Rendez_Vous.objects.all()
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    def perform_create(self, serializer):
        serializer.save()
        
    def update(self, request, pk=None):
        rdv = self.get_object()
        serializer = self.get_serializer(rdv, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        rdv = self.get_object()
        serializer = self.get_serializer(rdv, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def perform_update(self, serializer):
        serializer.save()


class DoctorView(viewsets.ModelViewSet):
    serializer_class = MedecinSerializer
    queryset = Medecin.objects.all()
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    def perform_create(self, serializer):
        serializer.save()
        
    def update(self, request, pk=None):
        doctor = self.get_object()
        serializer = self.get_serializer(doctor, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        doctor = self.get_object()
        serializer = self.get_serializer(doctor, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def perform_update(self, serializer):
        serializer.save()


class PatientView(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    def perform_create(self, serializer):
        serializer.save()
        
    def update(self, request, pk=None):
        patient = self.get_object()
        serializer = self.get_serializer(patient, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        patient = self.get_object()
        serializer = self.get_serializer(patient, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def perform_update(self, serializer):
        serializer.save()

class DossierMedicalView(viewsets.ModelViewSet):
    serializer_class = DossierMedicalSerializer
    queryset = DossierMedical.objects.all()
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    def perform_create(self, serializer):
        serializer.save()
        
    def update(self, request, pk=None):
        dm = self.get_object()
        serializer = self.get_serializer(dm, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        dm = self.get_object()
        serializer = self.get_serializer(dm, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def perform_update(self, serializer):
        serializer.save()

class ProcessusSpecificView(viewsets.ModelViewSet):
    serializer_class = ProcessusSpecificSerializer
    queryset = ProcessusSpecific.objects.all()
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    def perform_create(self, serializer):
        serializer.save()
        
    def update(self, request, pk=None):
        process = self.get_object()
        serializer = self.get_serializer(process, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        process = self.get_object()
        serializer = self.get_serializer(process, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def perform_update(self, serializer):
        serializer.save()
