from django.urls import path
from wajiha import views

app_name = 'wajiha'

urlpatterns = [
    path('', views.OpportunityListView.as_view(), name='index'),
    path('p/<int:pk>/', views.OpportunityDetailView.as_view(), name='opportunity_detail'),
    path('create/', views.OpportunityCreateView.as_view(), name='opportunity_create'),
]