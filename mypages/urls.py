from django.urls import path
from . import views
from allauth.socialaccount import providers

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('create/<slug:slug>/', views.create, name='create'),
    path('create/<slug:slug>/delete/<int:id>/', views.vocab_delete_view, name='vocab-delete'),
    path('create/<slug:slug>/edit/<int:id>/', views.vocab_edit_view, name='vocab-edit'),
    path('delete/<slug:slug>/', views.set_delete_view, name='set-delete'),
    path('pdf/<slug:slug>', views.generate_PDF, name="generate-pdf")
]
