# Generated by Django 3.1.5 on 2021-02-01 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210201_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='expire_Date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_premium',
            field=models.BooleanField(default=False),
        ),
    ]
