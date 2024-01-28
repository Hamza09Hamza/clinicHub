from django.shortcuts import redirect, render,get_object_or_404
from rest_framework import viewsets
from django.views import View
from .forms import PatientForm,DoctorForm,DepartementForm,Rendez_VousForm,ObservationForm,DossierMedicalForm,ProcessusSpecificForm
from .serializers import PatientSerializer,MedecinSerializer,Rendez_VousSerializer,DossierMedicalSerializer,ProcessusSpecificSerializer,ObservationSerializer,DepartementSerializer
from .models import Patient,Medecin,Rendez_Vous,DossierMedical,ProcessusSpecific,Observation,Departement
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

class DepartementView(viewsets.ModelViewSet):
    serializer_class = DepartementSerializer
    queryset = Departement.objects.all()
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    def perform_create(self, serializer):
        serializer.save()
        
    def update(self, request, pk=None):
        Dep = self.get_object()
        serializer = self.get_serializer(Dep, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        Dep = self.get_object()
        serializer = self.get_serializer(Dep, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def perform_update(self, serializer):
        serializer.save()
        
        
class ObservationView(viewsets.ModelViewSet):
    serializer_class = ObservationSerializer
    queryset = Observation.objects.all()
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

class PatientCRUDView(View):
    def patient_list(request):
        template_list = 'patients/PatientList.html'
        patients = Patient.objects.all()
        return render(request, template_list, {'patients': patients})

    def patient_detail(request, pk):
        template_detail = 'patients/PatientDetails.html'
        patient = get_object_or_404(Patient, pk=pk)
        return render(request, template_detail, {'patient': patient})

    def create_patient(request):
        template_create = 'patients/PatientCreate.html'
        form = PatientForm()
        if request.method == 'POST':
            form = PatientForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('patients/PatientList')
        else:
            form = PatientForm()

        return render(request, template_create, {'form': form})

    def patient_update(request, pk):
        template_update = 'patients/PatientUpdate.html'
        patient = get_object_or_404(Patient, pk=pk)
        form = PatientForm(instance=patient)
        if request.method == 'POST':
            form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patients/PatientList')  
        else:
            form = PatientForm(instance=patient)
        return render(request, template_update, {'form': form, 'patient': patient})

    def patient_delete(request, pk):
        template_delete = 'patients/PatientDelete.html'
        patient = get_object_or_404(Patient, pk=pk)
        if request.method == 'POST':
            patient.delete()
            return redirect('patients/PatientList')  

        return render(request, template_delete, {'patient': patient})

class DoctorCRUDView(View):
    def doctor_list(request):
        template_list = 'Medecin/List.html'
        doctors = Medecin.objects.all()
        return render(request, template_list, {'doctors': doctors})

    def doctor_detail(request, pk):
        template_detail = 'Medecin/Details.html'
        doctor = get_object_or_404(Medecin, pk=pk)
        return render(request, template_detail, {'doctor': doctor})

    def create_doctor(request):
        template_create = 'Medecin/Create.html'
        form = DoctorForm()
        if request.method == 'POST':
            form = DoctorForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('doctor_list')
        else:
            form = DoctorForm()

        return render(request, template_create, {'form': form})

    def doctor_update(request, pk):
        template_update = 'Medecin/Update.html'
        doctor = get_object_or_404(Medecin, pk=pk)
        form = DoctorForm(instance=doctor)
        if request.method == 'POST':
            form = DoctorForm(request.POST, instance=doctor)
            if form.is_valid():
                form.save()
                return redirect('doctor_list')
        return render(request, template_update, {'form': form, 'doctor': doctor})

    def doctor_delete(request, pk):
        template_delete = 'Medecin/Delete.html'
        doctor = get_object_or_404(Medecin, pk=pk)
        if request.method == 'POST':
            doctor.delete()
            return redirect('doctor_list')
        return render(request, template_delete, {'doctor': doctor})
       
class DepartmentCRUDView(View):
    def department_list(request):
        template_list = 'departments/List.html'
        departments = Departement.objects.all()
        return render(request, template_list, {'departments': departments})

    def department_detail(request, pk):
        template_detail = 'departments/Details.html'
        department = get_object_or_404(Departement, pk=pk)
        return render(request, template_detail, {'department': department})

    def create_department(request):
        template_create = 'departments/Create.html'
        form = DepartementForm()
        if request.method == 'POST':
            form = DepartementForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('department_list')
        else:
            form = DepartementForm()

        return render(request, template_create, {'form': form})

    def department_update(request, pk):
        template_update = 'departments/Update.html'
        department = get_object_or_404(Departement, pk=pk)
        if request.method == 'POST':
            form = DepartementForm(request.POST, instance=department)
            if form.is_valid():
                form.save()
                return redirect('department_list')
        else:
            form = DepartementForm(instance=department)
        return render(request, template_update, {'form': form, 'department': department})

    def department_delete(request, pk):
        template_delete = 'departments/Delete.html'
        department = get_object_or_404(Departement, pk=pk)
        if request.method == 'POST':
            department.delete()
            return redirect('department_list')
        return render(request, template_delete, {'department': department})
    
class RendezVousCRUDView(View):
    def rendezvous_list(request):
        template_list = 'rendezvous/List.html'
        RendezVous = Rendez_Vous.objects.all()
        return render(request, template_list, {'RendezVous': RendezVous})

    def rendezvous_detail(request, pk):
        template_detail = 'rendezvous/Details.html'
        RendezVous = get_object_or_404(Rendez_Vous, pk=pk)
        return render(request, template_detail, {'RendezVous': RendezVous})

    def create_rendezvous(request):
        template_create = 'rendezvous/Create.html'
        form = Rendez_VousForm()
        if request.method == 'POST':
            form = Rendez_VousForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('rendezvous_list')
        else:
            form = Rendez_VousForm()

        return render(request, template_create, {'form': form})

    def rendezvous_update(request, pk):
        template_update = 'rendezvous/Update.html'
        RendezVous = get_object_or_404(Rendez_Vous, pk=pk)
        if request.method == 'POST':
            form = Rendez_VousForm(request.POST, instance=RendezVous)
            if form.is_valid():
                form.save()
                return redirect('rendezvous_list')
        else:
            form = Rendez_VousForm(instance=RendezVous)
        return render(request, template_update, {'form': form, 'RendezVous': RendezVous})


    def rendezvous_delete(request, pk):
        template_delete = 'rendezvous/Delete.html'
        RendezVous = get_object_or_404(Rendez_Vous, pk=pk)
        if request.method == 'POST':
            RendezVous.delete()
            return redirect('rendezvous_list')
        return render(request, template_delete, {'RendezVous': RendezVous})

class ObservationCRUDView(View):
    def observation_list(request):
        template_list = 'observations/List.html'
        observations = Observation.objects.all()
        return render(request, template_list, {'observations': observations})

    def observation_detail(request, pk):
        template_detail = 'observations/Details.html'
        observation = get_object_or_404(Observation, pk=pk)
        return render(request, template_detail, {'observation': observation})

    def create_observation(request):
        template_create = 'observations/Create.html'
        form = ObservationForm()
        if request.method == 'POST':
            form = ObservationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('observation_list')
        else:
            form = ObservationForm()

        return render(request, template_create, {'form': form})

    def observation_update(request, pk):
        template_update = 'observations/Update.html'
        observation = get_object_or_404(Observation, pk=pk)

        if request.method == 'POST':
            form = ObservationForm(request.POST, instance=observation)
            if form.is_valid():
                form.save()
                return redirect('observation_list')
        else:
            form = ObservationForm(instance=observation)

        return render(request, template_update, {'form': form, 'observation': observation})

    def observation_delete(request, pk):
        template_delete = 'observations/Delete.html'
        observation = get_object_or_404(Observation, pk=pk)
        if request.method == 'POST':
            observation.delete()
            return redirect('observation_list')
        return render(request, template_delete, {'observation': observation})    

class ProcessusSpecificCRUDView(View):

    def processusspecific_list(request):
        template_list = 'processusspecific/List.html'
        processusspecifics = ProcessusSpecific.objects.all()
        return render(request, template_list, {'processusspecifics': processusspecifics})

    def processusspecific_detail(request, pk):
        template_detail = 'processusspecific/Details.html'
        processusspecific = get_object_or_404(ProcessusSpecific, pk=pk)
        return render(request, template_detail, {'processusspecific': processusspecific})

    def create_processusspecific(request):
        template_create = 'processusspecific/Create.html'
        form = ProcessusSpecificForm()
        if request.method == 'POST':
            form = ProcessusSpecificForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('processusspecific_list')
        else:
            form = ProcessusSpecificForm()

        return render(request, template_create, {'form': form})

    def processusspecific_update(request, pk):
        template_update = 'processusspecific/Update.html'
        processusspecific = get_object_or_404(ProcessusSpecific, pk=pk)
        form = ProcessusSpecificForm(instance=processusspecific)
        if request.method == 'POST':
            form = ProcessusSpecificForm(request.POST, instance=processusspecific)
            if form.is_valid():
                form.save()
                return redirect('processusspecific_list')
        return render(request, template_update, {'form': form, 'processusspecific': processusspecific})

    def processusspecific_delete(request, pk):
        template_delete = 'processusspecific/Delete.html'
        processusspecific = get_object_or_404(ProcessusSpecific, pk=pk)
        if request.method == 'POST':
            processusspecific.delete()
            return redirect('processusspecific_list')
        return render(request, template_delete, {'processusspecific': processusspecific})

class DossierMedicalCRUDView(View):

    def dossiermedical_list(request):
        template_list = 'dossiermedical/List.html'
        dossiermedicals = DossierMedical.objects.all()
        return render(request, template_list, {'dossiermedicals': dossiermedicals})

    def dossiermedical_detail(request, pk):
        template_detail = 'dossiermedical/Details.html'
        dossiermedical = get_object_or_404(DossierMedical, pk=pk)
        return render(request, template_detail, {'dossiermedical': dossiermedical})

    def create_dossiermedical(request):
        form = DossierMedicalForm()
        if request.method == 'POST':
            form = DossierMedicalForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('dossiermedical_list')


        return render(request, 'dossiermedical/Create.html', {'form': form})



    def dossiermedical_update(request, pk):
        template_update = 'dossiermedical/Update.html'
        dossiermedical = get_object_or_404(DossierMedical, pk=pk)
        form = DossierMedicalForm(instance=dossiermedical)
        if request.method == 'POST':
            form = DossierMedicalForm(request.POST, instance=dossiermedical)
            if form.is_valid():
                form.save()
                return redirect('dossiermedical_list')
        return render(request, template_update, {'form': form, 'dossiermedical': dossiermedical})

    def dossiermedical_delete(request, pk):
        template_delete = 'dossiermedical/Delete.html'
        dossiermedical = get_object_or_404(DossierMedical, pk=pk)
        if request.method == 'POST':
            dossiermedical.delete()
            return redirect('dossiermedical_list')
        return render(request, template_delete, {'dossiermedical': dossiermedical})

def home(request):
    return render(request, 'home.html')

