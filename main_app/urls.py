from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
    # new route for details!
    path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
    # new route to show form and create finch
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    # routes for update/delete
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
    path('finches/<int:finch_id>/add_sighting/', views.add_sighting, name='add_sighting'),
    path('finches/<int:finch_id>/assoc_predator/<int:predator_id>/', views.assoc_predator, name='assoc_predator'),
    path('predators/', views.PredatorList.as_view(), name='predators_index'),
    path('predators/<int:pk>/', views.PredatorDetail.as_view(), name='predators_detail'),
    path('predators/create/', views.PredatorCreate.as_view(), name='predators_create'),
    path('predators/<int:pk>/update/', views.PredatorUpdate.as_view(), name='predators_update'),
    path('predators/<int:pk>/delete/', views.PredatorDelete.as_view(), name='predators_delete'),
]   
