# Generated by Django 3.1.4 on 2021-01-03 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Medium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TuitionPost',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=100)),
                ('class_other', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('Admission Test', 'Admission Test'), ('KG school', 'KG school'), ('Specific Skill Develop', 'Specific Skill Develop'), ('other', 'other')], max_length=23)),
                ('medium', models.CharField(choices=[('English', 'English'), ('Bangla', 'Bangla'), ('Arabic', 'Arabic'), ('Other', 'Other')], default='Bangla', max_length=7)),
                ('subjects', models.CharField(max_length=250)),
                ('school_college', models.CharField(max_length=500)),
                ('student_quantity', models.CharField(max_length=2)),
                ('student_gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Other', max_length=6)),
                ('detail_tuition', models.TextField()),
                ('day_per_week', models.CharField(choices=[('1 day/week', '1 day/week'), ('2 day/week', '2 day/week'), ('3 day/week', '3 day/week'), ('4 day/week', '4 day/week'), ('5 day/week', '5 day/week'), ('6 day/week', '6 day/week'), ('7 day/week', '7 day/week')], default='3 day/week', max_length=10)),
                ('salary', models.CharField(max_length=50)),
                ('desire_tutor_gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Other', max_length=6)),
                ('preference_tuition_style', models.CharField(choices=[('Online', 'Online'), ('Private', 'Private'), ('Coaching', 'Coaching'), ('Group', 'Group')], default='Private', max_length=8)),
                ('address', models.CharField(max_length=250)),
                ('mobile', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=50)),
                ('available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tuition.country')),
            ],
        ),
    ]
