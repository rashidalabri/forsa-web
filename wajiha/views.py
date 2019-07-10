from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic import TemplateView


from django.db.models import Q

from wajiha.models import Opportunity
from wajiha.forms import OpportunityCreationForm

from django.contrib import messages

class OpportunityListView(ListView):
    model = Opportunity
    template_name = "wajiha/opportunity_list.html"
    paginate_by = 30

    def get_queryset(self):
        search_string = self.request.GET.get('q', '')
        return self.model.objects.filter(Q(hidden=False), 
            Q(description__icontains=search_string) | Q(title__icontains=search_string))


class OpportunityDetailView(DetailView):
    model = Opportunity
    template_name = "wajiha/opportunity_detail.html"

    def get(self, request, *args, **kwargs):
        opportunity = get_object_or_404(self.model, pk=kwargs['pk'], slug=kwargs['slug'])
        context = {'opportunity': opportunity, 'similar_opportunities': Opportunity.objects.filter(hidden=False)}
        return render(request, self.template_name, context)

class OpportunityCreationView(FormView):
    template_name = "wajiha/opportunity_create.html"
    form_class = OpportunityCreationForm
    
    def get_success_url(self):
        return reverse('wajiha:opportunity_create_success', current_app=self.request.resolver_match.namespace)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class OpportunityCreationSuccessView(TemplateView):
    template_name = 'wajiha/opportunity_create_success.html'

class ContactView(TemplateView):
    template_name = 'wajiha/contact.html'
