from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
from django.utils import timezone

from tuition.models import Country, Subject, Class


class UserProfile(models.Model):
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
        ('Online_Help', 'Online Help'),
        ('Phone_Help', 'Phone Help'),
        ('Provide_Hand_Notes', 'Provide Hand_Notes'),
        ('Video_Tutorials', 'Video Tutorials'),
    )
    Choice_Medium = (
        ('Bangla Medium', 'Bangla Medium'),
        ('English Medium', 'English Medium'),
        ('Arabic Medium', 'Arabic Medium'),
        ('Extra Curricular Activities', 'Extra Curricular Activities'),
        ('Language Learning', 'Language Learning'),
        ('Computer Learning', 'Computer Learning'),
    )
    class_choice = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'),
                    ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('Admission Test', 'Admission Test'),
                    ('KG school', 'KG school'),
                    ('Specific Skill Develop', 'Specific Skill Develop'), ('other', 'other')]
    district_choice = [('Bagerhat', 'Bagerhat'), ('Bandarban', 'Bandarban'), ('Barguna', 'Barguna'),
                       ('Barisal', 'Barisal'), ('Bhola', 'Bhola'), ('Bogra', 'Bogra'), ('Bramanbaria', 'Bramanbaria'),
                       ('Chadpur', 'Chadpur'), ('Chapainababganj', 'Chapainababganj'), ('Chittagong', 'Chittagong'),
                       ('Chuadanga', 'Chuadanga'), ('Comilla', 'Comilla'), ('Cox\'s bazar', 'Cox\'s bazar'),
                       ('Dhaka', 'Dhaka'), ('Dinajpur', 'Dinajpur'), ('Faridpur', 'Faridpur'), ('Feni', 'Feni'),
                       ('Gaibanda', 'Gaibanda'), ('Gazipur', 'Gazipur'), ('Gopalganj', 'Gopalganj'),
                       ('Habiganj', 'Habiganj'), ('Jamalpur', 'Jamalpur'), ('Jessore', 'jessore'),
                       ('Jhalokati', 'Jhalokati'), ('Jheniadaha', 'Jhenaidaha'), ('Joypurhat', 'Joypurhat'),
                       ('Khagrachhari', 'Khagrachhari'), ('Khulna', 'Khulna'), ('Kishoreganj', 'Khishoreganj'),
                       ('Kurigram', 'Kurigram'), ('Kustia', 'Kustia'), ('Lakshmipur', 'Lakshmipur'),
                       ('Lalmanirhat', 'Lalmanirhat'), ('Madaripur', 'Madaripur'), ('Magura', 'Magura'),
                       ('Manikganj', 'Manikganj'), ('Maulvi Bazar', 'Maulvi Bazar'), ('Meherpur', 'Meherpur'),
                       ('Munshiganj', 'Munshiganj'), ('Mymensingh', 'Mymensingh'), ('Naogaon', 'Naogaon'),
                       ('Narail', 'Narail'), ('Narayangonj', 'Narayangonj'), ('Narsingdi', 'Narsingdi'),
                       ('Natore', 'Natore'), ('Netrokona', 'Netrokona'), ('Nilphamari', 'Nilphamari'),
                       ('Noakhali', 'Noakhali'), ('Pabna', 'Pabna'), ('Panchagrah', 'Panchagrah'),
                       ('Patuakhali', 'Patuakhali'), ('Pirojpur', 'Pirojpur'), ('Rajbari', 'Rajbari'),
                       ('Rajshahi', 'Rajshahi'),
                       ('Rangamati', 'Rangamati'), ('Rangpur', 'Rangpur'), ('Satkhira', 'Satkhira'),
                       ('Shariatpur', 'Shariatpur'), ('Sherpur', 'Sherpur'), ('Sirajganj', 'Sirajganj'),
                       ('Sunamganj', 'Sunamganj'), ('Sylhet', 'Sylhet'), ('Tangail', 'Tangail'),
                       ('Thakurgoan', 'Thakurgoan')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField()
    bio_data = models.TextField()

    your_phone_no = models.CharField(max_length=14, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='profile_pic/', default='avatar.png')
    your_pa = models.CharField(max_length=250, null=True)
    your_ca = models.CharField(max_length=250, null=True)
    highest_degree = models.CharField(max_length=250, null=True)

    prefered_tutoring_style = models.CharField(max_length=20, choices=Choice_style, null=True)
    place_of_learning = models.CharField(max_length=25, choices=Choice_Place, null=True)
    tutoring_approach = models.CharField(max_length=50, choices=Choice_Approach, null=True)
    prefer_medium_of_education = models.CharField(max_length=30, choices=Choice_Medium, null=True)
    prefer_class = models.CharField(max_length=50, choices=class_choice, null=True)
    prefer_subjects = models.CharField(max_length=300, null=True)
    expected_salary = models.CharField(max_length=20, default='')
    negotiable = models.BooleanField(default=False)
    demo_class = models.URLField(verbose_name='video tutorial', max_length=1000, null=True, blank=True)
    linkedin = models.URLField(verbose_name='linkedin', max_length=1000, null=True, blank=True)
    whatsapp = models.URLField(verbose_name='whatsapp', max_length=1000, null=True, blank=True)
    fb_id = models.CharField(verbose_name='user facebook id', max_length=1000, null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    is_premium = models.BooleanField(default=False)
    expire_Date = models.DateTimeField(null=True, blank=True)
    district_area = models.CharField(choices=district_choice, max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    AUTH_PROFILE_MODULE = 'app.UserProfile'


class Membership(models.Model):
    Tx_id = models.CharField(max_length=25)
    member_username = models.CharField(max_length=50)
    member_email = models.EmailField(max_length=100)

    def __str__(self):
        return f'{self.Tx_id} | {self.member_username} | {self.member_email}'
