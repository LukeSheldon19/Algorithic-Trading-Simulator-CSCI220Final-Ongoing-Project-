# Generated by Django 4.2.11 on 2024-04-23 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_alter_company_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='share',
            name='available',
        ),
        migrations.RemoveField(
            model_name='share',
            name='share_price',
        ),
    ]
