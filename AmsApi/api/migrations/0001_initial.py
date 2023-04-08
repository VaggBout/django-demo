# Generated by Django 4.1.5 on 2023-02-19 19:38

import api.models
from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buildingName', models.CharField(max_length=255)),
                ('location', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ResearchProgramm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('researcher', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('registrationNumber', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=255)),
                ('pieces', models.IntegerField()),
                ('serialNumber', models.TextField()),
                ('invoiceNumber', models.TextField()),
                ('invoiceValue', djongo.models.fields.EmbeddedField(default=None, model_container=api.models.Price)),
                ('acquisitionValue', djongo.models.fields.EmbeddedField(default=None, model_container=api.models.Price)),
                ('taxValue', djongo.models.fields.EmbeddedField(default=None, model_container=api.models.Price)),
                ('supplier', models.TextField(max_length=255)),
                ('office', models.TextField()),
                ('school', models.TextField(choices=[('Enviroment', 'SCHOOL OF ENVIRONMENT, GEOGRAPHY AND APPLIED ECONOMICS'), ('Digital', 'SCHOOL OF DIGITAL TECHNOLOGY'), ('Health', 'SCHOOL OF HEALTH SCIENCE AND EDUCATION')])),
                ('department', models.TextField(choices=[('Economics', 'Economics and Sustainable Development'), ('Geography', 'Geography'), ('Tourism', 'International Master of Sustainable Tourism Development'), ('Informatics', 'Informatics and Telematics'), ('Dietetics', 'Nutrition and Dietetics')])),
                ('assetManager', models.TextField()),
                ('changes_additions', models.TextField()),
                ('invoiceURL', models.URLField()),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.building')),
                ('researchProgramm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.researchprogramm')),
            ],
        ),
    ]