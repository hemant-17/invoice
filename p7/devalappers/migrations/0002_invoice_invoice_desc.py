# Generated by Django 3.0 on 2020-01-11 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devalappers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='invoice_desc',
            field=models.CharField(default='', max_length=500),
        ),
    ]
