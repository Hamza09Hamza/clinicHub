"""
URL configuration for clinic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from clinicHub import views


# Creating a router and registering viewsets
router = routers.DefaultRouter()
router.register(r'patients', views.PatientView, basename='patients')
router.register(r'doctors', views.DoctorView, basename='doctors')
router.register(r'rendezvous', views.RendezVousView, basename='rendezvous')
router.register(r'dossiermedical', views.DossierMedicalView, basename='dossiermedical')
router.register(r'processusspecific', views.ProcessusSpecificView, basename='processusspecific')

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
   
    path('patients/', views.PatientCRUDView.patient_list, name='PatientList'),
    path('patients/<int:pk>/', views.PatientCRUDView.patient_detail, name='PatientDetails'),
    path('patient/create/', views.PatientCRUDView.create_patient, name='PatientCreate'),
    path('patients/<int:pk>/update/', views.PatientCRUDView.patient_update, name='patient_update'),
    path('patients/<int:pk>/delete/', views.PatientCRUDView.patient_delete, name='patient_delete'),
    
    path('doctors/', views.DoctorCRUDView.doctor_list, name='doctor_list'),
    path('doctors/<int:pk>/', views.DoctorCRUDView.doctor_detail, name='doctor_detail'),
    path('doctor/create/', views.DoctorCRUDView.create_doctor, name='create_doctor'),
    path('doctors/<int:pk>/update/', views.DoctorCRUDView.doctor_update, name='doctor_update'),
    path('doctors/<int:pk>/delete/', views.DoctorCRUDView.doctor_delete, name='doctor_delete'),
    
    path('departments/', views.DepartmentCRUDView.department_list, name='department_list'),
    path('departments/<int:pk>/', views.DepartmentCRUDView.department_detail, name='department_detail'),
    path('department/create/', views.DepartmentCRUDView.create_department, name='create_department'),
    path('departments/<int:pk>/update/', views.DepartmentCRUDView.department_update, name='department_update'),
    path('departments/<int:pk>/delete/', views.DepartmentCRUDView.department_delete, name='department_delete'),
   
    path('rendezvous/', views.RendezVousCRUDView.rendezvous_list, name='rendezvous_list'),
    path('rendezvous/<int:pk>/', views.RendezVousCRUDView.rendezvous_detail, name='rendezvous_detail'),
    path('rendezvous/create/', views.RendezVousCRUDView.create_rendezvous, name='create_rendezvous'),
    path('rendezvous/<int:pk>/update/', views.RendezVousCRUDView.rendezvous_update, name='rendezvous_update'),
    path('rendezvous/<int:pk>/delete/', views.RendezVousCRUDView.rendezvous_delete, name='rendezvous_delete'),
    
    path('observations/', views.ObservationCRUDView.observation_list, name='observation_list'),
    path('observations/<int:pk>/', views.ObservationCRUDView.observation_detail, name='observation_detail'),
    path('observation/create/', views.ObservationCRUDView.create_observation, name='create_observation'),
    path('observations/<int:pk>/update/', views.ObservationCRUDView.observation_update, name='observation_update'),
    path('observations/<int:pk>/delete/', views.ObservationCRUDView.observation_delete, name='observation_delete'),

    path('processus_specifics/', views.ProcessusSpecificCRUDView.processusspecific_list, name='processusspecific_list'),
    path('processus_specifics/<int:pk>/', views.ProcessusSpecificCRUDView.processusspecific_detail, name='processusspecific_detail'),
    path('processus_specific/create/', views.ProcessusSpecificCRUDView.create_processusspecific, name='create_processusspecific'),
    path('processus_specifics/<int:pk>/update/', views.ProcessusSpecificCRUDView.processusspecific_update, name='processusspecific_update'),
    path('processus_specifics/<int:pk>/delete/', views.ProcessusSpecificCRUDView.processusspecific_delete, name='processusspecific_delete'),

    path('dossiermedical/', views.DossierMedicalCRUDView.dossiermedical_list, name='dossiermedical_list'),
    path('dossiermedical/<int:pk>/', views.DossierMedicalCRUDView.dossiermedical_detail, name='dossiermedical_detail'),
    path('dossiermedical/create/', views.DossierMedicalCRUDView.create_dossiermedical, name='create_dossiermedical'),
    path('dossiermedical/<int:pk>/update/', views.DossierMedicalCRUDView.dossiermedical_update, name='update_dossiermedical'),
    path('dossiermedical/<int:pk>/delete/', views.DossierMedicalCRUDView.dossiermedical_delete, name='delete_dossiermedical'),
]
