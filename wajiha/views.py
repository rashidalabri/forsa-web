from random import shuffle

from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic import TemplateView

from django.db.models import Q
from django.contrib import messages

from wajiha.models import Opportunity, OpportunityCategory
from wajiha.forms import OpportunityCreationForm, SearchForm
from wajiha.helpers import grouped

from rest_framework import viewsets

from wajiha.serializers import OpportunitySerializer, OpportunityCategorySerializer

from django.core.paginator import Paginator


class CategoryListView(ListView):
    template_name = 'wajiha/category_list.html'
    model = OpportunityCategory

    def get_queryset(self):
        return self.model.objects.filter(is_featured=True).order_by('display_order')


class CategoryDetailView(DetailView):
    template_name = 'wajiha/category_detail.html'
    model = OpportunityCategory

    def get_context_data(self, **kwargs):
        category = self.get_object()
        opportunity_list = Opportunity.objects.filter(
            hidden=False, category=category).order_by('-created_at')
        paginator = Paginator(opportunity_list, 9)
        paginated_opportunity_list = paginator.get_page(
            self.request.GET.get('page', 1))
        return {
            'category': category,
            'opportunity_list': paginated_opportunity_list,
        }


class OpportunityListView(ListView):
    model = Opportunity
    template_name = "wajiha/opportunity_list.html"
    paginate_by = 9

    def get_queryset(self):
        objects = self.model.objects.filter(hidden=False)
        form = SearchForm(self.request.GET)
        if form.is_valid():
            params = form.cleaned_data
            objects = self.model.objects.filter(hidden=False)

            if params['text']:
                objects = objects.filter(Q(description__icontains=params['text']) | Q(
                    title__icontains=params['text']))

            if params['category']:
                objects = objects.filter(category=params['category'])

            if params['start_at']:
                objects = objects.filter(start_at__gte=params['start_at'])

            if params['end_at']:
                objects = objects.filter(start_at__lte=params['end_at'])

            if params['min_age']:
                objects = objects.filter(min_age__gte=params['min_age'])

            if params['max_age']:
                objects = objects.filter(max_age__lte=params['max_age'])
        #TODO: add invalid form alert messages to view
        return objects.order_by('-created_at')


class OpportunityDetailView(DetailView):
    model = Opportunity
    template_name = "wajiha/opportunity_detail.html"

    def get(self, request, *args, **kwargs):
        opportunity = get_object_or_404(
            self.model, pk=kwargs['pk'], slug=kwargs['slug'])
        context = {'opportunity': opportunity}
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
