from django import forms

from wajiha.models import Opportunity

class OpportunityCreationForm(forms.ModelForm):

    start_at = forms.DateField(input_formats=['%d-%m-%Y', '%d/%m/%Y', '%d/%m/%y', '%d-%m-%y'], required=False)
    end_at = forms.DateField(input_formats=['%d-%m-%Y', '%d/%m/%Y', '%d/%m/%y', '%d-%m-%y'], required=False)
    website = forms.URLField(required=False)
    phone_number = forms.IntegerField(required=False)
    email = forms.EmailField(required=False)
    age_min = forms.IntegerField(required=False)
    age_max = forms.IntegerField(required=False)

    class Meta:
        model = Opportunity
        fields = ('title', 'description', 'category', 'start_at', 'end_at', 'website', 'phone_number', 'email', 'age_min', 'age_max')