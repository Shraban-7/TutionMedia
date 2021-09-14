from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from accounts.models import UserProfile, Membership


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "This email address is already in use.")
        else:
            return email


class UserProfileForm(forms.ModelForm):
    class Meta:
        class_choice = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'),
                        ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('Admission Test', 'Admission Test'),
                        ('KG school', 'KG school'),
                        ('Specific Skill Develop', 'Specific Skill Develop'), ('other', 'other')]
        Choice_style = (
            ('Group Tuition', 'Group Tuition'),
            ('Private Tuition', 'Private Tuition'),
        )
        Choice_Place = (
            ('Class_Rooms', 'Class Rooms'),
            ('Coaching_Center', 'Coaching Center'),
            ('Students Home', 'Students Home'),
            ('Teachers Place', 'Teachers Place'),
        )
        Choice_Approach = (
            ('Online Help', 'Online Help'),
            ('Phone Help', 'Phone Help'),
            ('Provide Hand Notes', 'Provide Hand Notes'),
            ('Video Tutorials', 'Video Tutorials'),
        )
        Choice_Medium = (
            ('Bangla Medium', 'Bangla Medium'),
            ('English Medium', 'English Medium'),
            ('Arabic Medium', 'Arabic Medium'),
            ('Extra Curricular Activities', 'Extra Curricular Activities'),
            ('Language Learning', 'Language Learning'),
            ('Computer Learning', 'Computer Learning'),
        )
        model = UserProfile
        exclude = ('user', 'date_posted', 'is_premium', 'expire_Date')
        fields = ['image', 'birth_date', 'bio_data', 'your_phone_no', 'fb_id', 'highest_degree', 'expected_salary',
                  'negotiable', 'demo_class', 'district_area', 'prefer_class', 'place_of_learning',
                  'prefer_medium_of_education',
                  'prefered_tutoring_style', 'your_pa', 'your_ca', 'tutoring_approach', 'prefer_subjects', 'linkedin',
                  'whatsapp']

        labels = {
            'image': _('Edit profile picture'),
            'birth_date': _('Your Birth-date'),
            'bio_data': _('Bio'),
            'your_phone_no': _('your phone number'),
            'fb_id': _('your facebook profile link'),
            'highest_degree': _('your highest academic degree'),
            'expected_salary': _('expected salary'),
            'negotiable': _('negotiable'),
            'demo_class': _('demo class'),
            'district_area': _('your service district area'),
            'prefer_class': _('class you prefer'),
            'place_of_learning': _('palace of learning you prefer'),
            'prefer_medium_of_education': _('medium of education'),
            'prefered_tutoring_style': _('tutoring style'),
            'tutoring_approach': _('tutoring approach'),
            'your_pa': _('your permanent address'),
            'your_ca': _('your current address'),
            'prefer_subjects': _('subject you serve'),
            'whatsapp': _('whatsapp link'),
            'linkedin': _('linkedin link'),
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class MemberShipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = '__all__'

# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         exclude = ['user_to']
