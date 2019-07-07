from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView


from wajiha.models import Opportunity

class OpportunityListView(ListView):
    model = Opportunity
    template_name = "wajiha/opportunity_list.html"
    paginate_by = 25


class OpportunityDetailView(DetailView):
    model = Opportunity
    template_name = "wajiha/opportunity_detail.html"

    def get(self, request, *args, **kwargs):
        opportunity = get_object_or_404(self.model, pk=kwargs['pk'])
        context = {'opportunity': opportunity, 'similar_opportunities': Opportunity.objects.all()}
        return render(request, self.template_name, context)

class OpportunityCreateView(CreateView):
    model = Opportunity
    template_name = "wajiha/opportunity_create.html"

    fields = ('title', 'description', 'start_at', 'end_at')
    
    def get_success_url(self):
        return reverse('wajiha:index', current_app=self.request.resolver_match.namespace)
