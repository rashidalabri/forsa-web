from rest_framework import serializers, pagination
from wajiha.models import Opportunity, OpportunityCategory
from django.core.paginator import Paginator


class OpportunitySerializer(serializers.HyperlinkedModelSerializer):

    category = serializers.HyperlinkedRelatedField(
        view_name='wajiha:opportunitycategory-detail',
        read_only=True,
        many=False
    )

    class Meta:
        model = Opportunity
        fields = ['title', 'description', 'category', 'image', 'start_at', 'end_at',
                  'website', 'phone_number', 'email', 'age_min', 'age_max', 'created_at', 'source_url']


class OpportunityCategorySerializer(serializers.HyperlinkedModelSerializer):
    opportunities = serializers.SerializerMethodField(
        'paginated_opportunities')

    class Meta:
        model = OpportunityCategory
        fields = ['name', 'fontawesome_icon', 'is_featured', 'opportunities']

    def paginated_opportunities(self, obj):
        opportunities = Opportunity.objects.filter(category=obj)
        paginator = pagination.PageNumberPagination()
        page = paginator.paginate_queryset(opportunities, self.context['request'])
        serializer = OpportunitySerializer(page, many=True, context={'request': self.context['request']})
        return paginator.get_paginated_response(serializer.data).data 
