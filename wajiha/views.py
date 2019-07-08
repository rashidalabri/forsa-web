from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView


from wajiha.models import Opportunity
from wajiha.forms import OpportunityCreationForm

class OpportunityListView(ListView):
    queryset = Opportunity.objects.filter(hidden=False)
    template_name = "wajiha/opportunity_list.html"
    paginate_by = 25


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
        return reverse('wajiha:index', current_app=self.request.resolver_match.namespace)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
