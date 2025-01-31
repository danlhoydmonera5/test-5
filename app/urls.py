from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    HomePageView, AboutPageView, ContactPageView,
    PetListView, PetDetailView, PetCreateView, PetUpdateView, PetDeleteView,
    AdoptionApplicationListView, AdoptionApplicationDetailView, AdoptionApplicationCreateView,
    AdoptionApplicationUpdateView, AdoptionApplicationDeleteView,
    AdoptionEventListView, AdoptionEventDetailView, AdoptionEventCreateView, AdoptionEventUpdateView,
    AdoptionEventDeleteView, DonationListView, DonationDetailView, DonationCreateView, DonationUpdateView, DonationDeleteView,
)

urlpatterns = [

    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),


    path('pets/', PetListView.as_view(), name='pet_list'),
    path('pet/<int:pk>/', PetDetailView.as_view(), name='pet_detail'),
    path('pet/new/', PetCreateView.as_view(), name='pet_create'),
    path('pet/<int:pk>/edit/', PetUpdateView.as_view(), name='pet_update'),
    path('pet/<int:pk>/delete/', PetDeleteView.as_view(), name='pet_delete'),


    path('applications/', AdoptionApplicationListView.as_view(), name='adoption_application_list'),
    path('application/create/', AdoptionApplicationCreateView.as_view(), name='adoption_application_create'),
    path('applications/<int:pk>/', AdoptionApplicationDetailView.as_view(), name='adoption_application_detail'),
    path('applications/<int:pk>/edit/', AdoptionApplicationUpdateView.as_view(), name='adoption_application_update'),
    path('applications/<int:pk>/delete/', AdoptionApplicationDeleteView.as_view(), name='adoption_application_delete'),


    path('events/', AdoptionEventListView.as_view(), name='adoption_event_list'),
    path('event/<int:pk>/', AdoptionEventDetailView.as_view(), name='adoption_event_detail'),
    path('event/new/', AdoptionEventCreateView.as_view(), name='adoption_event_create'),
    path('event/<int:pk>/edit/', AdoptionEventUpdateView.as_view(), name='adoption_event_update'),
    path('event/<int:pk>/delete/', AdoptionEventDeleteView.as_view(), name='adoption_event_delete'),

    path('donations/', DonationListView.as_view(), name='donation_list'),
    path('donation/<int:pk>/', DonationDetailView.as_view(), name='donation_detail'),
    path('donation/new/', DonationCreateView.as_view(), name='donation_create'),
    path('donation/<int:pk>/edit/', DonationUpdateView.as_view(), name='donation_update'),
    path('donation/<int:pk>/delete/', DonationDeleteView.as_view(), name='donation_delete'),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)