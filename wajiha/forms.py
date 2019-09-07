from django import forms

from wajiha.models import Opportunity, OpportunityCategory

class SearchForm(forms.Form):
    text = forms.CharField(required=False, max_length=100)
    category = forms.ModelChoiceField(queryset=OpportunityCategory.objects.all(), required=False)
    start_at = forms.DateField(required=False, input_formats=['%d/%m/%Y'])
    end_at = forms.DateField(required=False, input_formats=['%d/%m/%Y'])
    min_age = forms.DateField(required=False)
    max_age = forms.DateField(required=False)

class OpportunityCreationForm(forms.ModelForm):

    start_at = forms.DateField(input_formats=['%d-%m-%Y', '%d/%m/%Y', '%d/%m/%y', '%d-%m-%y'], required=False)
    end_at = forms.DateField(input_formats=['%d-%m-%Y', '%d/%m/%Y', '%d/%m/%y', '%d-%m-%y'], required=False)
    website = forms.URLField(required=False)
    phone_number = forms.IntegerField(required=False)
    email = forms.EmailField(required=False)
    age_min = forms.IntegerField(required=False)
    age_max = forms.IntegerField(required=False)
    image = forms.ImageField(required=False)

    def __init__(self, *args, **kwargs):
        super(OpportunityCreationForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = 'العنوان'
        self.fields['description'].label = 'التفاصيل'
        self.fields['category'].label = 'نوع الفرصة'
        self.fields['start_at'].label = 'تاريخ الابتداء'
        self.fields['end_at'].label = 'تاريخ الانتهاء'
        self.fields['website'].label = 'الموقع الإلكتروني'
        self.fields['phone_number'].label = 'رقم الهاتف'
        self.fields['email'].label = 'البريد الإلكتروني'
        self.fields['age_min'].label = 'الحد الإدنى للسن'
        self.fields['age_max'].label = 'الحد الأقصى للسن'
        self.fields['image'].label = 'صورة'

    class Meta:
        model = Opportunity
        fields = ('title', 'description', 'category', 'start_at', 'end_at', 'website', 'phone_number', 'email', 'age_min', 'age_max', 'image')