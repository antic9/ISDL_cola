# Generated by Django 3.1 on 2020-09-03 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0004_auto_20200903_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='borrower',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
