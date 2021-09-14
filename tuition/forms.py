from django.forms import ModelForm
from django import forms
from django.utils.translation import gettext_lazy as _
from tuition.models import TuitionPost, City


class TuitionPostForm(ModelForm):
    class Meta:
        model = TuitionPost
        fields = ('fullname', 'country', 'city', 'class_other', 'medium', 'subjects', 'school_college',
                  'student_quantity', 'student_gender', 'detail_tuition', 'day_per_week', 'salary',
                  'desire_tutor_gender', 'preference_tuition_style', 'address', 'mobile', 'email',)
        # fields = '__all__'
        # exclude = ("sno", "available")
        labels = {
            'fullname': _('Your full name'),
            'country': _('District'),
            'city': _('Area'),
            'class_other': _('class'),
            'medium': _('medium'),
            'subjects': _('enter subjects'),
            'school_college': _('institution'),
            'student_quantity': _('student quantity'),
            'student_gender': _('student gender'),
            'detail_tuition': _('tuition details'),
            'day_per_week': _('day per week'),
            'salary': _('salary'),
            'desire_tutor_gender': _('tutor gender'),
            'preference_tuition_style': _('where teacher teach'),
            'address': _('Address'),
            'mobile': _('your phone number'),
            'email': _('your email address'),

        }
        widgets = {
            'mobile': forms.TextInput(attrs={'placeholder': '017xxxxxxxx'}),
            'email': forms.TextInput(attrs={'placeholder': 'example@example.com'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')
