# Generated by Django 5.1 on 2024-10-25 13:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jobs', '0001_initial'),
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('submitted', 'Soumis'), ('reviewed', 'Examiné'), ('accepted', 'Accepté'), ('rejected', 'Rejeté')], default='submitted', max_length=20)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.job')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile.profile')),
            ],
        ),
    ]
