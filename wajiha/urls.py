from django.urls import path
from wajiha import views

app_name = 'wajiha'

urlpatterns = [
    path('', views.OpportunityListView.as_view(), name='index'),
    path('opportunity', views.OpportunityListView.as_view(), name='opportunity_list'),
    path('opportunity/<int:pk>/<slug:slug>', views.OpportunityDetailView.as_view(), name='opportunity_detail'),
    path('opportunity/create', views.OpportunityCreationView.as_view(), name='opportunity_create'),
    path('opportunity/create/success', views.OpportunityCreationView.as_view(), name='opportunity_create_success'),
]