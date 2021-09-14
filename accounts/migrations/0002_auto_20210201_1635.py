# Generated by Django 3.1.5 on 2021-02-01 10:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='demo_class',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='video tutorial'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='expected_salary',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='fb_id',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='user facebook id'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='highest_degree',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='negotiable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='place_of_learning',
            field=models.CharField(choices=[('Class_Rooms', 'Class Rooms'), ('Coaching_Center', 'Coaching Center'), ('Students Home', 'Students Home'), ('Teachers Place', 'Teachers Place')], max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='prefer_class',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('Admission Test', 'Admission Test'), ('KG school', 'KG school'), ('Specific Skill Develop', 'Specific Skill Develop'), ('other', 'other')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='prefer_medium_of_education',
            field=models.CharField(choices=[('Bangla Medium', 'Bangla Medium'), ('English Medium', 'English Medium'), ('Arabic Medium', 'Arabic Medium'), ('Extra Curricular Activities', 'Extra Curricular Activities'), ('Language Learning', 'Language Learning'), ('Computer Learning', 'Computer Learning')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='prefer_subjects',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='prefered_tutoring_style',
            field=models.CharField(choices=[('Group Tuition', 'Group Tuition'), ('Private Tuition', 'Private Tuition')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='tutoring_approach',
            field=models.CharField(choices=[('Online_Help', 'Online Help'), ('Phone_Help', 'Phone Help'), ('Provide_Hand_Notes', 'Provide Hand_Notes'), ('Video_Tutorials', 'Video Tutorials')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='your_ca',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='your_pa',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='your_phone_no',
            field=models.CharField(max_length=14, null=True),
        ),
    ]