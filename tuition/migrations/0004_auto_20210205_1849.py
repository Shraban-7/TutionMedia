# Generated by Django 3.1.5 on 2021-02-05 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuition', '0003_auto_20210125_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tuitionpost',
            name='detail_tuition',
            field=models.TextField(blank=True, null=True),
        ),
    ]