# Generated by Django 5.0.1 on 2024-02-18 08:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_chart', '0003_alter_chart_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chart',
            name='date_in',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]