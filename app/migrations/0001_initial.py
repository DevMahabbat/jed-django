# Generated by Django 4.1.7 on 2023-03-11 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Ad')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='yaranma tarixi')),
            ],
        ),
    ]
