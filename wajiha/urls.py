from django.urls import path
from wajiha import views

app_name = 'wajiha'

urlpatterns = [
    path('', views.OpportunityListView.as_view(), name='index'),
    path('opportunity/<int:pk>/<slug:slug>', views.OpportunityDetailView.as_view(), name='opportunity_detail'),
    path('create/', views.OpportunityCreationView.as_view(), name='opportunity_create'),
]